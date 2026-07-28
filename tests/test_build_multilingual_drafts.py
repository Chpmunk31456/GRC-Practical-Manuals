from __future__ import annotations

import importlib.util
import io
import sys
import tempfile
import types
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_multilingual_drafts.py"


class FakeTranslator:
    def __init__(self) -> None:
        self.chunks: list[str] = []

    def translate(self, text: str, source: str, target: str) -> str:
        self.chunks.append(text)
        return text


def load_script(translator: FakeTranslator):
    argos = types.ModuleType("argostranslate")
    translate_module = types.ModuleType("argostranslate.translate")
    translate_module.translate = translator.translate
    argos.translate = translate_module
    with mock.patch.dict(
        sys.modules,
        {"argostranslate": argos, "argostranslate.translate": translate_module},
    ):
        spec = importlib.util.spec_from_file_location("build_multilingual_drafts_tested", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        assert spec.loader
        spec.loader.exec_module(module)
    return module


class BuildMultilingualDraftsTests(unittest.TestCase):
    def test_chunking_preserves_protected_markdown_and_logs_progress(self) -> None:
        translator = FakeTranslator()
        module = load_script(translator)
        source = (
            "A long paragraph " * 20
            + "https://example.com/a [guide](https://example.com/guide) "
            + "`command --flag` GV.OC-1\n\n```bash\necho unchanged\n```\n"
        )
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            translated = module.translate_markdown(
                source,
                "es",
                "NOTICE",
                source_name="manual.md",
                max_chars=100,
            )

        self.assertTrue(all(len(chunk) <= 100 for chunk in translator.chunks))
        self.assertIn("https://example.com/a", translated)
        self.assertIn("](https://example.com/guide)", translated)
        self.assertIn("`command --flag`", translated)
        self.assertIn("GV.OC-1", translated)
        self.assertIn("```bash\necho unchanged\n```", translated)
        self.assertIn("source=manual.md target=es line=1/", stdout.getvalue())

    def test_existing_output_is_skipped_without_force(self) -> None:
        translator = FakeTranslator()
        module = load_script(translator)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_dir = root / "01-foundations" / "Example"
            source_dir.mkdir(parents=True)
            (source_dir / "English_Source_Example_v1.0.md").write_text("New source\n", encoding="utf-8")
            localized = source_dir / "Espanol"
            localized.mkdir()
            destination = localized / "Example_Espanol_v1.0.md"
            destination.write_text("Reviewed edition\n", encoding="utf-8")
            module.ROOT = root

            stdout = io.StringIO()
            with redirect_stdout(stdout):
                result = module.main(["--target", "es"])

            self.assertEqual(0, result)
            self.assertEqual("Reviewed edition\n", destination.read_text(encoding="utf-8"))
            self.assertEqual([], translator.chunks)
            self.assertIn("[skip] completed output exists", stdout.getvalue())

    def test_translation_error_identifies_exact_context(self) -> None:
        translator = FakeTranslator()

        def fail(*_args):
            raise ValueError("model error")

        translator.translate = fail
        module = load_script(translator)
        with self.assertRaisesRegex(
            RuntimeError,
            r"source=manual\.md target=pt line=1 chunk=1/1: model error",
        ):
            module.translate_markdown(
                "Translate me",
                "pt",
                "NOTICE",
                source_name="manual.md",
                max_chars=100,
            )


if __name__ == "__main__":
    unittest.main()
