#!/usr/bin/env python3
"""Validate the canonical project scorecard and render README + SVG status views."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "status-do-projeto.json"
README = ROOT / "README.md"
SVG = ROOT / "assets" / "status-dashboard.svg"
START = "<!-- GOVERNANCA_STATUS_START -->"
END = "<!-- GOVERNANCA_STATUS_END -->"
MAX_POINTS = {"inicio": 20, "meio": 60, "fim": 20}
ALLOWED_STATES = {"Não iniciado", "Em início", "Em execução", "Em finalização", "Concluído", "Bloqueado", "Suspenso", "Cancelado"}
CLOSEOUT_KEYS = {"acceptance_validated", "final_review_approved", "delivery_confirmed", "knowledge_transfer_done", "closure_approved"}
PHASE_LABELS = {"inicio": "Início", "meio": "Meio", "fim": "Fim"}


class StatusError(ValueError):
    pass


def _valid_url(url: str) -> bool:
    return urlparse(url).scheme in {"https", "http"}


def load_status(path: Path = REGISTRY) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise StatusError(f"Não foi possível ler o registo de status: {exc}") from exc
    required = ("project", "status", "updated_at", "phase", "points", "criteria", "next_milestone", "blockers", "evidence", "closure_checks", "review_note")
    if data.get("schema_version") != 2:
        raise StatusError("schema_version tem de ser 2.")
    for field in required:
        if field not in data:
            raise StatusError(f"Campo obrigatório ausente: {field}")
    if data["status"] not in ALLOWED_STATES:
        raise StatusError(f"Estado inválido: {data['status']}")
    try:
        date.fromisoformat(data["updated_at"])
        date.fromisoformat(data.get("last_reviewed_at", data["updated_at"]))
    except (TypeError, ValueError) as exc:
        raise StatusError("updated_at e last_reviewed_at têm de usar AAAA-MM-DD.") from exc
    if data["phase"] not in MAX_POINTS:
        raise StatusError("phase tem de ser inicio, meio ou fim.")
    points, criteria = data["points"], data["criteria"]
    if set(points) != set(MAX_POINTS) or set(criteria) != set(MAX_POINTS):
        raise StatusError("points e criteria têm de conter inicio, meio e fim.")
    computed = {}
    for phase, maximum in MAX_POINTS.items():
        items = criteria[phase]
        if not isinstance(items, list) or not items:
            raise StatusError(f"criteria.{phase} tem de ser uma lista não vazia.")
        max_sum = earned_sum = 0
        seen = set()
        for item in items:
            if not isinstance(item, dict) or not all(k in item for k in ("id", "label", "max_points", "earned_points", "evidence")):
                raise StatusError(f"Critério malformado em {phase}: {item!r}")
            if item["id"] in seen:
                raise StatusError(f"ID de critério duplicado em {phase}: {item['id']}")
            seen.add(item["id"])
            maximum_item, earned = item["max_points"], item["earned_points"]
            if not isinstance(maximum_item, int) or isinstance(maximum_item, bool) or maximum_item <= 0:
                raise StatusError(f"max_points inválido em {item['id']}")
            if not isinstance(earned, int) or isinstance(earned, bool) or not 0 <= earned <= maximum_item:
                raise StatusError(f"earned_points inválido em {item['id']}")
            if not isinstance(item["evidence"], list) or not all(isinstance(u, str) and _valid_url(u) for u in item["evidence"]):
                raise StatusError(f"evidence inválida em {item['id']}")
            if earned > 0 and not item["evidence"]:
                raise StatusError(f"Critério pontuado sem evidência: {item['id']}")
            max_sum += maximum_item
            earned_sum += earned
        if max_sum != maximum:
            raise StatusError(f"Critérios de {phase} somam {max_sum}; esperado {maximum}.")
        if not isinstance(points[phase], int) or isinstance(points[phase], bool) or points[phase] != earned_sum:
            raise StatusError(f"points.{phase}={points[phase]} diverge da soma comprovada dos critérios ({earned_sum}).")
        computed[phase] = earned_sum
    total = sum(computed.values())
    checks = data["closure_checks"]
    if not isinstance(checks, dict) or set(checks) != CLOSEOUT_KEYS or any(not isinstance(v, bool) for v in checks.values()):
        raise StatusError("closure_checks deve conter os cinco controlos finais booleanos.")
    if total == 100 and (data["status"] != "Concluído" or not all(checks.values())):
        raise StatusError("100% exige estado Concluído e todos os controlos finais aprovados.")
    if data["status"] == "Concluído" and (total != 100 or not all(checks.values())):
        raise StatusError("O estado Concluído exige 100 pontos e todos os controlos finais aprovados.")
    if data["status"] not in {"Bloqueado", "Suspenso", "Cancelado", "Concluído"}:
        expected = "Não iniciado" if total == 0 else "Em início" if total <= 20 else "Em execução" if total < 80 else "Em finalização"
        if data["status"] != expected:
            raise StatusError(f"Estado incompatível com {total}%: esperado '{expected}'.")
    if not isinstance(data["blockers"], list) or not all(isinstance(x, str) for x in data["blockers"]):
        raise StatusError("blockers tem de ser uma lista de textos.")
    if not isinstance(data["evidence"], list):
        raise StatusError("evidence tem de ser uma lista.")
    for item in data["evidence"]:
        if not isinstance(item, dict) or not item.get("label") or not item.get("url") or not _valid_url(item["url"]):
            raise StatusError("Cada evidência tem de ter label e URL HTTP(S) válido.")
    if not isinstance(data["review_note"], str) or not data["review_note"].strip():
        raise StatusError("review_note tem de explicar o alcance da revisão.")
    return data


def render_block(data: dict) -> str:
    points = data["points"]
    percent = sum(points.values())
    filled = percent // 5
    bar = "█" * filled + "░" * (20 - filled)
    evidence = " · ".join(f"[{x['label']}]({x['url']})" for x in data["evidence"]) or "Nenhuma evidência ligada"
    phase_label = PHASE_LABELS[data["phase"]]
    phase_rows = []
    for key in ("inicio", "meio", "fim"):
        state = "Concluído" if points[key] == MAX_POINTS[key] else "Em curso" if points[key] else "Pendente"
        phase_rows.append(f"| **{PHASE_LABELS[key]}** | {points[key]}/{MAX_POINTS[key]} | {MAX_POINTS[key]}% | {state} |")
    blockers = "\n".join(f"- {item}" for item in data["blockers"]) if data["blockers"] else "- Nenhum bloqueio registado."
    return f"""{START}
