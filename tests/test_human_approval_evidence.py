from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import human_approval_evidence as evidence


class HumanApprovalEvidenceTests(unittest.TestCase):
    def test_repository_starts_fail_closed(self):
        result = evidence.run()
        self.assertEqual(result["status"], "HUMAN_OR_PRODUCTION_EVIDENCE_INCOMPLETE")
        self.assertFalse(result["publication_authorized"])
        self.assertEqual(len(result["candidates"]), 6)
        for candidate in result["candidates"]:
            self.assertIn(candidate["status"], {"HUMAN_REVIEW_INCOMPLETE", "HUMAN_REVIEW_REJECTED"})
            self.assertFalse(candidate["publication_authorized"])

    def test_requirements_are_explicit_for_every_candidate(self):
        requirements, _, _ = evidence.load_config()
        self.assertEqual(len(requirements["required_by_candidate"]), 6)
        for required in requirements["required_by_candidate"].values():
            self.assertIn("authoritative_source", required)
            self.assertIn("localization_semantic", required)
            self.assertIn("accessibility", required)
            self.assertIn("release_authorization", required)

    def test_hipaa_and_gdpr_require_legal_review(self):
        requirements, _, _ = evidence.load_config()
        self.assertIn("legal_semantic", requirements["required_by_candidate"]["manual06-hipaa-implementation-audit"])
        self.assertIn("privacy_legal", requirements["required_by_candidate"]["manual11-gdpr-controlled-implementation"])

    def test_missing_record_is_incomplete(self):
        packet = {"manual_id": "example", "packet_sha256": "a" * 64}
        status = evidence.current_records(packet, "accessibility", [], {"reviewers": [], "minimum_independent_reviewers": 2})
        self.assertEqual(status["status"], "INCOMPLETE")

    def test_release_authorization_requires_two_allowlisted_reviewers(self):
        packet = {"manual_id": "example", "packet_sha256": "a" * 64}
        status = evidence.current_records(packet, "release_authorization", [], {"reviewers": ["r1", "r2"], "minimum_independent_reviewers": 2})
        self.assertEqual(status["reason"], "human_evidence_missing")

    def test_automation_never_authorizes_publication(self):
        result = evidence.run()
        self.assertFalse(result["publication_authorized"])
        for candidate in result["candidates"]:
            self.assertFalse(candidate["publication_authorized"])


if __name__ == "__main__":
    unittest.main()
