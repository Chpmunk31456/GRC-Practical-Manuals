#!/usr/bin/env python3
"""Translate canonical EU AI Act Markdown sources into es-419 or pt-BR.

The pipeline is deliberately source-controlled and resumable. It selects the same
canonical chapter and appendix files as the English publication builder, preserves
Markdown structure and legal references, and records source/output hashes.

Machine translation is a drafting stage. The separate QA and publication workflow
must pass before either edition is represented as reviewed or published.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import torch
from transformers import MarianMTModel, MarianTokenizer

ROOT_REL = Path("04-regulatory-compliance/EU_AI_Act_GRC")
TRANSLATIONS_REL = ROOT_REL / "translations"
MODEL_BY_LANG = {
    "es-419": "Helsinki-NLP/opus-mt-en-es",
    "pt-BR": "Helsinki-NLP/opus-mt-en-pt",
}
TARGET_LABEL = {"es-419": "Spanish (Latin America)", "pt-BR": "Portuguese (Brazil)"}

URL_RE = re.compile(r"https?://[^\s)>]+")
INLINE_CODE_RE = re.compile(r"`[^`]+`")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
LIST_PREFIX_RE = re.compile(r"^(\s*(?:[-*+] |\d+[.)] |\[[ xX]\] ))(.*)$")
HEADING_RE = re.compile(r"^(#{1,6}\s+)(.*)$")
TABLE_SEPARATOR_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$")
HTML_RE = re.compile(r"^\s*<[^>]+>\s*$")


@dataclass(frozen=True)
class TranslationRecord:
    item: str
    source_path: str
    output_path: str
    source_sha256: str
    output_sha256: str
    source_bytes: int
    output_bytes: int
    model: str


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_english_builder(repo_root: Path):
    path = repo_root / ROOT_REL / "tools" / "build_english_publication.py"
    spec = importlib.util.spec_from_file_location("english_builder", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to import canonical selector: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def canonical_sources(repo_root: Path):
    builder = load_english_builder(repo_root)
    root = repo_root / ROOT_REL
    chapter_map: dict[int, list[Path]] = {}
    for path in sorted((root / "chapters").glob("*.md")):
        match = builder.CHAPTER_RE.match(path.name)
        if match:
            chapter_map.setdefault(int(match.group("number")), []).append(path)
    appendix_map: dict[str, list[Path]] = {}
    for path in sorted((root / "appendices").glob("*.md")):
        match = builder.APPENDIX_RE.match(path.name)
        if match:
            appendix_map.setdefault(match.group("letter"), []).append(path)
    chapters = {n: builder.choose_chapter(chapter_map.get(n, []), n) for n in range(1, 139)}
    appendices = {
        chr(code): builder.choose_appendix(appendix_map.get(chr(code), []), chr(code))
        for code in range(ord("A"), ord("Z") + 1)
    }
    return chapters, appendices


def protect_inline(text: str) -> tuple[str, dict[str, str]]:
    protected: dict[str, str] = {}

    def store(value: str) -> str:
        token = f"ZXQ{len(protected):04d}QXZ"
        protected[token] = value
        return token

    def link_repl(match: re.Match[str]) -> str:
        label, url = match.groups()
        return f"[{label}]({store(url)})"

    text = MARKDOWN_LINK_RE.sub(link_repl, text)
    text = INLINE_CODE_RE.sub(lambda m: store(m.group(0)), text)
    text = URL_RE.sub(lambda m: store(m.group(0)), text)
    return text, protected


def restore_inline(text: str, protected: dict[str, str]) -> str:
    for token, value in protected.items():
        text = text.replace(token, value)
    return text


def should_copy(line: str, in_code: bool) -> bool:
    stripped = line.strip()
    return (
        in_code
        or not stripped
        or stripped in {"---", "***", "___", "\\newpage"}
        or TABLE_SEPARATOR_RE.match(line) is not None
        or HTML_RE.match(line) is not None
        or stripped.startswith("<!--")
        or stripped.startswith("{") and stripped.endswith("}")
    )


class Translator:
    def __init__(self, language: str, batch_size: int = 12):
        self.language = language
        self.model_name = MODEL_BY_LANG[language]
        self.batch_size = batch_size
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
        self.model = MarianMTModel.from_pretrained(self.model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.model.eval()

    def translate_many(self, texts: list[str]) -> list[str]:
        if not texts:
            return []
        outputs: list[str] = []
        for start in range(0, len(texts), self.batch_size):
            batch = texts[start : start + self.batch_size]
            encoded = self.tokenizer(
                batch,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=512,
            ).to(self.device)
            with torch.inference_mode():
                generated = self.model.generate(
                    **encoded,
                    max_length=640,
                    num_beams=4,
                    early_stopping=True,
                )
            outputs.extend(self.tokenizer.batch_decode(generated, skip_special_tokens=True))
        return outputs

    def translate_line(self, line: str) -> str:
        heading = HEADING_RE.match(line)
        prefix = ""
        body = line
        if heading:
            prefix, body = heading.groups()
        else:
            listed = LIST_PREFIX_RE.match(line)
            if listed:
                prefix, body = listed.groups()

        protected_body, protected = protect_inline(body)
        translated = self.translate_many([protected_body])[0]
        return prefix + restore_inline(translated, protected)

    def translate_table_line(self, line: str) -> str:
        leading = line.startswith("|")
        trailing = line.rstrip().endswith("|")
        cells = line.strip().strip("|").split("|")
        clean = [cell.strip() for cell in cells]
        protected_cells: list[tuple[str, dict[str, str]]] = [protect_inline(cell) for cell in clean]
        translated = self.translate_many([value for value, _ in protected_cells])
        restored = [restore_inline(value, protected_cells[i][1]) for i, value in enumerate(translated)]
        result = " | ".join(restored)
        if leading:
            result = "| " + result
        if trailing:
            result += " |"
        return result

    def translate_markdown(self, text: str) -> str:
        output: list[str] = []
        in_code = False
        yaml_front_matter = False
        for index, line in enumerate(text.replace("\r\n", "\n").replace("\r", "\n").splitlines()):
            stripped = line.strip()
            if index == 0 and stripped == "---":
                yaml_front_matter = True
                output.append(line)
                continue
            if yaml_front_matter:
                output.append(line)
                if stripped == "---":
                    yaml_front_matter = False
                continue
            if stripped.startswith("```") or stripped.startswith("~~~"):
                in_code = not in_code
                output.append(line)
                continue
            if should_copy(line, in_code):
                output.append(line)
                continue
            if "|" in line and line.count("|") >= 2:
                output.append(self.translate_table_line(line))
            else:
                output.append(self.translate_line(line))
        return "\n".join(output).rstrip() + "\n"


def parse_items(value: str) -> tuple[str, list[str]]:
    if value == "appendices":
        return "appendices", [chr(code) for code in range(ord("A"), ord("Z") + 1)]
    match = re.fullmatch(r"chapters:(\d+)-(\d+)", value)
    if not match:
        raise ValueError("--items must be appendices or chapters:N-M")
    start, end = map(int, match.groups())
    if start < 1 or end > 138 or start > end:
        raise ValueError("Invalid chapter range")
    return "chapters", [str(number) for number in range(start, end + 1)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--language", choices=sorted(MODEL_BY_LANG), required=True)
    parser.add_argument("--items", required=True, help="chapters:N-M or appendices")
    parser.add_argument("--batch-size", type=int, default=12)
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    category, items = parse_items(args.items)
    chapters, appendices = canonical_sources(repo_root)
    translator = Translator(args.language, batch_size=args.batch_size)
    lang_root = repo_root / TRANSLATIONS_REL / args.language / "source"
    out_dir = lang_root / category
    out_dir.mkdir(parents=True, exist_ok=True)
    records: list[TranslationRecord] = []

    for item in items:
        source = chapters[int(item)] if category == "chapters" else appendices[item]
        source_text = source.read_text(encoding="utf-8")
        translated = translator.translate_markdown(source_text)
        output = out_dir / source.name
        output.write_text(translated, encoding="utf-8")
        records.append(
            TranslationRecord(
                item=f"Chapter {item}" if category == "chapters" else f"Appendix {item}",
                source_path=str(source.relative_to(repo_root)),
                output_path=str(output.relative_to(repo_root)),
                source_sha256=sha256_text(source_text),
                output_sha256=sha256_text(translated),
                source_bytes=len(source_text.encode("utf-8")),
                output_bytes=len(translated.encode("utf-8")),
                model=translator.model_name,
            )
        )
        print(f"Translated {records[-1].item}: {output}")

    manifest_dir = repo_root / TRANSLATIONS_REL / "quality" / "manifests" / args.language
    manifest_dir.mkdir(parents=True, exist_ok=True)
    safe_items = args.items.replace(":", "_")
    manifest = manifest_dir / f"TRANSLATION_MANIFEST_{safe_items}.json"
    manifest.write_text(
        json.dumps(
            {
                "language": args.language,
                "target": TARGET_LABEL[args.language],
                "model": translator.model_name,
                "items": args.items,
                "records": [asdict(record) for record in records],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Wrote manifest: {manifest}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # fail closed
        print(f"TRANSLATION ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
