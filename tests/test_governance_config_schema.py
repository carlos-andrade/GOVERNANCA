import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "governanca-config.schema.json"


class GovernanceConfigSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with SCHEMA_PATH.open(encoding="utf-8") as handle:
            cls.schema = json.load(handle)
        Draft202012Validator.check_schema(cls.schema)
        cls.validator = Draft202012Validator(cls.schema)

    def valid_config(self):
        return {
            "governanca": {
                "fonte": "carlos-andrade/GOVERNANCA",
                "modo": "diagnostico",
                "perfil": "automatico",
                "exigir_pull_request": True,
                "preservar_ficheiros_existentes": True,
                "auditoria": "obrigatoria",
            }
        }

    def test_canonical_config_is_valid(self):
        self.assertEqual(list(self.validator.iter_errors(self.valid_config())), [])

    def test_pinned_ref_is_optional_and_valid(self):
        config = self.valid_config()
        config["governanca"]["ref"] = "7003bd9848983c211aca588e68e5281a5babc39a"
        self.assertEqual(list(self.validator.iter_errors(config)), [])

    def test_alternative_source_is_rejected(self):
        config = self.valid_config()
        config["governanca"]["fonte"] = "someone/other-repo"
        self.assertTrue(list(self.validator.iter_errors(config)))

    def test_unknown_mode_is_rejected(self):
        config = self.valid_config()
        config["governanca"]["modo"] = "auto-merge"
        self.assertTrue(list(self.validator.iter_errors(config)))

    def test_direct_push_policy_cannot_be_disabled(self):
        config = self.valid_config()
        config["governanca"]["exigir_pull_request"] = False
        self.assertTrue(list(self.validator.iter_errors(config)))

    def test_existing_files_must_be_preserved(self):
        config = self.valid_config()
        config["governanca"]["preservar_ficheiros_existentes"] = False
        self.assertTrue(list(self.validator.iter_errors(config)))

    def test_audit_is_mandatory(self):
        config = self.valid_config()
        config["governanca"]["auditoria"] = "opcional"
        self.assertTrue(list(self.validator.iter_errors(config)))

    def test_unknown_properties_are_rejected(self):
        config = self.valid_config()
        config["governanca"]["token"] = "must-not-be-configured"
        self.assertTrue(list(self.validator.iter_errors(config)))

    def test_required_fields_are_enforced(self):
        config = self.valid_config()
        del config["governanca"]["auditoria"]
        self.assertTrue(list(self.validator.iter_errors(config)))


if __name__ == "__main__":
    unittest.main()
