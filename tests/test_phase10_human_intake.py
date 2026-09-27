from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import phase10_human_intake as intake


class Phase10HumanIntakeTests(unittest.TestCase):
    def test_empty_repository_queues_fail_closed(self):
        result = intake.run()
        self.assertEqual(
            result["reviewer_authorization"]["status"],
            "HUMAN_AUTHORIZATION_REQUIRED",
        )
        self.assertEqual(result["reviewer_authorization"]["current_authorized_count"], 0)
        self.assertEqual(result["reviewer_authorization"]["release_policy_mutations_applied"], 0)
        self.assertEqual(result["human_evidence"]["registry_mutations_applied"], 0)
        self.assertFalse(result["publication_authorized"])

    def test_reviewer_request_requires_human_evidence(self):
        policy = {
            "reviewer_authorization": {
                "required_fields": [
                    "reviewer_id", "authorized_by", "authorized_at",
                    "authorization_evidence_path", "authorization_evidence_sha256",
                ]
            }
        }
        result = intake.validate_reviewer_request({}, policy)
        self.assertEqual(result["status"], "INVALID")

    def test_valid_reviewer_request_remains_unapplied(self):
        policy = {
            "reviewer_authorization": {
                "required_fields": [
                    "reviewer_id", "authorized_by", "authorized_at",
                    "authorization_evidence_path", "authorization_evidence_sha256",
                ]
            }
        }
        with tempfile.TemporaryDirectory(dir=ROOT) as td:
            path = Path(td) / "authorization.txt"
            path.write_text("synthetic human authorization evidence", encoding="utf-8")
            record = {
                "reviewer_id": "reviewer-example",
                "authorized_by": "governance-owner",
                "authorized_at": "2026-09-27T18:00:00Z",
                "authorization_evidence_path": str(path.relative_to(ROOT)),
                "authorization_evidence_sha256": intake.sha256(path),
            }
            result = intake.validate_reviewer_request(record, policy)
        self.assertEqual(result["status"], "VALID_PROPOSAL")
        self.assertFalse(result["authorization_applied"])

    def test_stale_candidate_evidence_is_rejected(self):
        policy = {
            "human_evidence_submission": {
                "required_fields": [
                    "manual_id", "decision_type", "decision", "reviewer_id",
                    "packet_sha256", "evidence_path", "evidence_sha256", "reviewed_at",
                ]
            }
        }
        packets = {
            "packets": [{
                "manual_id": "manual-example",
                "packet_sha256": "a" * 64,
            }]
        }
        record = {
            "manual_id": "manual-example",
            "decision_type": "accessibility",
            "decision": "APPROVED",
            "reviewer_id": "reviewer-example",
            "packet_sha256": "b" * 64,
            "evidence_path": "does-not-matter",
            "evidence_sha256": "c" * 64,
            "reviewed_at": "2026-09-27T18:00:00Z",
        }
        result = intake.validate_evidence_submission(record, policy, packets)
        self.assertEqual(result["status"], "STALE")
        self.assertEqual(result["reason"], "packet_hash_mismatch")

    def test_valid_evidence_submission_remains_unapplied(self):
        policy = {
            "human_evidence_submission": {
                "required_fields": [
                    "manual_id", "decision_type", "decision", "reviewer_id",
                    "packet_sha256", "evidence_path", "evidence_sha256", "reviewed_at",
                ]
            }
        }
        packets = {
            "packets": [{
                "manual_id": "manual-example",
                "packet_sha256": "a" * 64,
            }]
        }
        with tempfile.TemporaryDirectory(dir=ROOT) as td:
            path = Path(td) / "review.txt"
            path.write_text("synthetic human review evidence", encoding="utf-8")
            record = {
                "manual_id": "manual-example",
                "decision_type": "accessibility",
                "decision": "APPROVED",
                "reviewer_id": "reviewer-example",
                "packet_sha256": "a" * 64,
                "evidence_path": str(path.relative_to(ROOT)),
                "evidence_sha256": intake.sha256(path),
                "reviewed_at": "2026-09-27T18:00:00Z",
            }
            result = intake.validate_evidence_submission(record, policy, packets)
        self.assertEqual(result["status"], "VALID_PROPOSAL")
        self.assertFalse(result["evidence_applied"])


if __name__ == "__main__":
    unittest.main()
