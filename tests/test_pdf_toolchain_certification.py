from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import pdf_toolchain_certification as cert


class PDFToolchainCertificationTests(unittest.TestCase):
    def test_lock_is_exact_and_non_authorizing(self):
        result = cert.run()
        self.assertEqual(result["errors"], [])
        self.assertRegex(result["pdf_lock_sha256"], r"^[0-9a-f]{64}$")
        self.assertFalse(result["publication_authorized"])

    def test_unpinned_pdf_digest_is_not_verified(self):
        result = cert.run()
        if result["container_digest"] is None:
            self.assertEqual(result["status"], "BLOCKED")
            self.assertFalse(result["immutable_pdf_toolchain_verified"])


if __name__ == "__main__":
    unittest.main()