## Painel executivo de status — {data['project']}

![Painel visual de status: {percent}% comprovados](assets/status-dashboard.svg)

**{percent}% comprovados** · `[{bar}] {percent}%` · **Estado:** {data['status']} · **Fase:** {phase_label}

| Fase | Pontos comprovados | Peso máximo | Estado |
|---|---:|---:|---|
{chr(10).join(phase_rows)}

**Próximo marco:** {data['next_milestone']}

**Bloqueios ativos ({len(data['blockers'])}):**
{blockers}

**Última revisão:** {data.get('last_reviewed_at', data['updated_at'])} · **Atualização do registo:** {data['updated_at']}

> **Limite da revisão:** {data['review_note']}

**Evidências:** {evidence}

> **Fonte de verdade:** `registry/status-do-projeto.json`. O script valida os critérios pontuados e gera este painel Markdown e o SVG. Não editar manualmente este bloco. Uma fase só recebe pontos se tiver evidência; 100% exige aprovação explícita de todos os controlos de encerramento.
{END}"""


def render_svg(data: dict) -> str:
    total = sum(data["points"].values())
    state_color = "#22c55e" if total == 100 else "#f59e0b" if data["blockers"] else "#38bdf8"
    state = html.escape(data["status"])
    project = html.escape(data["project"])
    milestone = html.escape(data["next_milestone"])
    reviewed = html.escape(data.get("last_reviewed_at", data["updated_at"]))
    cards = []
    for x, key in zip((44, 354, 664), ("inicio", "meio", "fim")):
        pts, max_pts = data["points"][key], MAX_POINTS[key]
        pct = round(100 * pts / max_pts)
        color = "#22c55e" if pts == max_pts else "#f59e0b" if pts else "#64748b"
        label = html.escape(PHASE_LABELS[key])
        phase_state = "Concluído" if pts == max_pts else "Em curso" if pts else "Pendente"
        cards.append(f'<rect x="{x}" y="171" width="292" height="78" rx="13" fill="#111c32" stroke="#293852"/><text x="{x+16}" y="196" font-size="14" fill="#a7b6cf">{label}</text><text x="{x+16}" y="226" font-size="23" font-weight="700" fill="#f8fafc">{pts}/{max_pts}</text><text x="{x+272}" y="196" text-anchor="end" font-size="12" fill="{color}">{phase_state}</text><rect x="{x+16}" y="235" width="260" height="5" rx="2.5" fill="#26364f"/><rect x="{x+16}" y="235" width="{260*pct/100:.1f}" height="5" rx="2.5" fill="{color}"/>')
    milestone_a, milestone_b = milestone[:112], milestone[112:224]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="390" viewBox="0 0 1000 390" role="img" aria-labelledby="title desc">
<title id="title">{project} — painel de status</title>
<desc id="desc">{total}% de conclusão comprovada. Estado {state}. {len(data["blockers"])} bloqueios ativos.</desc>
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1220"/><stop offset="1" stop-color="#17243a"/></linearGradient><linearGradient id="progress" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#38bdf8"/><stop offset="1" stop-color="#818cf8"/></linearGradient></defs>
<rect width="1000" height="390" rx="22" fill="url(#bg)"/>
<text x="44" y="48" font-size="13" font-weight="700" letter-spacing="2" fill="#8fa3c4">GOVERNANÇA / EXECUTIVE STATUS</text>
<text x="44" y="86" font-size="26" font-weight="700" fill="#f8fafc">{project}</text>
<rect x="790" y="32" width="166" height="34" rx="17" fill="#2b261b" stroke="#72501a"/><circle cx="808" cy="49" r="4" fill="{state_color}"/><text x="821" y="54" font-size="12" font-weight="600" fill="#fde68a">{state}</text>
<text x="44" y="130" font-size="39" font-weight="750" fill="#f8fafc">{total}%</text>
<text x="150" y="129" font-size="13" fill="#a7b6cf">conclusão comprovada</text>
<text x="956" y="128" font-size="12" text-anchor="end" fill="#a7b6cf">{len(data["blockers"])} bloqueios ativos</text>
<rect x="44" y="143" width="912" height="9" rx="4.5" fill="#26364f"/><rect x="44" y="143" width="{912*total/100:.1f}" height="9" rx="4.5" fill="url(#progress)"/>
{''.join(cards)}
<text x="44" y="282" font-size="11" font-weight="700" letter-spacing="1.4" fill="#8fa3c4">PRÓXIMO MARCO</text>
<text x="44" y="305" font-size="13" fill="#e2e8f0">{milestone_a}</text>
<text x="44" y="325" font-size="13" fill="#e2e8f0">{milestone_b}</text>
<line x1="44" y1="347" x2="956" y2="347" stroke="#293852"/>
<text x="44" y="369" font-size="11" fill="#8fa3c4">Revisão: {reviewed} · Pontuação baseada em critérios com evidência</text>
<text x="956" y="369" font-size="11" text-anchor="end" fill="#8fa3c4">GOV-CONTROL / STATUS v2</text>
</svg>
'''



def canonical_sha256(text: str) -> str:
    """Hash UTF-8/LF document content excluding the two control metadata rows."""
    normalized = text.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")
    canonical = "".join(
        line for line in normalized.splitlines(keepends=True)
        if not line.startswith("| **SHA-256 (conteúdo canónico)**")
        and not line.startswith("| **Commit de referência (versão anterior)**")
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def update_canonical_hash(text: str) -> str:
    """Update the canonical checksum when a document has the standard metadata row."""
    lines = text.splitlines(keepends=True)
    indices = [
        index for index, line in enumerate(lines)
        if line.startswith("| **SHA-256 (conteúdo canónico)**")
    ]
    if not indices:
        return text
    if len(indices) != 1:
        raise StatusError("README deve conter no máximo uma linha SHA-256 canónico.")
    index = indices[0]
    ending = "\r\n" if lines[index].endswith("\r\n") else "\n" if lines[index].endswith("\n") else ""
    lines[index] = f"| **SHA-256 (conteúdo canónico)** | {canonical_sha256(text)} |{ending}"
    return "".join(lines)


def sync(readme_path: Path = README, registry_path: Path = REGISTRY, svg_path: Path = SVG, check_only: bool = False) -> bool:
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
    new_text = update_canonical_hash(new_text)
    svg_text = render_svg(data)
    old_svg = svg_path.read_text(encoding="utf-8") if svg_path.exists() else ""
    if check_only:
        if new_text != text:
            raise StatusError("README desatualizado: executar automation/sync_project_status.py.")
        if svg_text != old_svg:
            raise StatusError("SVG desatualizado: executar automation/sync_project_status.py.")
        return False
    changed = False
    if new_text != text:
        readme_path.write_text(new_text, encoding="utf-8")
        changed = True
    if svg_text != old_svg:
        svg_path.parent.mkdir(parents=True, exist_ok=True)
        svg_path.write_text(svg_text, encoding="utf-8")
        changed = True
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Falha se README ou SVG não corresponderem ao registo.")
    args = parser.parse_args()
    try:
        changed = sync(check_only=args.check)
    except StatusError as exc:
        print(f"ERRO DE STATUS: {exc}", file=sys.stderr)
        return 1
    print("Painel já sincronizado." if not changed else "README e SVG atualizados a partir do registo canónico.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
