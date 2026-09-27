from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import phase10_source_review_packets as packets


class Phase10SourceReviewPacketTests(unittest.TestCase):
    def test_repository_source_backlog_is_visible(self):
        result = packets.run()
        self.assertGreater(result["source_count"], 0)
        self.assertGreater(result["review_required_count"], 0)
        self.assertEqual(result["baseline_updates_applied"], 0)
        self.assertFalse(result["publication_authorized"])

    def test_empty_baselines_are_never_inferred(self):
        result = packets.run()
        self.assertTrue(any(
            "approved_baseline_missing" in row["blockers"]
            for row in result["packets"]
        ))
        for row in result["packets"]:
            if "approved_baseline_missing" in row["blockers"]:
                self.assertIsNone(row["current_baseline"])
                self.assertTrue(row["human_approval_required"])

    def test_missing_source_mappings_are_explicit(self):
        result = packets.run()
        self.assertTrue(any(
            "source_to_manual_mapping_missing" in row["blockers"]
            for row in result["packets"]
        ))

    def test_existing_mappings_are_preserved(self):
        result = packets.run()
        by_id = {row["source_id"]: row for row in result["packets"]}
        self.assertTrue(by_id["nist-ai-rmf-1-0"]["affected_manuals"])
        self.assertTrue(by_id["nist-ai-600-1"]["affected_manuals"])

    def test_packets_never_mutate_baselines(self):
        result = packets.run()
        self.assertEqual(result["baseline_updates_applied"], 0)
        self.assertTrue(all(row["automation_may_update_baseline"] is False for row in result["packets"]))


if __name__ == "__main__":
    unittest.main()
