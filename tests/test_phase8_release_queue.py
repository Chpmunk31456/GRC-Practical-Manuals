from pathlib import Path
import sys
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import phase8_release_queue as release_queue


class Phase8ReleaseQueueTests(unittest.TestCase):
    def test_repository_queue_is_fail_closed(self):
        result = release_queue.run()
        self.assertEqual(len(result["queue"]), 6)
        self.assertEqual(result["eligible_candidate_count"], 0)
        self.assertEqual(result["rollout_changes_applied"], 0)
        self.assertFalse(result["bulk_promotion_allowed"])
        self.assertFalse(result["publication_authorized"])
        for row in result["queue"]:
            self.assertEqual(row["status"], "BLOCKED")
            self.assertFalse(row["eligible_for_controlled_release_review"])
            self.assertFalse(row["rollout_change_permitted"])
            self.assertFalse(row["publication_authorized"])
            self.assertTrue(row["blockers"])

    def test_queue_never_bulk_promotes(self):
        result = release_queue.run()
        self.assertEqual(result["promotion_mode"], "one_candidate_at_a_time")
        self.assertFalse(result["bulk_promotion_allowed"])
        self.assertEqual(result["rollout_changes_applied"], 0)

    def test_eligible_state_still_does_not_authorize_publication(self):
        fake_status = {
            "source_revision": "a" * 40,
            "candidates": [{
                "manual_id": "manual-example",
                "packet_sha256": "b" * 64,
                "status": "READY_FOR_CONTROLLED_RELEASE_REVIEW",
                "decisions": [{
                    "decision_type": "accessibility",
                    "status": "CURRENT_APPROVED",
                    "reason": "exact_human_evidence_match",
                }],
            }],
            "global_requirements": [{
                "requirement": "immutable_production_toolchain",
                "status": "COMPLETE",
                "reason": None,
            }],
        }
        fake_policy = {
            "required_candidate_state": "READY_FOR_CONTROLLED_RELEASE_REVIEW",
            "promotion_mode": "one_candidate_at_a_time",
            "bulk_promotion_allowed": False,
        }
        with mock.patch.object(release_queue.human_approval_evidence, "run", return_value=fake_status):
            with mock.patch.object(release_queue, "read_json", return_value=fake_policy):
                result = release_queue.run()
        self.assertEqual(result["eligible_candidate_count"], 1)
        self.assertTrue(result["queue"][0]["eligible_for_controlled_release_review"])
        self.assertFalse(result["queue"][0]["rollout_change_permitted"])
        self.assertFalse(result["queue"][0]["publication_authorized"])
        self.assertFalse(result["publication_authorized"])


if __name__ == "__main__":
    unittest.main()
