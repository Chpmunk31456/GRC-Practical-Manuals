from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import phase8_human_handoff as handoff


class Phase8HumanHandoffTests(unittest.TestCase):
    def test_handoff_is_non_authorizing(self):
        result = handoff.run()
        self.assertFalse(result["publication_authorized"])
        self.assertEqual(result["automation_completed_human_actions"], 0)
        for candidate in result["candidate_requests"]:
            self.assertFalse(candidate["publication_authorized"])

    def test_source_baseline_backlog_is_visible(self):
        result = handoff.run()
        self.assertGreater(result["authoritative_source_request_count"], 0)
        self.assertTrue(any(
            "approved_baseline" in row["missing"]
            for row in result["authoritative_source_requests"]
        ))

    def test_reviewer_authorization_backlog_is_visible(self):
        result = handoff.run()
        reviewer = result["release_reviewer_authorization"]
        self.assertEqual(reviewer["status"], "HUMAN_AUTHORIZATION_REQUIRED")
        self.assertGreaterEqual(reviewer["minimum_independent_reviewers"], 2)

    def test_immutable_toolchain_backlog_is_visible(self):
        result = handoff.run()
        self.assertIn("status=VERIFIED", result["production_toolchain"]["missing"])
        self.assertIn("pdf_toolchain.container_digest", result["production_toolchain"]["missing"])
        self.assertNotIn("build_environment.container_digest", result["production_toolchain"]["missing"])

    def test_all_six_candidates_have_handoff_rows(self):
        result = handoff.run()
        self.assertEqual(len(result["candidate_requests"]), 6)
        self.assertTrue(all(row["required_human_actions"] for row in result["candidate_requests"]))


if __name__ == "__main__":
    unittest.main()
