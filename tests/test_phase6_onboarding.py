import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import controlled_publication_qa as controlled
import repository_publication_qa as repository


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


if __name__ == "__main__":
    unittest.main()
