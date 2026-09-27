from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import pdf_toolchain_certification as cert


class PdfToolchainCertificationTests(unittest.TestCase):
    def test_pdf_contract_is_valid(self):
        result = cert.validate()
        self.assertEqual(result["contract_status"], "PASS")
        self.assertEqual(result["errors"], [])
        self.assertRegex(result["dependency_lock_sha256"], r"^[0-9a-f]{64}$")

    def test_unpinned_digest_remains_unverified(self):
        result = cert.validate()
        if result["configured_pdf_container_digest"] is None:
            self.assertFalse(result["immutable_pdf_toolchain_verified"])
        self.assertFalse(result["publication_authorized"])


if __name__ == "__main__":
    unittest.main()
