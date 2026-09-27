import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import review_evidence_validation as validation
import review_readiness_packets as readiness
from controlled_publication_qa import sha256


class ExactReviewEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.packet_report = readiness.run()
        self.packet = self.packet_report["packets"][0]
        self.policy = json.loads((ROOT / "config/review_readiness_policy.json").read_text(encoding="utf-8"))
        self.scopes = self.policy["required_scopes"][self.packet["manual_id"]]
        evidence_path = self.packet["review_records"][0]["path"]
        self.record = {
            "schema_version": 1,
            "manual_id": self.packet["manual_id"],
            "source_revision": self.packet["source_revision"],
            "packet_sha256": self.packet["packet_sha256"],
            "reviewer": "reviewer@example.test",
            "prepared_by": "producer@example.test",
            "decision": "APPROVED",
            "scopes": [self.scopes[0]],
            "artifacts": validation.flatten_artifacts(self.packet),
            "review_records": validation.flatten_review_records(self.packet),
            "evidence_files": {evidence_path: sha256(ROOT / evidence_path)},
            "reviewed_at": "2026-09-27T12:00:00+00:00",
        }

    def validate(self, record=None):
        return validation.validate_record(
            record or self.record,
            self.packet,
            self.scopes,
            self.policy,
            ROOT,
        )

    def test_exact_hash_bound_review_record_can_be_current(self):
        status, errors = self.validate()
        self.assertEqual(status, "CURRENT")
        self.assertEqual(errors, [])

    def test_stale_revision_and_packet_hash_fail_closed(self):
        record = dict(self.record, source_revision="a" * 40, packet_sha256="b" * 64)
        status, errors = self.validate(record)
        self.assertEqual(status, "STALE")
        self.assertIn("source_revision_stale", errors)
        self.assertIn("packet_hash_stale", errors)

    def test_changed_artifact_hashes_invalidate_review(self):
        record = dict(self.record)
        record["artifacts"] = dict(record["artifacts"])
        first = next(iter(record["artifacts"]))
        record["artifacts"][first] = "0" * 64
        status, errors = self.validate(record)
        self.assertEqual(status, "STALE")
        self.assertIn("artifact_hashes_stale", errors)

    def test_changed_review_record_hashes_invalidate_review(self):
        record = dict(self.record)
        record["review_records"] = dict(record["review_records"])
        first = next(iter(record["review_records"]))
        record["review_records"][first] = "0" * 64
        status, errors = self.validate(record)
        self.assertEqual(status, "STALE")
        self.assertIn("review_record_hashes_stale", errors)

    def test_self_review_is_invalid(self):
        record = dict(self.record, prepared_by=self.record["reviewer"])
        status, errors = self.validate(record)
        self.assertEqual(status, "INVALID")
        self.assertIn("independent_reviewer_required", errors)

    def test_unknown_scope_is_invalid(self):
        record = dict(self.record, scopes=["not_a_required_scope"])
        status, errors = self.validate(record)
        self.assertEqual(status, "INVALID")
        self.assertIn("scope_not_required", errors)

    def test_tampered_evidence_hash_is_invalid(self):
        record = dict(self.record, evidence_files={next(iter(self.record["evidence_files"])): "0" * 64})
        status, errors = self.validate(record)
        self.assertEqual(status, "INVALID")
        self.assertIn("evidence_file_hash_mismatch", errors)

    def test_empty_registry_stays_review_required(self):
        result = validation.run()
        self.assertEqual(result["status"], "REVIEW_REQUIRED")
        self.assertEqual(result["records"], [])
        self.assertFalse(result["publication_authorized"])
        self.assertTrue(all(row["status"] == "REVIEW_REQUIRED" for row in result["manuals"]))

    def test_policy_covers_every_candidate_exactly(self):
        packets = {p["manual_id"] for p in self.packet_report["packets"]}
        self.assertEqual(set(self.policy["required_scopes"]), packets)


if __name__ == "__main__":
    unittest.main()
