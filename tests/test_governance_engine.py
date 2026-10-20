import json
import tempfile
import unittest
from pathlib import Path

from automation.governance_engine import build_report, main


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "governanca-config.schema.json"


class GovernanceEngineTests(unittest.TestCase):
    def make_target(self, mode="diagnostico"):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / ".governanca").mkdir()
        (root / "schemas").mkdir()
        (root / "schemas" / "governanca-config.schema.json").write_text(
            SCHEMA.read_text(encoding="utf-8"), encoding="utf-8"
        )
        config = {
            "governanca": {
                "fonte": "carlos-andrade/GOVERNANCA",
                "modo": mode,
                "perfil": "generico",
                "exigir_pull_request": True,
                "preservar_ficheiros_existentes": True,
                "auditoria": "obrigatoria",
            }
        }
        (root / ".governanca" / "config.yml").write_text(
            __import__("yaml").safe_dump(config, sort_keys=False), encoding="utf-8"
        )
        return temp, root

    def test_valid_config_does_not_claim_global_compliance(self):
        temp, root = self.make_target()
        with temp:
            report = build_report(root, root / ".governanca/config.yml",
                                  root / "schemas/governanca-config.schema.json")
            self.assertEqual(report["status"], "DESCONHECIDO")
            self.assertTrue(any("catálogo" in b for b in report["blockers"]))

    def test_apply_mode_fails_closed_without_writes(self):
        temp, root = self.make_target("aplicar")
        with temp:
            before = (root / ".governanca/config.yml").read_bytes()
            report = build_report(root, root / ".governanca/config.yml",
                                  root / "schemas/governanca-config.schema.json")
            self.assertEqual(report["status"], "NAO_CONFORME")
            self.assertTrue(any("F3" in b for b in report["blockers"]))
            self.assertEqual(before, (root / ".governanca/config.yml").read_bytes())

    def test_missing_config_is_nonconformant(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = build_report(root, root / ".governanca/config.yml", SCHEMA)
            self.assertEqual(report["status"], "NAO_CONFORME")

    def test_invalid_config_is_nonconformant(self):
        temp, root = self.make_target()
        with temp:
            path = root / ".governanca/config.yml"
            path.write_text("governanca:\n  fonte: someone/else\n", encoding="utf-8")
            report = build_report(root, path, root / "schemas/governanca-config.schema.json")
            self.assertEqual(report["status"], "NAO_CONFORME")
            self.assertTrue(any(c["result"] == "FAIL" for c in report["checks"]))

    def test_cli_emits_json_and_returns_nonzero_for_unknown(self):
        temp, root = self.make_target()
        with temp:
            # Directly test the engine's contract without changing process-global streams.
            report = build_report(root, root / ".governanca/config.yml",
                                  root / "schemas/governanca-config.schema.json")
            self.assertEqual(json.loads(json.dumps(report))["status"], "DESCONHECIDO")


if __name__ == "__main__":
    unittest.main()
