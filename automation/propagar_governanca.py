#!/usr/bin/env python3
"""Distribui automaticamente as regras canónicas da GOVERNANCA por Pull Request."""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "repositorios-consumidores.json"
BRANCH = "bot/sincronizar-regras-governanca"
TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".py", ".sh", ".toml", ".txt"}
REQUIRED_ROOTS = {
    "CONSTITUICAO.md", "ROADMAP-PADRAO-GOVERNANCA.md",
    "CARTA-CONTRATO-PADRAO-ROADMAP.md", "standards", "docs",
    "templates", "CABEÇALHO", "WATCHDOG",
}

def run(args, cwd=None, check=True):
    """Execute a subprocess and capture output for safe reporting."""
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True, check=check)

def safe_detail(result):
    """Redact credentials before including subprocess diagnostics in reports."""
    detail = (result.stderr or result.stdout or "").strip()
    for secret in (os.getenv("GH_TOKEN"), os.getenv("GITHUB_TOKEN")):
        if secret:
            detail = detail.replace(secret, "[REDACTED]")
    return detail[:1500]

def load_registry():
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or data.get("source_repository") != "carlos-andrade/GOVERNANCA":
        raise ValueError("Esquema ou origem inválida no registo")
    if data.get("policy") != "pull_request_only":
        raise ValueError("A política tem de permanecer pull_request_only")
    roots = data.get("published_roots")
    if not isinstance(roots, list) or set(roots) != REQUIRED_ROOTS:
        raise ValueError("published_roots diverge do âmbito normativo permitido")
    for relative in roots:
        path = PurePosixPath(relative)
        source = ROOT / relative
        if path.is_absolute() or ".." in path.parts or not source.exists():
            raise ValueError("Raiz normativa inválida ou ausente: " + relative)
    repos = data.get("repositories", [])
    names = [item.get("name") for item in repos]
    if len(names) != len(set(names)):
        raise ValueError("Há repositórios duplicados no registo")
    for item in repos:
        name = item.get("name", "")
        if name.count("/") != 1 or any(not part for part in name.split("/")):
            raise ValueError("Nome de repositório inválido: " + name)
        if not isinstance(item.get("enabled"), bool):
            raise ValueError("enabled tem de ser booleano: " + name)
    return data

def discover_files(data):
    files = set()
    for relative in data["published_roots"]:
        source = ROOT / relative
        if source.is_file():
            if source.suffix.lower() in TEXT_SUFFIXES:
                files.add(source.relative_to(ROOT).as_posix())
            continue
        for candidate in source.rglob("*"):
            if candidate.is_file() and not candidate.is_symlink() and candidate.suffix.lower() in TEXT_SUFFIXES:
                files.add(candidate.relative_to(ROOT).as_posix())
    if not files:
        raise ValueError("Nenhum ficheiro normativo elegível encontrado")
    return sorted(files)

