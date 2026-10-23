import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from automation import propagar_governanca as sync

class TestPropagarGovernancaRegistry(unittest.TestCase):
    def test_idempotencia_reutiliza_arvore_remota_inalterada(self):
        # A árvore calculada deve ser comparada com a branch remota antes de criar
        # um novo commit; igualdade significa não reescrever a branch nem fazer push.
        desired_tree = "tree-sha-123"
        remote_tree = "tree-sha-123"
        self.assertTrue(sync.same_tree(desired_tree, remote_tree))
        self.assertFalse(sync.same_tree(desired_tree, "tree-sha-456"))
        self.assertFalse(sync.same_tree("", remote_tree))
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

    def test_registo_canonico_mantem_licitacao_desativado(self):
        data = sync.load_registry()
        targets = {item["name"].lower(): item["enabled"] for item in data["repositories"]}
        self.assertIn("carlos-andrade/licitacao", targets)
        self.assertFalse(
            targets["carlos-andrade/licitacao"],
            "LICITACAO deve permanecer desativado até reconciliação e aceitação individual."
        )

    def test_selecao_normal_exclui_destinos_desativados(self):
        data = {
            "repositories": [
                {"name": "carlos-andrade/B3", "enabled": True},
                {"name": "carlos-andrade/LICITACAO", "enabled": False},
            ]
        }
        self.assertEqual([r["name"] for r in sync.select_targets(data)], ["carlos-andrade/B3"])
        with self.assertRaisesRegex(ValueError, "não registado/ativo"):
            sync.select_targets(data, "carlos-andrade/LICITACAO")

    def test_teste_desativado_exige_destino_explicito_e_unico(self):
        data = {
            "repositories": [
                {"name": "carlos-andrade/B3", "enabled": True},
                {"name": "carlos-andrade/LICITACAO", "enabled": False},
            ]
        }
        with self.assertRaisesRegex(ValueError, "exige --repo"):
            sync.select_targets(data, allow_disabled_test=True)
        selected = sync.select_targets(data, "carlos-andrade/LICITACAO", allow_disabled_test=True)
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0]["name"], "carlos-andrade/LICITACAO")
        with self.assertRaisesRegex(ValueError, "só pode selecionar"):
            sync.select_targets(data, "carlos-andrade/B3", allow_disabled_test=True)

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
            with patch.object(sync, "REGISTRY", path), patch.object(sync, "REQUIRED_ROOTS", {"../README.md"}):
                with self.assertRaises(ValueError):
                    sync.load_registry()

    def test_credencial_ausente_produz_erro_estruturado(self):
        with patch.object(sync, "load_registry", return_value={
            "repositories": [], "destination_root": ".governanca/upstream"
        }), patch.object(sync, "discover_files", return_value=["CONSTITUICAO.md"]), \
             patch.object(sync, "select_targets", return_value=[]), \
             patch.dict("os.environ", {"GH_TOKEN": "", "GITHUB_TOKEN": ""}), patch("sys.argv", ["test_propagate_governance.py"]):
            with patch("builtins.print") as output:
                code = sync.main()
            self.assertEqual(code, 2)
            payload = json.loads(output.call_args.args[0])
            self.assertEqual(payload["code"], "TOKEN_MISSING")

    def test_credencial_invalida_produz_erro_estruturado_sem_expor_token(self):
        with patch.object(sync, "load_registry", return_value={
            "repositories": [], "destination_root": ".governanca/upstream"
        }), patch.object(sync, "discover_files", return_value=["CONSTITUICAO.md"]), \
             patch.object(sync, "select_targets", return_value=[]), \
             patch.dict("os.environ", {"GH_TOKEN": "fake-test-token", "GITHUB_TOKEN": ""}), \
             patch("sys.argv", ["test_propagate_governance.py"]), patch.object(sync, "run", return_value=type("Result", (), {
                 "returncode": 1, "stdout": "", "stderr": "token fake-test-token rejected"
             })()):
            with patch("builtins.print") as output:
                code = sync.main()
            self.assertEqual(code, 2)
            payload = json.loads(output.call_args.args[0])
            self.assertEqual(payload["code"], "TOKEN_REJECTED")
            self.assertNotIn("fake-test-token", payload["detail"])

if __name__ == "__main__":
    unittest.main()
