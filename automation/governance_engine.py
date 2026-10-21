#!/usr/bin/env python3
"""Fail-closed diagnostic core for the GOVERNANCA Integration Framework.

Diagnostic and audit modes are read-only with respect to the target repository.
The apply mode remains blocked until the PR-based adapter is explicitly delivered.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator


OFFICIAL_SOURCE = "carlos-andrade/GOVERNANCA"
SCHEMA_RELATIVE = Path("schemas/governanca-config.schema.json")
CATALOG_RELATIVE = Path("catalogs/governance-profile-catalog.json")
CONFIG_RELATIVE = Path(".governanca/config.yml")
VALID_MODES = {"diagnostico", "aplicar", "auditar"}


class GovernanceError(Exception):
    """Expected fail-closed execution error."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_value(root: Path, *args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *args],
            check=True, capture_output=True, text=True, timeout=10,
        )
        return result.stdout.strip() or None
    except (subprocess.SubprocessError, OSError):
        return None


def load_yaml(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return yaml.safe_load(handle)
    except (OSError, yaml.YAMLError) as exc:
        raise GovernanceError(f"Não foi possível ler YAML de forma segura: {exc}") from exc


def load_json_object(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise GovernanceError(f"{label} ausente ou inválido: {exc}") from exc
    if not isinstance(value, dict):
        raise GovernanceError(f"{label} tem de ser um objeto JSON.")
    return value


def validate_config(config: Any, schema_path: Path) -> list[str]:
    schema = load_json_object(schema_path, "Esquema oficial")
    try:
        Draft202012Validator.check_schema(schema)
        return sorted(error.message for error in Draft202012Validator(schema).iter_errors(config))
    except Exception as exc:
        from jsonschema.exceptions import SchemaError
        if isinstance(exc, SchemaError):
            raise GovernanceError(f"Esquema oficial estruturalmente inválido: {exc.message}") from exc
        raise


def validate_catalog(catalog: dict[str, Any]) -> None:
    if catalog.get("schema_version") != 1 or not isinstance(catalog.get("profiles"), dict):
        raise GovernanceError("Catálogo de perfis inválido: schema_version/profiles.")
    for profile, definition in catalog["profiles"].items():
        if not isinstance(definition, dict) or not isinstance(definition.get("complete"), bool):
            raise GovernanceError(f"Definição inválida para o perfil: {profile}")
        requirements = definition.get("requirements")
        if not isinstance(requirements, list):
            raise GovernanceError(f"requirements inválido para o perfil: {profile}")
        seen: set[str] = set()
        for requirement in requirements:
            if not isinstance(requirement, dict):
                raise GovernanceError(f"Requisito inválido no perfil: {profile}")
            rid, kind, relative = requirement.get("id"), requirement.get("kind"), requirement.get("path")
            if not isinstance(rid, str) or not rid or rid in seen:
                raise GovernanceError(f"ID de requisito ausente/duplicado no perfil: {profile}")
            seen.add(rid)
            supported_kinds = {"file_exists", "json_valid", "yaml_valid", "yaml_field_equals", "file_contains"}
            if kind not in supported_kinds or not isinstance(relative, str) or not relative:
                raise GovernanceError(f"Tipo/caminho de requisito não suportado: {profile}/{rid}")
            path = Path(relative)
            if path.is_absolute() or ".." in path.parts:
                raise GovernanceError(f"Caminho de requisito inseguro: {profile}/{rid}")
            if kind == "yaml_field_equals" and (
                not isinstance(requirement.get("field"), str) or not requirement["field"]
                or "value" not in requirement
            ):
                raise GovernanceError(f"Parâmetros field/value obrigatórios: {profile}/{rid}")
            if kind == "file_contains" and (
                not isinstance(requirement.get("value"), str) or not requirement["value"]
            ):
                raise GovernanceError(f"Parâmetro value obrigatório: {profile}/{rid}")


def evaluate_profile(root: Path, profile: str, catalog_path: Path) -> tuple[list[dict[str, Any]], bool, str]:
    catalog = load_json_object(catalog_path, "Catálogo de requisitos por perfil")
    validate_catalog(catalog)
    definition = catalog["profiles"].get(profile)
    if definition is None:
        raise GovernanceError(f"Perfil sem definição no catálogo: {profile}")
    checks: list[dict[str, Any]] = []
    missing: list[str] = []
    root_resolved = root.resolve()
    for requirement in definition["requirements"]:
        target = root / requirement["path"]
        try:
            target_resolved = target.resolve(strict=False)
            target_resolved.relative_to(root_resolved)
        except (OSError, ValueError):
            raise GovernanceError(f"Caminho de requisito sai da raiz do repositório: {profile}/{requirement['id']}")
        kind = requirement["kind"]
        passed = target_resolved.is_file()
        evidence: Any = requirement["path"]
        detail = ""
        if passed and kind == "json_valid":
            try:
                json.loads(target_resolved.read_text(encoding="utf-8"))
            except (OSError, UnicodeError, json.JSONDecodeError) as exc:
                passed, detail = False, f"JSON inválido: {exc}"
        elif passed and kind in {"yaml_valid", "yaml_field_equals"}:
            try:
                parsed = yaml.safe_load(target_resolved.read_text(encoding="utf-8"))
                if kind == "yaml_field_equals":
                    value: Any = parsed
                    found = True
                    for segment in requirement["field"].split("."):
                        if not isinstance(value, dict) or segment not in value:
                            found = False
                            value = None
                            break
                        value = value[segment]
                    expected = requirement["value"]
                    passed = found and value == expected
                    evidence = {"path": requirement["path"], "field": requirement["field"],
                                "expected": expected, "actual": value}
                    if not passed:
                        detail = "Campo YAML ausente ou diferente do valor esperado."
            except (OSError, UnicodeError, yaml.YAMLError) as exc:
                passed, detail = False, f"YAML inválido: {exc}"
        elif passed and kind == "file_contains":
            try:
                content = target_resolved.read_text(encoding="utf-8")
                passed = requirement["value"] in content
                evidence = {"path": requirement["path"], "contains": requirement["value"]}
                if not passed:
                    detail = "Texto obrigatório não encontrado."
            except (OSError, UnicodeError) as exc:
                passed, detail = False, f"Ficheiro não pode ser lido: {exc}"
        check = {
            "id": requirement["id"],
            "result": "PASS" if passed else "FAIL",
            "kind": kind,
            "evidence": evidence,
            "description": requirement.get("description", ""),
        }
        if detail:
            check["detail"] = detail
        checks.append(check)
        if not passed:
            missing.append(requirement["path"])
    return checks, bool(definition["complete"]), ", ".join(missing)


def build_report(
    root: Path, config_path: Path, schema_path: Path, catalog_path: Path | None = None
) -> dict[str, Any]:
    catalog_path = catalog_path or (Path(__file__).resolve().parents[1] / CATALOG_RELATIVE)
    now = datetime.now(timezone.utc).isoformat()
    report: dict[str, Any] = {
        "report_schema_version": 1,
        "framework": "Governance Integration Framework",
        "execution": {
            "timestamp_utc": now,
            "mode": None,
            "repository_path": str(root.resolve()),
            "repository_name": git_value(root, "config", "--get", "remote.origin.url"),
            "repository_commit": git_value(root, "rev-parse", "HEAD"),
            "source": OFFICIAL_SOURCE,
            "source_commit": os.environ.get("GOVERNANCA_SOURCE_COMMIT"),
        },
        "integrity": {},
        "checks": [],
        "blockers": [],
        "status": "DESCONHECIDO",
        "limitations": [
            "O catálogo por perfil cobre verificações estruturais iniciais; não certifica conformidade semântica ou global.",
            "A aplicação por Pull Request não é executada por este motor de diagnóstico.",
        ],
    }
    if not config_path.is_file():
        report["status"] = "NAO_CONFORME"
        report["blockers"].append(f"Configuração obrigatória ausente: {CONFIG_RELATIVE.as_posix()}")
        report["checks"].append({"id": "CFG-001", "result": "FAIL", "evidence": str(config_path)})
        return report

    if not schema_path.is_file():
        raise GovernanceError(f"Esquema de configuração ausente: {schema_path}")

    config = load_yaml(config_path)
    errors = validate_config(config, schema_path)
    report["integrity"] = {
        "config_path": str(config_path),
        "config_sha256": sha256_file(config_path),
        "schema_path": str(schema_path),
        "schema_sha256": sha256_file(schema_path),
    }
    if errors:
        report["status"] = "NAO_CONFORME"
        report["blockers"].append("Configuração inválida segundo o contrato F1.")
        report["checks"].append({"id": "CFG-002", "result": "FAIL", "evidence": errors})
        return report

    gov = config["governanca"]
    profile = gov["perfil"]
    report["execution"]["mode"] = gov["modo"]
    report["execution"]["profile"] = profile
    report["execution"]["configured_source"] = gov["fonte"]
    report["execution"]["pinned_ref"] = gov.get("ref")
    report["checks"].append({
        "id": "CFG-002", "result": "PASS",
        "evidence": "Configuração válida pelo JSON Schema Draft 2020-12.",
    })
    source_ok = gov["fonte"] == OFFICIAL_SOURCE
    report["checks"].append({
        "id": "SRC-001", "result": "PASS" if source_ok else "FAIL",
        "evidence": gov["fonte"],
    })
    report["integrity"]["catalog_path"] = str(catalog_path)
    if not catalog_path.is_file():
        report["status"] = "DESCONHECIDO"
        report["blockers"].append(f"Catálogo por perfil ausente: {catalog_path}")
        return report
    report["integrity"]["catalog_sha256"] = sha256_file(catalog_path)
    try:
        profile_checks, complete, missing = evaluate_profile(root, profile, catalog_path)
    except GovernanceError as exc:
        report["status"] = "DESCONHECIDO"
        report["blockers"].append(str(exc))
        return report
    report["checks"].extend(profile_checks)
    if not profile_checks:
        report["status"] = "DESCONHECIDO"
        report["blockers"].append(
            f"O perfil '{profile}' não tem requisitos executáveis definidos; não é possível avaliar conformidade."
        )
        return report
    if not source_ok or any(item["result"] == "FAIL" for item in profile_checks):
        report["status"] = "NAO_CONFORME"
        if not source_ok:
            report["blockers"].append("A fonte configurada não corresponde à fonte oficial.")
        if missing:
            report["blockers"].append("Ficheiros estruturais obrigatórios ausentes: " + missing)
    elif gov["modo"] == "aplicar":
        report["status"] = "NAO_CONFORME"
        report["blockers"].append(
            "Modo aplicar bloqueado: este motor não altera ficheiros nem abre Pull Requests."
        )
    elif not complete:
        report["status"] = "DESCONHECIDO"
        report["blockers"].append(
            f"O catálogo do perfil '{profile}' está incompleto; os controlos estruturais aprovados não certificam conformidade global."
        )
    else:
        report["status"] = "DESCONHECIDO"
        report["blockers"].append(
            "A conformidade global exige controlos semânticos e evidências adicionais não cobertos pelo catálogo estrutural."
        )
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Raiz do repositório alvo.")
    parser.add_argument("--config", type=Path, default=None, help="Caminho da configuração.")
    parser.add_argument("--schema", type=Path, default=None, help="Caminho do JSON Schema F1.")
    parser.add_argument("--catalog", type=Path, default=None, help="Caminho do catálogo executável por perfil.")
    parser.add_argument("--mode", choices=sorted(VALID_MODES), default=None, help="Sobrepõe o modo apenas para a execução.")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    config_path = (args.config or root / CONFIG_RELATIVE).resolve()
    schema_path = (args.schema or Path(__file__).resolve().parents[1] / SCHEMA_RELATIVE).resolve()
    catalog_path = (args.catalog or Path(__file__).resolve().parents[1] / CATALOG_RELATIVE).resolve()
    try:
        report = build_report(root, config_path, schema_path, catalog_path)
        if args.mode:
            if args.mode == "aplicar":
                report["status"] = "NAO_CONFORME"
                report["blockers"].append("Modo aplicar não disponível no motor de diagnóstico; nenhuma escrita foi efetuada.")
            report["execution"]["mode"] = args.mode
        print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
        return 0 if report["status"] in {"CONFORME", "CONFORME_COM_PENDENCIAS"} else 2
    except GovernanceError as exc:
        print(json.dumps({
            "report_schema_version": 1,
            "status": "NAO_CONFORME",
            "error": str(exc),
            "fail_closed": True,
            "writes_performed": False,
        }, ensure_ascii=False, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
