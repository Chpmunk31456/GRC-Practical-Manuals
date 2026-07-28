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
    def make_source(self, root: Path, text: str = "New source\n") -> tuple[Path, Path]:
        source_dir = root / "01-foundations" / "Example"
        source_dir.mkdir(parents=True)
        source = source_dir / "English_Source_Example_v1.0.md"
        source.write_text(text, encoding="utf-8")
        destination = source_dir / "Espanol" / "Example_Espanol_v1.0.md"
        return source, destination

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

    def test_unchanged_source_with_valid_checkpoint_is_skipped(self) -> None:
        translator = FakeTranslator()
        module = load_script(translator)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            _, destination = self.make_source(root)
            module.ROOT = root
            self.assertEqual(0, module.main(["--target", "es"]))
            generated = destination.read_text(encoding="utf-8")
            translator.chunks.clear()

            stdout = io.StringIO()
            with redirect_stdout(stdout):
                result = module.main(["--target", "es", "--allow-protected-existing"])

            self.assertEqual(0, result)
            self.assertEqual(generated, destination.read_text(encoding="utf-8"))
            self.assertEqual([], translator.chunks)
            self.assertIn("[skip] valid checkpoint", stdout.getvalue())

    def test_changed_source_invalidates_checkpoint(self) -> None:
        translator = FakeTranslator()
        module = load_script(translator)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, destination = self.make_source(root)
            module.ROOT = root
            self.assertEqual(0, module.main(["--target", "es"]))
            generated = destination.read_text(encoding="utf-8")
            translator.chunks.clear()
            source.write_text("Changed English source\n", encoding="utf-8")

            stdout = io.StringIO()
            with redirect_stdout(stdout):
                result = module.main(["--target", "es", "--allow-protected-existing"])

            self.assertEqual(2, result)
            self.assertEqual(generated, destination.read_text(encoding="utf-8"))
            self.assertEqual([], translator.chunks)
            self.assertIn("[stale]", stdout.getvalue())
            self.assertIn("--refresh-generated", stdout.getvalue())
            self.assertIn("cannot be acknowledged as current", stdout.getvalue())

    def test_stale_generated_file_passes_only_after_explicit_refresh(self) -> None:
        translator = FakeTranslator()
        module = load_script(translator)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, destination = self.make_source(root)
            module.ROOT = root
            self.assertEqual(0, module.main(["--target", "es"]))
            source.write_text("Changed English source\n", encoding="utf-8")

            stdout = io.StringIO()
            with redirect_stdout(stdout):
                result = module.main(
                    ["--target", "es", "--refresh-generated", "--allow-protected-existing"]
                )

            self.assertEqual(0, result)
            self.assertIn("[refresh]", stdout.getvalue())
            self.assertIn("Changed English source", destination.read_text(encoding="utf-8"))
            translator.chunks.clear()
            self.assertEqual(0, module.main(["--target", "es"]))
            self.assertEqual([], translator.chunks)

    def test_reviewed_file_remains_protected_even_when_refresh_requested(self) -> None:
        translator = FakeTranslator()
        module = load_script(translator)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            _, destination = self.make_source(root)
            module.ROOT = root
            self.assertEqual(0, module.main(["--target", "es"]))
            destination.write_text("Human-reviewed localized edition\n", encoding="utf-8")
            translator.chunks.clear()

            stdout = io.StringIO()
            with redirect_stdout(stdout):
                result = module.main(
                    ["--target", "es", "--refresh-generated", "--allow-protected-existing"]
                )

            self.assertEqual(0, result)
            self.assertEqual("Human-reviewed localized edition\n", destination.read_text(encoding="utf-8"))
            self.assertEqual([], translator.chunks)
            self.assertIn("reason=output-modified-after-generation", stdout.getvalue())
            self.assertIn("classification=manual-or-reviewed", stdout.getvalue())

    def test_legacy_existing_file_without_checkpoint_is_reported(self) -> None:
        translator = FakeTranslator()
        module = load_script(translator)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            _, destination = self.make_source(root)
            destination.parent.mkdir()
            destination.write_text("Legacy localized edition\n", encoding="utf-8")
            module.ROOT = root

            stdout = io.StringIO()
            with redirect_stdout(stdout):
                result = module.main(["--target", "es"])

            self.assertEqual(2, result)
            self.assertEqual("Legacy localized edition\n", destination.read_text(encoding="utf-8"))
            self.assertEqual([], translator.chunks)
            self.assertIn("reason=no-trusted-checkpoint", stdout.getvalue())
            self.assertIn("[action-required]", stdout.getvalue())

            acknowledged = io.StringIO()
            with redirect_stdout(acknowledged):
                result = module.main(["--target", "es", "--allow-protected-existing"])
            self.assertEqual(0, result)
            self.assertIn("[protected-acknowledged]", acknowledged.getvalue())
            self.assertIn("not certified current", acknowledged.getvalue())

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
