import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "automation" / "sync_project_status.py"
SPEC = importlib.util.spec_from_file_location("sync_project_status", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)

EVIDENCE = ["https://example.com/evidence"]


def criterion(cid, label, maximum, earned):
    return {"id": cid, "label": label, "max_points": maximum, "earned_points": earned,
            "evidence": EVIDENCE if earned else []}


def sample_status():
    return {
        "schema_version": 2,
        "project": "TESTE",
        "status": "Em finalização",
        "updated_at": "2026-10-17",
        "last_reviewed_at": "2026-10-17",
        "phase": "fim",
        "points": {"inicio": 20, "meio": 60, "fim": 0},
        "criteria": {
            "inicio": [
                criterion("i1", "Objetivo", 5, 5),
                criterion("i2", "Responsáveis", 3, 3),
                criterion("i3", "Escopo", 4, 4),
                criterion("i4", "Riscos", 4, 4),
                criterion("i5", "Aceitação", 4, 4),
            ],
            "meio": [
                criterion("m1", "Entregáveis", 30, 30),
                criterion("m2", "Rastreabilidade", 10, 10),
                criterion("m3", "Testes", 10, 10),
                criterion("m4", "Documentação", 5, 5),
                criterion("m5", "Riscos tratados", 5, 5),
            ],
            "fim": [
                criterion("f1", "Aceitação", 8, 0),
                criterion("f2", "Revisão final", 4, 0),
                criterion("f3", "Entrega", 3, 0),
                criterion("f4", "Transferência", 2, 0),
                criterion("f5", "Aprovação", 3, 0),
            ],
        },
        "next_milestone": "Validar encerramento",
        "blockers": [],
        "review_note": "Revisão efetuada.",
        "evidence": [{"label": "Teste", "url": "https://example.com/teste"}],
        "closure_checks": {
            "acceptance_validated": False,
            "final_review_approved": False,
            "delivery_confirmed": False,
            "knowledge_transfer_done": False,
            "closure_approved": False,
        },
    }


class StatusSyncTests(unittest.TestCase):
    def test_percent_and_modern_panel_are_calculated_from_criteria(self):
        data = sample_status()
        self.assertEqual(sum(data["points"].values()), 80)
        block = module.render_block(data)
        self.assertIn("80%", block)
        self.assertIn("[████████████████░░░░] 80%", block)
        self.assertIn("assets/status-dashboard.svg", block)
        svg = module.render_svg(data)
        self.assertIn("<svg", svg)
        self.assertIn("80%", svg)
        self.assertIn("3", svg)

    def test_points_must_match_criterion_evidence_score(self):
        data = sample_status()
        data["criteria"]["meio"][0]["earned_points"] = 20
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "status.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaises(module.StatusError):
                module.load_status(path)

    def test_awarded_points_require_evidence(self):
        data = sample_status()
        data["criteria"]["inicio"][0]["evidence"] = []
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "status.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaises(module.StatusError):
                module.load_status(path)

    def test_100_percent_requires_approved_closeout(self):
        data = sample_status()
        for key in ("inicio", "meio", "fim"):
            for item in data["criteria"][key]:
                item["earned_points"] = item["max_points"]
                item["evidence"] = EVIDENCE
        data["points"] = {"inicio": 20, "meio": 60, "fim": 20}
        data["status"] = "Concluído"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "status.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaises(module.StatusError):
                module.load_status(path)

    def test_inconsistent_status_is_rejected(self):
        data = sample_status()
        data["status"] = "Concluído"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "status.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaises(module.StatusError):
                module.load_status(path)

    def test_canonical_hash_is_updated_and_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            readme = root / "README.md"
            text = (
                "# Documento\n"
                "| Campo | Valor |\n"
                "|---|---|\n"
                "| **SHA-256 (conteúdo canónico)** | stale |\n"
                "| **Commit de referência (versão anterior)** | abc |\n"
                "\nCorpo original.\n"
            )
            readme.write_text(text, encoding="utf-8")
            updated = module.update_canonical_hash(text)
            self.assertNotEqual(updated, text)
            digest = updated.split("**SHA-256 (conteúdo canónico)** | ", 1)[1].split(" |", 1)[0]
            self.assertEqual(len(digest), 64)
            self.assertEqual(digest, module.canonical_sha256(updated))
            self.assertEqual(module.update_canonical_hash(updated), updated)

    def test_sync_readme_and_svg_and_check(self):
        data = sample_status()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry = root / "status.json"
            readme = root / "README.md"
            svg = root / "assets" / "status-dashboard.svg"
            registry.write_text(json.dumps(data), encoding="utf-8")
            readme.write_text("Antes\n" + module.START + "\nPainel antigo\n" + module.END + "\nDepois\n", encoding="utf-8")
            self.assertTrue(module.sync(readme, registry, svg))
            self.assertIn("assets/status-dashboard.svg", readme.read_text(encoding="utf-8"))
            self.assertIn("<svg", svg.read_text(encoding="utf-8"))
            self.assertFalse(module.sync(readme, registry, svg, check_only=True))


if __name__ == "__main__":
    unittest.main()
