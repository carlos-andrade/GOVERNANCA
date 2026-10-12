#!/usr/bin/env python3
"""Synchronize the GOVERNANCA README status panel from the canonical JSON registry."""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "status-do-projeto.json"
README = ROOT / "README.md"
START = "<!-- GOVERNANCA_STATUS_START -->"
END = "<!-- GOVERNANCA_STATUS_END -->"
MAX_POINTS = {"inicio": 20, "meio": 60, "fim": 20}
ALLOWED_STATES = {"Não iniciado", "Em início", "Em execução", "Em finalização", "Concluído", "Bloqueado", "Suspenso", "Cancelado"}
CLOSEOUT_KEYS = {"acceptance_validated", "final_review_approved", "delivery_confirmed", "knowledge_transfer_done", "closure_approved"}


class StatusError(ValueError):
    pass


def load_status(path: Path = REGISTRY) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise StatusError(f"Não foi possível ler o registo de status: {exc}") from exc
    if data.get("schema_version") != 1:
        raise StatusError("schema_version tem de ser 1.")
    for field in ("project", "status", "updated_at", "phase", "points", "next_milestone", "blockers", "evidence", "closure_checks"):
        if field not in data:
            raise StatusError(f"Campo obrigatório ausente: {field}")
    if data["status"] not in ALLOWED_STATES:
        raise StatusError(f"Estado inválido: {data['status']}")
    try:
        date.fromisoformat(data["updated_at"])
    except (TypeError, ValueError) as exc:
        raise StatusError("updated_at tem de usar AAAA-MM-DD.") from exc
    points = data["points"]
    if set(points) != set(MAX_POINTS):
        raise StatusError("points tem de conter exatamente inicio, meio e fim.")
    for phase, maximum in MAX_POINTS.items():
        value = points[phase]
        if not isinstance(value, int) or isinstance(value, bool) or value < 0 or value > maximum:
            raise StatusError(f"Pontuação inválida para {phase}: deve ser um inteiro entre 0 e {maximum}.")
    total = sum(points.values())
    checks = data["closure_checks"]
    if not isinstance(checks, dict) or set(checks) != CLOSEOUT_KEYS or any(not isinstance(v, bool) for v in checks.values()):
        raise StatusError("closure_checks deve conter os cinco controlos finais booleanos.")
    if total == 100 and (data["status"] != "Concluído" or not all(checks.values())):
        raise StatusError("100% exige estado Concluído e todos os controlos finais aprovados.")
    if data["status"] == "Concluído" and total != 100:
        raise StatusError("O estado Concluído exige 100 pontos comprovados.")
    if data["status"] not in {"Bloqueado", "Suspenso", "Cancelado", "Concluído"}:
        expected = "Não iniciado" if total == 0 else "Em início" if total <= 20 else "Em execução" if total < 80 else "Em finalização"
        if data["status"] != expected:
            raise StatusError(f"Estado incompatível com {total}%: esperado '{expected}'.")
    if not isinstance(data["blockers"], list) or not all(isinstance(x, str) for x in data["blockers"]):
        raise StatusError("blockers tem de ser uma lista de textos.")
    if not isinstance(data["evidence"], list):
        raise StatusError("evidence tem de ser uma lista.")
    for item in data["evidence"]:
        if not isinstance(item, dict) or not item.get("label") or not item.get("url"):
            raise StatusError("Cada evidência tem de ter label e url.")
        if urlparse(item["url"]).scheme not in {"https", "http"}:
            raise StatusError(f"URL de evidência inválido: {item['url']}")
    return data


def render_block(data: dict) -> str:
    points = data["points"]
    percent = sum(points.values())
    filled = percent // 5
    bar = "█" * filled + "░" * (20 - filled)
    blockers = "; ".join(data["blockers"]) if data["blockers"] else "Nenhum bloqueio registado"
    evidence = " · ".join(f"[{x['label']}]({x['url']})" for x in data["evidence"]) or "Nenhuma evidência ligada"
    phase_label = {"inicio": "Início", "meio": "Meio", "fim": "Fim"}[data["phase"].lower()]
    return f"""{START}
## Barra de status do {data['project']}

**Estado atual:** {data['status']} — fase {phase_label}.  
**Percentual comprovado:** **{percent}%**  
`[{bar}] {percent}%`

| Fase | Pontos | Peso | Estado |
|---|---:|---:|---|
| **Início** | {points['inicio']}/20 | 20% | {"Concluído" if points['inicio'] == 20 else "Em curso" if points['inicio'] else "Pendente"} |
| **Meio** | {points['meio']}/60 | 60% | {"Concluído" if points['meio'] == 60 else "Em curso" if points['meio'] else "Pendente"} |
| **Fim** | {points['fim']}/20 | 20% | {"Concluído" if points['fim'] == 20 else "Em curso" if points['fim'] else "Pendente"} |

**Próximo marco:** {data['next_milestone']}  
**Bloqueios:** {blockers}  
**Última atualização do estado:** {data['updated_at']}  
**Evidências:** {evidence}

> **Atualização automática:** este painel é gerado a partir de `registry/status-do-projeto.json`. Alterações nesse registo acionam o workflow `Sincronizar barra de status`. O workflow valida o esquema, as pontuações e os critérios de encerramento antes de atualizar este README. Não editar manualmente o painel; alterar a fonte de verdade e rever o resultado do workflow.
{END}"""


def sync(readme_path: Path = README, registry_path: Path = REGISTRY, check_only: bool = False) -> bool:
    data = load_status(registry_path)
    text = readme_path.read_text(encoding="utf-8")
    if text.count(START) != 1 or text.count(END) != 1:
        raise StatusError(f"README deve conter exatamente um marcador {START} e um {END}.")
    if text.index(START) > text.index(END):
        raise StatusError("Marcadores de status fora de ordem.")
    block = render_block(data)
    pattern = re.escape(START) + r"[\s\S]*?" + re.escape(END)
    new_text, count = re.subn(pattern, lambda _: block, text, count=1)
    if count != 1:
        raise StatusError("Não foi possível substituir o painel de status.")
    if check_only:
        if new_text != text:
            raise StatusError("README desatualizado: executar automation/sync_project_status.py.")
        return False
    if new_text != text:
        readme_path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Falha se README não corresponder ao registo.")
    args = parser.parse_args()
    try:
        changed = sync(check_only=args.check)
    except StatusError as exc:
        print(f"ERRO DE STATUS: {exc}", file=sys.stderr)
        return 1
    print("README já sincronizado." if not changed else "README atualizado a partir do registo de status.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
