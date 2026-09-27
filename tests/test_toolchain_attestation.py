from pathlib import Path
import sys
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import toolchain_attestation as attestation


class ToolchainAttestationTests(unittest.TestCase):
    def setUp(self):
        self.config = {
            "python": "3.12.14",
            "pdf_toolchain": {
                "poppler_package_version": "22.12.0-2+deb12u3",
                "pdftotext_version": "pdftotext version 22.12.0",
                "pdfinfo_version": "pdfinfo version 22.12.0",
            },
            "hosted_ci_attestation": {
                "runner_image_version": "20260920.314.1",
                "poppler_package_version": "24.02.0-1ubuntu9.9",
                "pdftotext_version": "pdftotext version 24.02.0",
                "pdfinfo_version": "pdfinfo version 24.02.0",
            },
        }
        self.observed = {
            "python": "3.12.14",
            "runner_image_version": "20260920.314.1",
            "poppler_package_version": "24.02.0-1ubuntu9.9",
            "pdftotext_version": "pdftotext version 24.02.0",
            "pdfinfo_version": "pdfinfo version 24.02.0",
        }

    def test_exact_baseline_passes(self):
        self.assertEqual(attestation.verify(self.config, self.observed), [])

    def test_runner_image_drift_is_visible(self):
        changed = dict(self.observed, runner_image_version="newer")
        self.assertIn("runner_image_version_drift", attestation.verify(self.config, changed))

    def test_poppler_drift_is_visible(self):
        changed = dict(self.observed, poppler_package_version="different")
        self.assertIn("poppler_package_version_mismatch", attestation.verify(self.config, changed))

    def test_attestation_never_claims_publication_authority(self):
        fake = dict(self.observed)
        fake["validation_environment"] = "ubuntu-24.04"
        fake["runner_image"] = "ubuntu24"
        with mock.patch.object(attestation, "probe", return_value=fake):
            with mock.patch.object(attestation, "read_json", return_value={
                **self.config,
                "status": "REVIEW_REQUIRED",
            }):
                result = attestation.run()
        self.assertEqual(result["status"], "PASS")
        self.assertFalse(result["immutable_production_environment"])
        self.assertFalse(result["publication_authorized"])
        self.assertEqual(result["production_status"], "REVIEW_REQUIRED")


if __name__ == "__main__":
    unittest.main()
