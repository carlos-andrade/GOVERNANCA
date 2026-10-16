import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from automation import propagar_governanca as sync

class TestPropagarGovernancaRegistry(unittest.TestCase):
    def test_registo_canonico_valido(self):
        data = sync.load()
        self.assertEqual(data["policy"], "pull_request_only")
        self.assertTrue(data["repositories"])
        self.assertEqual(set(data["published_files"]), sync.REQUIRED)

    def test_bloqueia_politica_insegura(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "registry.json"
            data = {
                "schema_version": 1,
                "source_repository": "carlos-andrade/GOVERNANCA",
                "policy": "direct_push",
                "published_files": sorted(sync.REQUIRED),
                "repositories": []
            }
            path.write_text(json.dumps(data), encoding="utf-8")
            with patch.object(sync, "REGISTRY", path):
                with self.assertRaises(ValueError):
                    sync.load()

    def test_bloqueia_path_traversal(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "registry.json"
            data = {
                "schema_version": 1,
                "source_repository": "carlos-andrade/GOVERNANCA",
                "policy": "pull_request_only",
                "published_files": ["../README.md"],
                "repositories": []
            }
            path.write_text(json.dumps(data), encoding="utf-8")
            with patch.object(sync, "REGISTRY", path):
                with self.assertRaises(ValueError):
                    sync.load()

if __name__ == "__main__":
    unittest.main()
