import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

import yaml

from automation.governance_engine import GovernanceError, build_report


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
            yaml.safe_dump(config, sort_keys=False), encoding="utf-8"
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
            path = root / ".governanca/config.yml"
            before = path.read_bytes()
            report = build_report(root, path, root / "schemas/governanca-config.schema.json")
            self.assertEqual(report["status"], "NAO_CONFORME")
            self.assertTrue(any("F3" in b for b in report["blockers"]))
            self.assertEqual(before, path.read_bytes())

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

    def test_malformed_yaml_fails_closed(self):
        temp, root = self.make_target()
        with temp:
            path = root / ".governanca/config.yml"
            path.write_text("governanca: [unterminated", encoding="utf-8")
            with self.assertRaises(GovernanceError):
                build_report(root, path, root / "schemas/governanca-config.schema.json")

    def test_invalid_schema_fails_closed(self):
        temp, root = self.make_target()
        with temp:
            schema = root / "schemas/governanca-config.schema.json"
            schema.write_text("{not json", encoding="utf-8")
            with self.assertRaises(GovernanceError):
                build_report(root, root / ".governanca/config.yml", schema)

    def test_unknown_properties_and_secrets_are_rejected(self):
        temp, root = self.make_target()
        with temp:
            path = root / ".governanca/config.yml"
            config = yaml.safe_load(path.read_text(encoding="utf-8"))
            config["governanca"]["token"] = "never-store-secrets"
            path.write_text(yaml.safe_dump(config), encoding="utf-8")
            report = build_report(root, path, root / "schemas/governanca-config.schema.json")
            self.assertEqual(report["status"], "NAO_CONFORME")

    def test_report_has_config_and_schema_hashes(self):
        temp, root = self.make_target()
        with temp:
            report = build_report(root, root / ".governanca/config.yml",
                                  root / "schemas/governanca-config.schema.json")
            self.assertEqual(len(report["integrity"]["config_sha256"]), 64)
            self.assertEqual(len(report["integrity"]["schema_sha256"]), 64)

    def test_source_commit_is_unknown_without_explicit_source_evidence(self):
        temp, root = self.make_target()
        with temp:
            report = build_report(root, root / ".governanca/config.yml",
                                  root / "schemas/governanca-config.schema.json")
            self.assertIsNone(report["execution"]["source_commit"])


    def test_source_commit_is_reported_when_explicitly_resolved(self):
        temp, root = self.make_target()
        with temp, patch.dict("os.environ", {"GOVERNANCA_SOURCE_COMMIT": "a" * 40}):
            report = build_report(root, root / ".governanca/config.yml",
                                  root / "schemas/governanca-config.schema.json")
            self.assertEqual(report["execution"]["source_commit"], "a" * 40)


if __name__ == "__main__":
    unittest.main()
