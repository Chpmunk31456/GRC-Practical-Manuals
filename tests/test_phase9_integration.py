import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import phase9_release_drill as drill
import production_environment_certification as environment
import pdf_toolchain_certification as pdf_cert


class Phase9IntegrationTests(unittest.TestCase):
    def test_phase9_manifest_records_closed_scope(self):
        manifest = json.loads((ROOT / "config/writing_system_manifest.json").read_text(encoding="utf-8"))
        phase9 = manifest["phase9"]
        self.assertEqual(phase9["completed_improvements"], [54, 55, 56, 57])
        self.assertTrue(phase9["production_certification"])
        self.assertTrue(phase9["immutable_build_image_verified"])
        self.assertTrue(phase9["immutable_pdf_toolchain_verified"])
        self.assertTrue(phase9["production_toolchain_verified"])
        self.assertTrue(phase9["controlled_release_drill"])
        self.assertTrue(phase9["candidate_artifact_fingerprints"])
        self.assertTrue(phase9["operational_handoff"])
        self.assertTrue(phase9["technical_phase_complete"])
        self.assertFalse(phase9["external_human_approval_prerequisites_complete"])
        self.assertFalse(phase9["publication_authorized_by_phase9_automation"])
        self.assertEqual(
            phase9["acceptance_record"],
            "qa/PHASE9_INTEGRATION_ACCEPTANCE_2026-09-27.md",
        )

    def test_production_environment_is_technically_verified_non_authorizing(self):
        result = environment.run()
        self.assertEqual(result["status"], "VERIFIED")
        self.assertTrue(result["immutable_build_image_verified"])
        self.assertTrue(result["immutable_pdf_toolchain_verified"])
        self.assertFalse(result["publication_authorized"])

    def test_pdf_toolchain_is_verified_non_authorizing(self):
        result = pdf_cert.validate()
        self.assertTrue(result["immutable_pdf_toolchain_verified"])
        self.assertFalse(result["publication_authorized"])

    def test_release_drill_remains_human_blocked(self):
        result = drill.run(recovery_report={"status": "PASS"})
        self.assertEqual(result["status"], "TECHNICAL_READY_HUMAN_APPROVALS_REQUIRED")
        self.assertEqual(result["rollout_changes_applied"], 0)
        self.assertFalse(result["publication_performed"])
        self.assertFalse(result["publication_authorized"])

    def test_acceptance_record_preserves_human_boundary(self):
        text = (ROOT / "qa/PHASE9_INTEGRATION_ACCEPTANCE_2026-09-27.md").read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        for phrase in (
            "does not approve any manual",
            "technical completion is not publication approval",
            "at least two authorized independent release reviewers",
            "exact-candidate controlled-release verification",
            "Bulk release remains prohibited",
        ):
            self.assertIn(phrase, normalized)


if __name__ == "__main__":
    unittest.main()
