import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import controlled_publication_qa as controlled
import repository_publication_qa as repository
import publication_roundtrip_qa as roundtrip


class Phase6OnboardingTests(unittest.TestCase):
    def setUp(self):
        self.index = json.loads((ROOT / "config/controlled_publications/index.json").read_text(encoding="utf-8"))
        self.path = ROOT / "config/controlled_publications/manual09.json"
        self.manifest = json.loads(self.path.read_text(encoding="utf-8"))

    def test_manual09_is_candidate_not_active(self):
        relative = "config/controlled_publications/manual09.json"
        self.assertIn(relative, self.index["candidate_manifests"])
        self.assertNotIn(relative, self.index["manifests"])
        self.assertEqual(
            self.manifest["readiness_status"],
            "candidate-blocked-human-localization-accessibility-review",
        )

    def test_manual09_removed_from_next_candidate_queue(self):
        self.assertNotIn(
            "01-foundations/NIST_CSF_2_Controlled_Implementation",
            self.index["next_candidates"],
        )

    def test_manual09_all_locales_have_32_chapters(self):
        root = ROOT / self.manifest["manual_root"]
        for locale, cfg in self.manifest["languages"].items():
            sources = controlled.collect(root, cfg["source_globs"])
            text = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in sources)
            with self.subTest(locale=locale):
                self.assertEqual(
                    controlled.chapter_numbers(text, cfg["chapter_heading_pattern"]),
                    list(range(1, 33)),
                )

    def test_manual09_retains_fail_closed_human_review_records(self):
        root = ROOT / self.manifest["manual_root"]
        for record in self.manifest["review_records"]:
            text = (root / record["path"]).read_text(encoding="utf-8").casefold()
            with self.subTest(path=record["path"]):
                self.assertIn("fail-closed", text)

    def test_repository_discovery_reports_manual09_as_candidate(self):
        manifests, _ = repository.discover()
        match = next(m for _, m in manifests if m["manual_id"] == "manual09-nist-csf-2")
        self.assertEqual(match["rollout_lane"], "candidate")


class Phase6Manual10OnboardingTests(unittest.TestCase):
    def setUp(self):
        self.index = json.loads((ROOT / "config/controlled_publications/index.json").read_text(encoding="utf-8"))
        self.path = ROOT / "config/controlled_publications/manual10.json"
        self.manifest = json.loads(self.path.read_text(encoding="utf-8"))

    def test_manual10_is_candidate_not_active(self):
        relative = "config/controlled_publications/manual10.json"
        self.assertIn(relative, self.index["candidate_manifests"])
        self.assertNotIn(relative, self.index["manifests"])
        self.assertEqual(
            self.manifest["readiness_status"],
            "candidate-blocked-human-localization-accessibility-release-review",
        )

    def test_manual10_removed_from_next_candidate_queue(self):
        self.assertNotIn(
            "01-foundations/NIST_RMF_SP_800-53_Controlled_Implementation",
            self.index["next_candidates"],
        )

    def test_manual10_all_locales_have_32_chapters(self):
        root = ROOT / self.manifest["manual_root"]
        for locale, cfg in self.manifest["languages"].items():
            sources = controlled.collect(root, cfg["source_globs"])
            text = "\\n".join(p.read_text(encoding="utf-8", errors="replace") for p in sources)
            with self.subTest(locale=locale):
                self.assertEqual(
                    controlled.chapter_numbers(text, cfg["chapter_heading_pattern"]),
                    list(range(1, 33)),
                )

    def test_manual10_retains_fail_closed_human_review_records(self):
        root = ROOT / self.manifest["manual_root"]
        for record in self.manifest["review_records"]:
            text = (root / record["path"]).read_text(encoding="utf-8").casefold()
            with self.subTest(path=record["path"]):
                self.assertIn("fail-closed", text)

    def test_manual10_follows_manual09_in_candidate_sequence(self):
        candidates = self.index["candidate_manifests"]
        self.assertLess(
            candidates.index("config/controlled_publications/manual09.json"),
            candidates.index("config/controlled_publications/manual10.json"),
        )

    def test_repository_discovery_reports_manual10_as_candidate(self):
        manifests, _ = repository.discover()
        match = next(m for _, m in manifests if m["manual_id"] == "manual10-nist-rmf-sp-800-53")
        self.assertEqual(match["rollout_lane"], "candidate")


class Phase6Manual05OnboardingTests(unittest.TestCase):
    def setUp(self):
        self.index = json.loads((ROOT / "config/controlled_publications/index.json").read_text(encoding="utf-8"))
        self.path = ROOT / "config/controlled_publications/manual05.json"
        self.manifest = json.loads(self.path.read_text(encoding="utf-8"))

    def test_manual05_is_candidate_not_active(self):
        relative = "config/controlled_publications/manual05.json"
        self.assertIn(relative, self.index["candidate_manifests"])
        self.assertNotIn(relative, self.index["manifests"])
        self.assertEqual(
            self.manifest["readiness_status"],
            "candidate-blocked-substantive-human-localization-accessibility-review",
        )

    def test_manual05_removed_from_next_candidate_queue(self):
        self.assertNotIn(
            "03-assurance-and-audit/AI_Auditing_and_Assurance",
            self.index["next_candidates"],
        )

    def test_manual05_all_locales_have_32_chapters(self):
        root = ROOT / self.manifest["manual_root"]
        for locale, cfg in self.manifest["languages"].items():
            sources = controlled.collect(root, cfg["source_globs"])
            text = "\\n".join(p.read_text(encoding="utf-8", errors="replace") for p in sources)
            with self.subTest(locale=locale):
                self.assertEqual(
                    controlled.chapter_numbers(text, cfg["chapter_heading_pattern"]),
                    list(range(1, 33)),
                )

    def test_manual05_retains_substantive_human_review_blocks(self):
        root = ROOT / self.manifest["manual_root"]
        localization = (root / "qa/LOCALIZATION_SEMANTIC_REVIEW_GATE.md").read_text(encoding="utf-8").casefold()
        accessibility = (root / "qa/DOCUMENT_ACCESSIBILITY_PUBLICATION_QA_GATE.md").read_text(encoding="utf-8").casefold()
        packet = (root / "qa/HUMAN_REVIEW_PACKET_2026-08-29.md").read_text(encoding="utf-8").casefold()
        self.assertIn("fail-closed", localization)
        self.assertIn("fail-closed", accessibility)
        self.assertIn("does not itself make manual 05 publication-eligible", packet)

    def test_manual05_follows_manual10_in_candidate_sequence(self):
        candidates = self.index["candidate_manifests"]
        self.assertLess(
            candidates.index("config/controlled_publications/manual10.json"),
            candidates.index("config/controlled_publications/manual05.json"),
        )

    def test_repository_discovery_reports_manual05_as_candidate(self):
        manifests, _ = repository.discover()
        match = next(m for _, m in manifests if m["manual_id"] == "manual05-ai-auditing-assurance")
        self.assertEqual(match["rollout_lane"], "candidate")

    def test_manual05_roundtrip_gate_passes(self):
        result = roundtrip.run(self.manifest)
        self.assertEqual(result["status"], "PASS", json.dumps(result, indent=2))


if __name__ == "__main__":
    unittest.main()
