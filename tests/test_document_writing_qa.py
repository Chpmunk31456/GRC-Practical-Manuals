import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from document_writing_qa import (  # noqa: E402
    detect_language,
    extract_markdown_blocks,
    is_local_endpoint,
    load_policy,
    local_findings,
)


class DocumentWritingQATests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.policy = load_policy(ROOT / "config" / "document_writing_policy.json")

    def test_detects_spanish_path(self):
        path = ROOT / "example" / "translations" / "es-419" / "source" / "chapter.md"
        self.assertEqual(detect_language(path, "# Capítulo", self.policy), "es")

    def test_detects_brazilian_portuguese_path(self):
        path = ROOT / "example" / "translations" / "pt-BR" / "source" / "chapter.md"
        self.assertEqual(detect_language(path, "# Capítulo", self.policy), "pt-BR")

    def test_detects_controlled_english_metadata(self):
        path = ROOT / "example" / "README.md"
        text = "**Controlled language:** English\n\n## Purpose"
        self.assertEqual(detect_language(path, text, self.policy), "en-US")

    def test_detects_mixed_language_index(self):
        path = ROOT / "README.md"
        text = "## English\nText\n## Español\nTexto\n## Português\nTexto"
        self.assertEqual(detect_language(path, text, self.policy), "mixed")

    def test_markdown_excludes_code_and_urls(self):
        text = """# Test

Use the [official source](https://example.com).

~~~python
print("do not lint this")
~~~
"""
        blocks = extract_markdown_blocks(text)
        joined = " ".join(block["text"] for block in blocks)
        self.assertIn("official source", joined)
        self.assertNotIn("https://example.com", joined)
        self.assertNotIn("print", joined)

    def test_duplicate_word_is_blocking(self):
        blocks = [{"text": "The control control owner reviews evidence.", "location": "line 1", "line": 1}]
        findings = local_findings(blocks, self.policy)
        self.assertTrue(
            any(item["code"] == "duplicate_word" and item["severity"] == "error" for item in findings)
        )

    def test_clear_technical_sentence_has_no_local_error(self):
        blocks = [{
            "text": "The control owner reviews evidence before approving the production change.",
            "location": "line 1",
            "line": 1,
        }]
        findings = local_findings(blocks, self.policy)
        self.assertFalse(any(item["severity"] == "error" for item in findings))

    def test_local_endpoint_detection(self):
        self.assertTrue(is_local_endpoint("http://127.0.0.1:8010/v2/check"))
        self.assertTrue(is_local_endpoint("http://localhost:8010/v2/check"))
        self.assertFalse(is_local_endpoint("https://api.languagetool.org/v2/check"))


if __name__ == "__main__":
    unittest.main()
