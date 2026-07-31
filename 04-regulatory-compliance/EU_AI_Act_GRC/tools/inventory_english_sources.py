#!/usr/bin/env python3
"""Report all missing English chapter and appendix source numbers in one pass."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT_REL = Path("04-regulatory-compliance/EU_AI_Act_GRC")
CHAPTER_RE = re.compile(r"^(?P<number>\d{1,3})_(?P<title>.+)\.md$")
APPENDIX_RE = re.compile(r"^Appendix_(?P<letter>[A-Z])_(?P<title>.+)\.md$")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    chapters_dir = repo_root / ROOT_REL / "chapters"
    appendices_dir = repo_root / ROOT_REL / "appendices"

    chapter_numbers: set[int] = set()
    for path in chapters_dir.glob("*.md"):
        match = CHAPTER_RE.match(path.name)
        if match:
            chapter_numbers.add(int(match.group("number")))

    appendix_letters: set[str] = set()
    for path in appendices_dir.glob("*.md"):
        match = APPENDIX_RE.match(path.name)
        if match:
            appendix_letters.add(match.group("letter"))

    missing_chapters = [number for number in range(1, 139) if number not in chapter_numbers]
    missing_appendices = [chr(code) for code in range(ord("A"), ord("Z") + 1) if chr(code) not in appendix_letters]

    print(f"Present chapter numbers: {len(chapter_numbers)} of 138")
    print(f"Present appendix letters: {len(appendix_letters)} of 26")
    print("Missing chapters: " + (", ".join(map(str, missing_chapters)) if missing_chapters else "none"))
    print("Missing appendices: " + (", ".join(missing_appendices) if missing_appendices else "none"))

    if missing_chapters or missing_appendices:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
