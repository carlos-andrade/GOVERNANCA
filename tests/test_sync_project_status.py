import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "automation" / "sync_project_status.py"
SPEC = importlib.util.spec_from_file_location("sync_project_status", MODULE_PATH)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


def sample_status():
    return {
        "schema_version": 1,
        "project": "TESTE",
        "status": "Em finalização",
        "updated_at": "2026-10-12",
        "phase": "fim",
        "points": {"inicio": 20, "meio": 60, "fim": 0},
        "next_milestone": "Validar encerramento",
        "blockers": [],
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
    def test_percent_and_bar_are_calculated_from_points(self):
        block = module.render_block(sample_status())
        self.assertIn("80%", block)
        self.assertIn("[████████████████░░░░] 80%", block)

    def test_100_percent_requires_approved_closeout(self):
        data = sample_status()
        data["points"]["fim"] = 20
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

    def test_sync_and_check(self):
        data = sample_status()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry = root / "status.json"
            readme = root / "README.md"
            registry.write_text(json.dumps(data), encoding="utf-8")
            readme.write_text("Antes\n" + module.START + "\nPainel antigo\n" + module.END + "\nDepois\n", encoding="utf-8")
            self.assertTrue(module.sync(readme, registry))
            self.assertFalse(module.sync(readme, registry, check_only=True))


if __name__ == "__main__":
    unittest.main()
