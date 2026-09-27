import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from manual03_end_to_end_qa import (  # noqa: E402
    chapter_numbers,
    check_docx,
    check_pdf,
    load_policy,
    run,
)


class Manual03EndToEndQATests(unittest.TestCase):
    def test_policy_targets_three_locales(self):
        policy = load_policy(ROOT / "config" / "manual03_e2e_policy.json")
        self.assertEqual(set(policy["languages"]), {"en", "es-419", "pt-BR"})
        self.assertEqual(policy["expected_chapters"], 32)

    def test_chapter_number_extraction_matches_manual_convention(self):
        text = "# 1. First chapter\n## 1.1 Detail\n# 2. Second chapter\n# 2. Duplicate"
        self.assertEqual(chapter_numbers(text, r"^#\s+(\d+)\."), [1, 2])

    def test_docx_integrity_rejects_invalid_zip(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.docx"
            path.write_bytes(b"not-a-docx")
            ok, _ = check_docx(path)
            self.assertFalse(ok)

    def test_docx_integrity_accepts_minimal_package(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "good.docx"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("[Content_Types].xml", "<Types/>")
                archive.writestr(
                    "word/document.xml",
                    '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                    "<w:body><w:p><w:r><w:t>Evidence</w:t></w:r></w:p></w:body></w:document>",
                )
            ok, _ = check_docx(path)
            self.assertTrue(ok)

    def test_pdf_signature(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.pdf"
            path.write_bytes(b"%PDF-1.7\n" + b"x" * 2048)
            ok, _ = check_pdf(path)
            self.assertTrue(ok)

    def test_current_manual03_package_has_complete_language_evidence(self):
        policy = load_policy(ROOT / "config" / "manual03_e2e_policy.json")
        result = run(policy)
        self.assertEqual(set(result["evidence"]["languages"]), {"en", "es-419", "pt-BR"})
        for locale in ("en", "es-419", "pt-BR"):
            self.assertEqual(result["evidence"]["languages"][locale]["chapter_count"], 32)
            self.assertTrue(result["evidence"]["languages"][locale]["required_terms_present"])

    def test_current_manual03_package_passes_end_to_end_gate(self):
        policy = load_policy(ROOT / "config" / "manual03_e2e_policy.json")
        result = run(policy)
        self.assertEqual(result["status"], "PASS", "\n".join(result["failures"]))


if __name__ == "__main__":
    unittest.main()
