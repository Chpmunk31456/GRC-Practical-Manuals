"""Repository rollout regressions; synthetic gate results are not approval evidence."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repository_publication_qa as rollout


class RepositoryPublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.config = self.root / "config/controlled_publications"
        self.config.mkdir(parents=True)
        (self.root / ".compliance").mkdir()
        manifests, _ = rollout.discover()
        self.manifests = []
        catalog = []
        for path, manifest in manifests:
            (self.root / manifest["manual_root"]).mkdir(parents=True)
            self.write(self.config / path.name, manifest)
            self.manifests.append("config/controlled_publications/" + path.name)
            catalog.append({"id": manifest["manual_id"], "path": manifest["manual_root"]})
        self.write(self.root / ".compliance/manual-catalog.json", {"manuals": catalog})
        self.write(self.config / "index.json", {"schema_version": 1, "manifests": self.manifests})

    def write(self, path, data):
        path.write_text(json.dumps(data), encoding="utf-8")

    def mutate_manifest(self, mutate):
        path = self.root / self.manifests[0]
        data = rollout.read_json(path)
        mutate(data)
        self.write(path, data)

    def test_real_catalog_includes_both_reference_manuals(self):
        manifests, inventory = rollout.discover()
        self.assertGreaterEqual(len(manifests), 2)
        self.assertIn("manual03-nist-ai-rmf", {m["manual_id"] for _, m in manifests})
        self.assertIn("manual04-nist-ai-600-1", {m["manual_id"] for _, m in manifests})
        self.assertTrue(any(x["rollout"] == "onboarding_required" for x in inventory))

    def test_each_manual_runs_all_gates(self):
        with patch.object(rollout, "execute_gate", return_value={"status": "PASS"}) as gate:
            result = rollout.run(self.root)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(gate.call_count, len(self.manifests) * len(rollout.GATES))
        self.assertEqual(result["human_publication_approval"], "NOT_EVALUATED")
        for item in result["results"]:
            self.assertEqual(set(item["gates"]), set(rollout.GATES))

    def test_new_registered_manual_runs_without_code_changes(self):
        data = rollout.read_json(self.root / self.manifests[0])
        data["manual_id"] = "test-additional-manual"
        data["manual_root"] = "01-foundations/Test"
        (self.root / data["manual_root"]).mkdir()
        self.write(self.config / "additional.json", data)
        index = rollout.read_json(self.config / "index.json")
        index["manifests"].append("config/controlled_publications/additional.json")
        self.write(self.config / "index.json", index)
        path = self.root / ".compliance/manual-catalog.json"
        catalog = rollout.read_json(path)
        catalog["manuals"].append({"id": data["manual_id"], "path": data["manual_root"]})
        self.write(path, catalog)
        with patch.object(rollout, "execute_gate", return_value={"status": "PASS"}) as gate:
            result = rollout.run(self.root)
        self.assertEqual(len(result["results"]), 3)
        self.assertEqual(gate.call_count, 12)

    def test_failure_never_skips_remaining_gates(self):
        with patch.object(rollout, "execute_gate", return_value={"status": "FAIL"}) as gate:
            result = rollout.run(self.root)
        self.assertEqual(result["status"], "FAIL")
        self.assertEqual(gate.call_count, 8)

    def test_execution_errors_fail_closed_without_prose_logging(self):
        with patch.object(rollout, "execute_gate", side_effect=RuntimeError("PRIVATE SAMPLE")):
            result = rollout.run(self.root)
        self.assertEqual(result["status"], "FAIL")
        self.assertNotIn("PRIVATE SAMPLE", json.dumps(result))
        self.assertEqual(result["results"][0]["gates"]["layout"]["error_type"], "RuntimeError")

    def test_candidate_lane_stays_explicit(self):
        self.write(self.config / "index.json", {"schema_version": 1,
                   "manifests": self.manifests[:1], "candidate_manifests": self.manifests[1:]})
        with patch.object(rollout, "execute_gate", return_value={"status": "PASS"}):
            result = rollout.run(self.root)
        self.assertEqual(result["results"][1]["rollout_lane"], "candidate")
        self.assertEqual(result["human_publication_approval"], "NOT_EVALUATED")

    def test_missing_status_is_failure(self):
        with patch.object(rollout, "execute_gate", return_value={}):
            self.assertEqual(rollout.run(self.root)["status"], "FAIL")

    def test_disabled_control_is_rejected(self):
        self.mutate_manifest(lambda m: m["release_controls"].update(require_roundtrip=False))
        with self.assertRaises(ValueError):
            rollout.discover(self.root)

    def test_missing_locale_is_rejected(self):
        self.mutate_manifest(lambda m: m["languages"].pop("pt-BR"))
        with self.assertRaises(ValueError):
            rollout.discover(self.root)

    def test_missing_review_records_are_rejected(self):
        self.mutate_manifest(lambda m: m.update(review_records=[]))
        with self.assertRaises(ValueError):
            rollout.discover(self.root)

    def test_path_escape_and_absolute_paths_are_rejected(self):
        for name in ("../outside", "/outside", "C:/outside", "..\\outside"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                rollout.contained(self.root, name)

    def test_empty_index_is_rejected(self):
        self.write(self.config / "index.json", {"schema_version": 1, "manifests": []})
        with self.assertRaises(ValueError):
            rollout.discover(self.root)

    def test_unregistered_manifest_is_rejected(self):
        self.write(self.config / "forgotten.json", {})
        with self.assertRaises(ValueError):
            rollout.discover(self.root)

    def test_duplicate_registration_is_rejected(self):
        self.write(self.config / "index.json", {"schema_version": 1, "manifests": self.manifests * 2})
        with self.assertRaises(ValueError):
            rollout.discover(self.root)

    def test_duplicate_json_keys_are_rejected(self):
        path = self.config / "index.json"
        path.write_text('{"schema_version":1,"schema_version":2}', encoding="utf-8")
        with self.assertRaises(ValueError):
            rollout.read_json(path)

    def test_unknown_catalog_manual_is_rejected(self):
        self.write(self.root / ".compliance/manual-catalog.json", {"manuals": []})
        with self.assertRaises(ValueError):
            rollout.discover(self.root)


if __name__ == "__main__":
    unittest.main()
