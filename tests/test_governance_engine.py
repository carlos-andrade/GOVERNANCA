import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

import yaml

from automation.governance_engine import GovernanceError, build_report


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "governanca-config.schema.json"
CATALOG = ROOT / "catalogs" / "governance-profile-catalog.json"


class GovernanceEngineTests(unittest.TestCase):
    def make_target(self, mode="diagnostico", profile="generico", with_readme=True, with_workflow=True):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / ".governanca").mkdir()
        (root / "schemas").mkdir()
        (root / "catalogs").mkdir()
        (root / ".github" / "workflows").mkdir(parents=True)
        (root / "schemas" / "governanca-config.schema.json").write_text(
            SCHEMA.read_text(encoding="utf-8"), encoding="utf-8"
        )
        (root / "catalogs" / "governance-profile-catalog.json").write_text(
            CATALOG.read_text(encoding="utf-8"), encoding="utf-8"
        )
        if with_readme:
            (root / "README.md").write_text("# Target\n", encoding="utf-8")
        if with_workflow:
            (root / ".github" / "workflows" / "governance-integration.yml").write_text(
                "name: diagnostic\n", encoding="utf-8"
            )
        config = {
            "governanca": {
                "fonte": "carlos-andrade/GOVERNANCA",
                "modo": mode,
                "perfil": profile,
                "exigir_pull_request": True,
                "preservar_ficheiros_existentes": True,
                "auditoria": "obrigatoria",
            }
        }
        (root / ".governanca" / "config.yml").write_text(
            yaml.safe_dump(config, sort_keys=False), encoding="utf-8"
        )
        return temp, root

    def report(self, root):
        return build_report(
            root, root / ".governanca/config.yml",
            root / "schemas/governanca-config.schema.json",
            root / "catalogs/governance-profile-catalog.json",
        )

    def test_valid_config_does_not_claim_global_compliance(self):
        temp, root = self.make_target()
        with temp:
            report = self.report(root)
            self.assertEqual(report["status"], "DESCONHECIDO")
            self.assertTrue(any("catálogo" in b for b in report["blockers"]))
            self.assertTrue(any(c["id"] == "GEN-STR-001" and c["result"] == "PASS" for c in report["checks"]))

    def test_data_profile_evaluates_profile_specific_requirements(self):
        temp, root = self.make_target(profile="dados")
        with temp:
            report = self.report(root)
            self.assertEqual(report["status"], "DESCONHECIDO")
            ids = {c["id"] for c in report["checks"]}
            self.assertIn("DAD-STR-001", ids)
            self.assertIn("DAD-STR-002", ids)
            self.assertTrue(any("incompleto" in b for b in report["blockers"]))

    def test_missing_profile_requirement_is_nonconformant(self):
        temp, root = self.make_target(profile="dados", with_workflow=False)
        with temp:
            report = self.report(root)
            self.assertEqual(report["status"], "NAO_CONFORME")
            self.assertTrue(any(c["id"] == "DAD-STR-002" and c["result"] == "FAIL" for c in report["checks"]))

    def test_apply_mode_fails_closed_without_writes(self):
        temp, root = self.make_target("aplicar")
        with temp:
            path = root / ".governanca/config.yml"
            before = path.read_bytes()
            report = self.report(root)
            self.assertEqual(report["status"], "NAO_CONFORME")
            self.assertTrue(any("Modo aplicar" in b for b in report["blockers"]))
            self.assertEqual(before, path.read_bytes())

    def test_missing_config_is_nonconformant(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = build_report(root, root / ".governanca/config.yml", SCHEMA, CATALOG)
            self.assertEqual(report["status"], "NAO_CONFORME")

    def test_invalid_config_is_nonconformant(self):
        temp, root = self.make_target()
        with temp:
            path = root / ".governanca/config.yml"
            path.write_text("governanca:\n  fonte: someone/else\n", encoding="utf-8")
            report = self.report(root)
            self.assertEqual(report["status"], "NAO_CONFORME")
            self.assertTrue(any(c["result"] == "FAIL" for c in report["checks"]))

    def test_malformed_yaml_fails_closed(self):
        temp, root = self.make_target()
        with temp:
            path = root / ".governanca/config.yml"
            path.write_text("governanca: [unterminated", encoding="utf-8")
            with self.assertRaises(GovernanceError):
                self.report(root)

    def test_invalid_schema_fails_closed(self):
        temp, root = self.make_target()
        with temp:
            schema = root / "schemas/governanca-config.schema.json"
            schema.write_text("{not json", encoding="utf-8")
            with self.assertRaises(GovernanceError):
                build_report(root, root / ".governanca/config.yml", schema, CATALOG)

    def test_invalid_catalog_fails_closed(self):
        temp, root = self.make_target()
        with temp:
            catalog = root / "catalogs/governance-profile-catalog.json"
            catalog.write_text("{not json", encoding="utf-8")
            with self.assertRaises(GovernanceError):
                self.report(root)

    def test_unknown_properties_and_secrets_are_rejected(self):
        temp, root = self.make_target()
        with temp:
            path = root / ".governanca/config.yml"
            config = yaml.safe_load(path.read_text(encoding="utf-8"))
            config["governanca"]["token"] = "never-store-secrets"
            path.write_text(yaml.safe_dump(config), encoding="utf-8")
            self.assertEqual(self.report(root)["status"], "NAO_CONFORME")

    def test_report_has_config_schema_and_catalog_hashes(self):
        temp, root = self.make_target()
        with temp:
            report = self.report(root)
            self.assertEqual(len(report["integrity"]["config_sha256"]), 64)
            self.assertEqual(len(report["integrity"]["schema_sha256"]), 64)
            self.assertEqual(len(report["integrity"]["catalog_sha256"]), 64)

    def test_source_commit_is_unknown_without_explicit_source_evidence(self):
        temp, root = self.make_target()
        with temp:
            self.assertIsNone(self.report(root)["execution"]["source_commit"])

    def test_source_commit_is_reported_when_explicitly_resolved(self):
        temp, root = self.make_target()
        with temp, patch.dict("os.environ", {"GOVERNANCA_SOURCE_COMMIT": "a" * 40}):
            self.assertEqual(self.report(root)["execution"]["source_commit"], "a" * 40)


if __name__ == "__main__":
    unittest.main()
