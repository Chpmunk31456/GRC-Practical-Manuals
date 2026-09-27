import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import phase8_human_handoff as handoff
import phase8_release_queue as release_queue


class Phase8IntegrationTests(unittest.TestCase):
    def test_phase8_manifest_records_closed_scope(self):
        manifest = json.loads((ROOT / "config/writing_system_manifest.json").read_text(encoding="utf-8"))
        phase8 = manifest["phase8"]
        self.assertEqual(phase8["completed_improvements"], [49, 50, 51, 52, 53])
        self.assertTrue(phase8["production_approval_readiness"])
        self.assertTrue(phase8["hosted_ci_toolchain_attestation"])
        self.assertTrue(phase8["explicit_human_approval_requirements"])
        self.assertTrue(phase8["exact_human_evidence_binding"])
        self.assertTrue(phase8["one_candidate_at_a_time_release_queue"])
        self.assertTrue(phase8["deterministic_human_handoff"])
        self.assertTrue(phase8["human_approval_inference_prohibited"])
        self.assertFalse(phase8["publication_authorized_by_phase8_automation"])
        self.assertEqual(
            phase8["acceptance_record"],
            "qa/PHASE8_INTEGRATION_ACCEPTANCE_2026-09-27.md",
        )

    def test_release_queue_never_applies_rollout_changes(self):
        result = release_queue.run()
        self.assertEqual(result["rollout_changes_applied"], 0)
        self.assertFalse(result["bulk_promotion_allowed"])
        self.assertFalse(result["publication_authorized"])
        for row in result["queue"]:
            self.assertFalse(row["rollout_change_permitted"])
            self.assertFalse(row["publication_authorized"])

    def test_handoff_never_completes_human_actions(self):
        result = handoff.run()
        self.assertEqual(result["automation_completed_human_actions"], 0)
        self.assertFalse(result["publication_authorized"])

    def test_acceptance_record_preserves_external_approval_boundary(self):
        text = (ROOT / "qa/PHASE8_INTEGRATION_ACCEPTANCE_2026-09-27.md").read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        for phrase in (
            "does not approve publication",
            "implementation completion is not production approval",
            "authorized independent release-reviewer allowlist",
            "immutable production PDF/build environment digests",
            "exact-candidate controlled-release verification",
        ):
            self.assertIn(phrase, normalized)


if __name__ == "__main__":
    unittest.main()
