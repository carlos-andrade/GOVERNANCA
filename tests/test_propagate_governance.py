import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from automation import propagar_governanca as sync

class TestPropagarGovernancaRegistry(unittest.TestCase):
    def test_registo_canonico_valido_e_descoberta_deterministica(self):
        data = sync.load_registry()
        self.assertEqual(data["policy"], "pull_request_only")
        self.assertTrue(data["repositories"])
        first = sync.discover_files(data)
        second = sync.discover_files(data)
        self.assertTrue(first)
        self.assertEqual(first, second)
        self.assertIn("CONSTITUICAO.md", first)
        self.assertTrue(any(path.startswith("standards/") for path in first))
        self.assertTrue(any(path.startswith("WATCHDOG/") for path in first))

    def test_bloqueia_politica_insegura(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "registry.json"
            data = {
                "schema_version": 1,
                "source_repository": "carlos-andrade/GOVERNANCA",
                "policy": "direct_push",
                "published_roots": sorted(sync.REQUIRED_ROOTS),
                "repositories": []
            }
            path.write_text(json.dumps(data), encoding="utf-8")
            with patch.object(sync, "REGISTRY", path):
                with self.assertRaises(ValueError):
                    sync.load_registry()

    def test_bloqueia_path_traversal(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "registry.json"
            data = {
                "schema_version": 1,
                "source_repository": "carlos-andrade/GOVERNANCA",
                "policy": "pull_request_only",
                "published_roots": ["../README.md"],
                "repositories": []
            }
            path.write_text(json.dumps(data), encoding="utf-8")
            with patch.object(sync, "REGISTRY", path):
                with self.assertRaises(ValueError):
                    sync.load_registry()

if __name__ == "__main__":
    unittest.main()
