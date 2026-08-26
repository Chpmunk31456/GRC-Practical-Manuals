#!/usr/bin/env python3
"""Fail-closed PDF publication preflight.

Prevents blank, near-blank, malformed, or obviously truncated PDFs from passing
release QA merely because a .pdf file exists. This is machine QA only and does
not replace page-level visual/accessibility review.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MIN_PDF_BYTES = 1024
MIN_TEXT_CHARS = 80


def display_path(path: Path) -> Path:
    """Return a stable printable path for repo and external/temp artifacts."""
    resolved = path.resolve()
    try:
        return resolved.relative_to(REPO_ROOT)
    except ValueError:
        return resolved


def iter_pdfs(inputs: list[Path]) -> list[Path]:
    found: set[Path] = set()
    for item in inputs:
        path = item if item.is_absolute() else REPO_ROOT / item
        if path.is_file() and path.suffix.lower() == ".pdf":
            found.add(path.resolve())
        elif path.is_dir():
            found.update(p.resolve() for p in path.rglob("*.pdf") if p.is_file())
    return sorted(found)


def count_pages(data: bytes) -> int:
    # Match page dictionaries while excluding /Pages tree nodes.
    return len(re.findall(rb"/Type\s*/Page(?!s)\b", data))


def decoded_streams(data: bytes):
    for match in re.finditer(rb"stream\r?\n(.*?)\r?\nendstream", data, re.S):
        raw = match.group(1)
        yield raw
        for wbits in (zlib.MAX_WBITS, -zlib.MAX_WBITS):
            try:
                yield zlib.decompress(raw, wbits)
                break
            except zlib.error:
                pass


def rendered_content_hits(data: bytes) -> int:
    # Common text/image/path operators. Useful even when a stream is compressed.
    pattern = rb"(?:^|\s)(?:BT|Tf|Tj|TJ|'|\"|Do|re|m|l|c|v|y|h|S|s|f|F|f\*|B|B\*|b|b\*|cm)(?:\s|$)"
    hits = len(re.findall(pattern, data, re.M))
    for stream in decoded_streams(data):
        hits += len(re.findall(pattern, stream, re.M))
    return hits


def extract_text_chars(path: Path) -> int | None:
    exe = shutil.which("pdftotext")
    if not exe:
        return None
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "text.txt"
        proc = subprocess.run(
            [exe, "-enc", "UTF-8", str(path), str(out)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30,
            check=False,
        )
        if proc.returncode != 0 or not out.exists():
            return 0
        text = out.read_text(encoding="utf-8", errors="ignore")
        return len(re.sub(r"\s+", "", text))


def check_pdf(path: Path) -> list[str]:
    errors: list[str] = []
    data = path.read_bytes()
    rel = display_path(path)

    if len(data) < MIN_PDF_BYTES:
        errors.append(f"{rel}: PDF is suspiciously small ({len(data)} bytes)")
        return errors
    if not data.startswith(b"%PDF-"):
        errors.append(f"{rel}: missing PDF header")
    if b"%%EOF" not in data[-4096:]:
        errors.append(f"{rel}: missing terminal PDF EOF marker")

    pages = count_pages(data)
    if pages < 1:
        errors.append(f"{rel}: PDF has zero detectable pages")

    content_hits = rendered_content_hits(data)
    if content_hits < 1:
        errors.append(f"{rel}: no detectable rendered page-content operators")

    text_chars = extract_text_chars(path)
    if text_chars is not None and text_chars < MIN_TEXT_CHARS:
        errors.append(
            f"{rel}: extracted text is blank/near-blank ({text_chars} non-whitespace characters)"
        )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, default=[Path(".")])
    args = parser.parse_args()

    pdfs = iter_pdfs(args.paths)
    if not pdfs:
        print("PDF content preflight: no PDFs found; nothing to check")
        return 0

    errors: list[str] = []
    for pdf in pdfs:
        pdf_errors = check_pdf(pdf)
        label = display_path(pdf)
        if pdf_errors:
            errors.extend(pdf_errors)
            print(f"[FAIL] {label}")
            for err in pdf_errors:
                print(f"  ERROR: {err}")
        else:
            print(f"[PASS] {label}")

    if errors:
        print(f"PDF content preflight: FAIL ({len(errors)} error(s))")
        return 1
    print(f"PDF content preflight: PASS ({len(pdfs)} PDF(s) checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