def publish_to_repo(name, files, destination_root, source_sha, dry_run):
    with tempfile.TemporaryDirectory(prefix="governanca-sync-") as tmp:
        repo = Path(tmp) / "consumer"
        clone = run(["gh", "repo", "clone", name, str(repo)], check=False)
        if clone.returncode:
            return {"repository": name, "status": "ERROR", "stage": "clone", "detail": safe_detail(clone)}
        head = run(["git", "symbolic-ref", "refs/remotes/origin/HEAD"], cwd=repo, check=False)
        base = head.stdout.strip().split("/")[-1] if head.returncode == 0 else "main"
        for args in [("checkout", base), ("pull", "--ff-only", "origin", base), ("checkout", "-B", BRANCH, base)]:
            step = run(["git", *args], cwd=repo, check=False)
            if step.returncode:
                return {"repository": name, "status": "ERROR", "stage": "git_checkout", "detail": safe_detail(step)}
        destination = repo / destination_root
        if destination.exists():
            shutil.rmtree(destination)
        destination.mkdir(parents=True, exist_ok=True)
        manifest_files = []
        for relative in files:
            source = ROOT / relative
            target = destination.joinpath(*PurePosixPath(relative).parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            manifest_files.append({
                "source_path": relative,
                "destination_path": destination_root + "/" + relative,
                "sha256": hashlib.sha256(source.read_bytes()).hexdigest()
            })
        manifest = {
            "schema_version": 1,
            "source_repository": "carlos-andrade/GOVERNANCA",
            "source_branch": "main",
            "source_commit": source_sha,
            "distribution_policy": "pull_request_only",
            "files": manifest_files,
            "warning": "Espelho de regras canónicas; adoção local exige revisão e aprovação."
        }
        (destination / "UPSTREAM-MANIFEST.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        run(["git", "add", "--", destination_root], cwd=repo)
        changed = run(["git", "diff", "--cached", "--quiet"], cwd=repo, check=False)
        if changed.returncode == 0:
            return {"repository": name, "status": "NO_CHANGE"}
        if dry_run:
            return {"repository": name, "status": "WOULD_OPEN_PR", "files": len(files)}
        run(["git", "config", "user.name", "github-actions[bot]"], cwd=repo)
        run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], cwd=repo)
        run(["git", "commit", "-m", "chore(governanca): atualizar espelho de regras canónicas"], cwd=repo)
        pushed = run(["git", "push", "--force", "origin", "HEAD:refs/heads/" + BRANCH], cwd=repo, check=False)
        if pushed.returncode:
            return {"repository": name, "status": "ERROR", "stage": "git_push", "detail": safe_detail(pushed)}
        listed = run(["gh", "pr", "list", "--repo", name, "--head", BRANCH, "--state", "open", "--json", "url", "--limit", "1"], check=False)
        if listed.returncode:
            return {"repository": name, "status": "ERROR", "stage": "list_prs", "detail": safe_detail(listed)}
        prs = json.loads(listed.stdout or "[]")
        if prs:
            return {"repository": name, "status": "PR_UPDATED", "url": prs[0]["url"]}
        body = (
            "Esta PR sincroniza uma cópia isolada das regras canónicas da GOVERNANCA.\n\n"
            + "Commit de origem: " + source_sha + "\n"
            + "Destino: " + destination_root + "/\n"
            + "Rever, validar e aprovar segundo as regras locais. Não há merge automático "
            + "nem certificação implícita de adoção."
        )
        created = run(["gh", "pr", "create", "--repo", name, "--base", base, "--head", BRANCH,
                       "--title", "chore(governanca): sincronizar regras canónicas", "--body", body], check=False)
        if created.returncode:
            return {"repository": name, "status": "ERROR", "stage": "create_pr", "detail": safe_detail(created)}
        return {"repository": name, "status": "PR_CREATED", "url": created.stdout.strip()}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="simular sem publicar branches/PRs")
    parser.add_argument("--repo", help="processar apenas um consumidor ativo (owner/name)")
    args = parser.parse_args()
    try:
        data = load_registry()
        files = discover_files(data)
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 2
    token = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")
    if not token:
        print(json.dumps({
            "status": "FAIL", "stage": "authentication", "code": "TOKEN_MISSING",
            "error": "GH_TOKEN/GITHUB_TOKEN obrigatório; configure GOVERNANCA_SYNC_TOKEN no repositório de origem."
        }, ensure_ascii=False))
        return 2
    auth = run(["gh", "auth", "status"], check=False)
    if auth.returncode:
        print(json.dumps({
            "status": "FAIL", "stage": "authentication", "code": "TOKEN_INVALID",
            "error": "GitHub CLI rejeitou a credencial. Confirme validade, expiração, revogação e conta do token.",
            "detail": safe_detail(auth)
        }, ensure_ascii=False))
        return 2
    setup = run(["gh", "auth", "setup-git"], check=False)
    if setup.returncode:
        print(json.dumps({
            "status": "FAIL", "stage": "authentication", "code": "GIT_AUTH_SETUP_FAILED",
            "error": "Não foi possível configurar autenticação Git para clone/push.",
            "detail": safe_detail(setup)
        }, ensure_ascii=False))
        return 2
    targets = [item for item in data["repositories"] if item["enabled"]]
    if args.repo:
        targets = [item for item in targets if item["name"].lower() == args.repo.lower()]
        if not targets:
            print("Repositório não registado/ativo: " + args.repo, file=sys.stderr)
            return 2
    source_sha = run(["git", "rev-parse", "HEAD"], cwd=ROOT).stdout.strip()
    results = [publish_to_repo(item["name"], files, data["destination_root"], source_sha, args.dry_run) for item in targets]
    report = {
        "source_repository": "carlos-andrade/GOVERNANCA",
        "source_commit": source_sha,
        "mode": "dry-run" if args.dry_run else "pull-request",
        "files_discovered": len(files),
        "total_repositories": len(results),
        "errors": sum(item["status"] == "ERROR" for item in results),
        "results": results
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["errors"] else 0

if __name__ == "__main__":
    raise SystemExit(main())
