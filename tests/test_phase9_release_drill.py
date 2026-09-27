from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import phase9_release_drill as drill
import review_readiness_packets


class Phase9ReleaseDrillTests(unittest.TestCase):
    def test_artifact_fingerprints_are_stable(self):
        packets = review_readiness_packets.run()["packets"]
        first = [drill.artifact_fingerprint(p) for p in packets]
        second = [drill.artifact_fingerprint(p) for p in packets]
        self.assertEqual(first, second)
        self.assertTrue(all(len(value) == 64 for value in first))

    def test_successful_recovery_yields_technical_ready_human_blocked(self):
        result = drill.run(recovery_report={"status": "PASS"})
        self.assertEqual(result["status"], "TECHNICAL_READY_HUMAN_APPROVALS_REQUIRED")
        self.assertTrue(all(result["technical_controls"].values()))
        self.assertEqual(len(result["candidate_artifact_fingerprints"]), 6)
        self.assertEqual(result["rollout_changes_applied"], 0)
        self.assertFalse(result["publication_performed"])
        self.assertFalse(result["publication_authorized"])

    def test_missing_recovery_fails_closed(self):
        result = drill.run(recovery_report={"status": "NOT_SUPPLIED"})
        self.assertEqual(result["status"], "TECHNICAL_PREREQUISITE_INCOMPLETE")
        self.assertFalse(result["technical_controls"]["isolated_recovery_pass"])
        self.assertFalse(result["publication_authorized"])

    def test_every_candidate_remains_non_authorizing(self):
        result = drill.run(recovery_report={"status": "PASS"})
        self.assertEqual(len(result["candidate_queue"]), 6)
        for row in result["candidate_queue"]:
            self.assertFalse(row["publication_authorized"])
            self.assertEqual(row["status"], "BLOCKED")
            self.assertTrue(row["blockers"])


if __name__ == "__main__":
    unittest.main()
