#!/usr/bin/env python3
"""Fail-closed diagnostic core for the GOVERNANCA Integration Framework (F2).

Diagnostic and audit modes are read-only with respect to the target repository.
The apply mode is deliberately blocked until the PR-based adapter is delivered in F3.
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


def validate_config(config: Any, schema_path: Path) -> list[str]:
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise GovernanceError(f"Esquema oficial ausente ou inválido: {exc}") from exc
    Draft202012Validator.check_schema(schema)
    return sorted(error.message for error in Draft202012Validator(schema).iter_errors(config))


def build_report(root: Path, config_path: Path, schema_path: Path) -> dict[str, Any]:
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
            "O catálogo normativo executável por perfil ainda não está implementado; não é possível certificar conformidade global.",
            "A aplicação por Pull Request pertence à F3 e está bloqueada neste motor F2.",
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
        report["checks"].append({
            "id": "CFG-002", "result": "FAIL", "evidence": errors,
        })
        return report

    gov = config["governanca"]
    report["execution"]["mode"] = gov["modo"]
    report["execution"]["profile"] = gov["perfil"]
    report["execution"]["configured_source"] = gov["fonte"]
    report["execution"]["pinned_ref"] = gov.get("ref")
    report["checks"].append({
        "id": "CFG-002", "result": "PASS",
        "evidence": "Configuração válida pelo JSON Schema Draft 2020-12.",
    })
    report["checks"].append({
        "id": "SRC-001",
        "result": "PASS" if gov["fonte"] == OFFICIAL_SOURCE else "FAIL",
        "evidence": gov["fonte"],
    })
    if gov["modo"] == "aplicar":
        report["status"] = "NAO_CONFORME"
        report["blockers"].append(
            "Modo aplicar bloqueado: o adaptador de Pull Request ainda não foi entregue (F3). Nenhum ficheiro foi alterado."
        )
    else:
        report["status"] = "DESCONHECIDO"
        report["blockers"].append(
            "Não existe ainda catálogo de requisitos executáveis para este perfil; a ausência impede certificar conformidade."
        )
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Raiz do repositório alvo.")
    parser.add_argument("--config", type=Path, default=None, help="Caminho da configuração (por defeito .governanca/config.yml).")
    parser.add_argument("--schema", type=Path, default=None, help="Caminho do JSON Schema F1.")
    parser.add_argument("--mode", choices=sorted(VALID_MODES), default=None, help="Sobrepõe o modo apenas para a execução.")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    config_path = (args.config or root / CONFIG_RELATIVE).resolve()
    schema_path = (args.schema or root / SCHEMA_RELATIVE).resolve()
    try:
        report = build_report(root, config_path, schema_path)
        if args.mode:
            if args.mode == "aplicar":
                report["status"] = "NAO_CONFORME"
                report["blockers"].append("Modo aplicar não disponível em F2; nenhuma escrita foi efetuada.")
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
