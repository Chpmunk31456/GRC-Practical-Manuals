import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import pdf_execution_closure as closure


class PDFExecutionClosureTests(unittest.TestCase):
    def test_order_does_not_change_digest(self):
        with tempfile.TemporaryDirectory() as td:
            a = Path(td) / "a.txt"
            b = Path(td) / "b.txt"
            h1 = "1" * 64
            h2 = "2" * 64
            a.write_text(f"{h1} /usr/bin/pdfinfo\n{h2} /usr/bin/pdftotext\n", encoding="utf-8")
            b.write_text(f"{h2} /usr/bin/pdftotext\n{h1} /usr/bin/pdfinfo\n", encoding="utf-8")
            self.assertEqual(closure.digest_inventory(a), closure.digest_inventory(b))

    def test_file_hash_change_changes_digest(self):
        with tempfile.TemporaryDirectory() as td:
            a = Path(td) / "a.txt"
            b = Path(td) / "b.txt"
            a.write_text(f"{'1'*64} /usr/bin/pdfinfo\n", encoding="utf-8")
            b.write_text(f"{'2'*64} /usr/bin/pdfinfo\n", encoding="utf-8")
            self.assertNotEqual(closure.digest_inventory(a), closure.digest_inventory(b))

    def test_relative_paths_fail_closed(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "bad.txt"
            p.write_text(f"{'1'*64} usr/bin/pdfinfo\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                closure.digest_inventory(p)


if __name__ == "__main__":
    unittest.main()
