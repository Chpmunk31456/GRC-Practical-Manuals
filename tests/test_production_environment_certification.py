from pathlib import Path
import sys
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import production_environment_certification as cert


class ProductionEnvironmentCertificationTests(unittest.TestCase):
    def test_contract_is_digest_pinned_and_network_install_free(self):
        result = cert.validate_contract()
        self.assertEqual(result["contract_status"], "PASS")
        self.assertEqual(result["errors"], [])
        self.assertRegex(result["dependency_lock_sha256"], r"^[0-9a-f]{64}$")
        self.assertRegex(result["base_image_manifest_digest"], r"^sha256:[0-9a-f]{64}$")
        self.assertTrue(result["immutable_build_image_verified"])
        self.assertRegex(result["configured_build_container_digest"], r"^sha256:[0-9a-f]{64}$")

    def test_absent_runtime_remains_blocked_not_verified(self):
        with mock.patch.object(cert, "docker_available", return_value=False):
            result = cert.run()
        self.assertEqual(result["status"], "BLOCKED")
        self.assertTrue(result["immutable_build_image_verified"])
        self.assertFalse(result["immutable_pdf_toolchain_verified"])
        self.assertFalse(result["publication_authorized"])

    def test_runtime_presence_alone_does_not_verify_environment(self):
        with mock.patch.object(cert, "docker_available", return_value=True):
            result = cert.run()
        self.assertEqual(result["status"], "BLOCKED")
        self.assertEqual(result["reason"], "immutable_pdf_toolchain_digest_evidence_required")
        self.assertTrue(result["immutable_build_image_verified"])
        self.assertFalse(result["publication_authorized"])

    def test_phase9_never_infers_pdf_toolchain_verification(self):
        with mock.patch.object(cert, "docker_available", return_value=True):
            result = cert.run()
        self.assertFalse(result["immutable_pdf_toolchain_verified"])


if __name__ == "__main__":
    unittest.main()
