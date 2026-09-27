from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import phase10_review_campaign as campaign


class Phase10ReviewCampaignTests(unittest.TestCase):
    def test_campaign_is_one_candidate_at_a_time(self):
        result = campaign.run()
        self.assertEqual(result["campaign_mode"], "one_candidate_at_a_time")
        self.assertEqual(result["candidate_count"], 6)

    def test_campaign_never_authors_or_authorizes(self):
        result = campaign.run()
        self.assertEqual(result["automation_authored_evidence_count"], 0)
        self.assertEqual(result["rollout_changes_applied"], 0)
        self.assertFalse(result["publication_authorized"])
        for row in result["campaign"]:
            self.assertFalse(row["publication_authorized"])

    def test_priority_is_deterministic(self):
        result = campaign.run()
        ordered = sorted(
            result["campaign"],
            key=lambda row: (row["unresolved_decision_count"], row["manual_id"]),
        )
        self.assertEqual([r["manual_id"] for r in result["campaign"]], [r["manual_id"] for r in ordered])
        self.assertEqual([r["campaign_priority"] for r in result["campaign"]], list(range(1, 7)))

    def test_every_unresolved_item_requires_human_action(self):
        result = campaign.run()
        self.assertTrue(all(row["unresolved_decisions"] for row in result["campaign"]))
        for row in result["campaign"]:
            for decision in row["unresolved_decisions"]:
                self.assertTrue(decision["human_action_required"])
                self.assertIn("reviewer_id", decision["required_evidence_fields"])
                self.assertIn("evidence_sha256", decision["required_evidence_fields"])

    def test_next_candidate_is_not_release_authorized(self):
        result = campaign.run()
        first = result["campaign"][0]
        self.assertEqual(result["next_candidate"], first["manual_id"])
        self.assertFalse(first["publication_authorized"])


if __name__ == "__main__":
    unittest.main()
