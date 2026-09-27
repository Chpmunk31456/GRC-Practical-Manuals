import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import review_evidence_status as evidence
import review_readiness_packets as readiness


class Phase7IntegrationTests(unittest.TestCase):
    def test_candidate_packets_remain_non_authorizing(self):
        result = readiness.run()
        self.assertGreater(result["candidate_count"], 0)
        self.assertFalse(result["publication_authorized"])
        for packet in result["packets"]:
            self.assertFalse(packet["publication_authorized"])
            self.assertEqual(packet["readiness_status"], "REVIEW_REQUIRED")

    def test_evidence_status_never_converts_freshness_into_approval(self):
        result = evidence.run()
        self.assertFalse(result["publication_authorized"])
        for manual in result["manuals"]:
            self.assertFalse(manual["publication_authorized"])
            self.assertEqual(manual["readiness_status"], "REVIEW_REQUIRED")
            self.assertIn(manual["evidence_status"], {"INCOMPLETE", "STALE", "CURRENT"})

    def test_phase7_manifest_records_closed_scope(self):
        manifest = json.loads((ROOT / "config/writing_system_manifest.json").read_text(encoding="utf-8"))
        phase7 = manifest["phase7"]
        self.assertEqual(phase7["completed_improvements"], [46, 47, 48])
        self.assertTrue(phase7["review_readiness_operationalization"])
        self.assertTrue(phase7["exact_revision_packets"])
        self.assertTrue(phase7["stale_incomplete_evidence_visibility"])
        self.assertTrue(phase7["approval_inference_prohibited"])
        self.assertFalse(phase7["publication_authorized_by_phase7_automation"])
        self.assertEqual(
            phase7["acceptance_record"],
            "qa/PHASE7_INTEGRATION_ACCEPTANCE_2026-09-27.md",
        )

    def test_acceptance_record_preserves_human_boundaries(self):
        text = (ROOT / "qa/PHASE7_INTEGRATION_ACCEPTANCE_2026-09-27.md").read_text(encoding="utf-8")
        for phrase in (
            "does not approve publication",
            "CURRENT is metadata freshness only",
            "production-toolchain verification",
            "controlled release verification",
        ):
            self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
