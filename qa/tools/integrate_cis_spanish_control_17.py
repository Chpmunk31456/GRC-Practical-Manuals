#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

TARGET = Path(
    "01-foundations/CIS_Controls_v8.1/Espanol/"
    "CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md"
)
REWRITE = Path("qa/rewrite/CIS_CONTROLS_V8_1_ES_CONTROL_17_REVIEWED.md")

CLEAN_START = re.compile(r"(?m)^# 22\.\s+Control 17\b")
LEGACY_START = re.compile(r"(?mi)^Control 17\s*[-—]\s*Gestión de la respuesta")
END = re.compile(r"(?m)^# 23\.\s+Control 18\b")


def extract_rewrite(text: str) -> str:
    start = text.find("# 22. Control 17")
    if start < 0:
        raise ValueError("Reviewed rewrite is missing the # 22. Control 17 heading")
    end = text.find("## Criterios de aceptación", start)
    if end < 0:
        raise ValueError("Reviewed rewrite is missing its acceptance-criteria boundary")
    return text[start:end].rstrip() + "\n\n"


def unique_match(pattern: re.Pattern[str], text: str, label: str) -> re.Match[str] | None:
    matches = list(pattern.finditer(text))
    if len(matches) > 1:
        raise ValueError(f"Ambiguous {label} boundary: {len(matches)} matches")
    return matches[0] if matches else None


def main() -> int:
    if not TARGET.is_file() or not REWRITE.is_file():
        print("Missing target or reviewed rewrite", file=sys.stderr)
        return 2

    target = TARGET.read_text(encoding="utf-8")
    rewrite = extract_rewrite(REWRITE.read_text(encoding="utf-8"))

    try:
        clean_start = unique_match(CLEAN_START, target, "clean Control 17 start")
        legacy_start = unique_match(LEGACY_START, target, "legacy Control 17 start")
        end = unique_match(END, target, "Control 18 end")
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 3

    if clean_start and legacy_start:
        print("Both clean and legacy Control 17 headings exist; refusing replacement", file=sys.stderr)
        return 3

    start = clean_start or legacy_start
    if start is None or end is None or start.start() >= end.start():
        print("Could not resolve one safe Control 17-to-Control 18 boundary", file=sys.stderr)
        return 3

    updated = target[: start.start()] + rewrite + target[end.start() :]

    new_start = updated.index("# 22. Control 17")
    new_end = updated.index("# 23. Control 18", new_start)
    section = updated[new_start:new_end]

    for safeguard in range(1, 10):
        marker = f"| 17.{safeguard} |"
        if section.count(marker) != 1:
            print(f"Expected exactly one {marker}", file=sys.stderr)
            return 4

    forbidden = ["TEN", "TENER", "TENED", "tención", "Silencioso", "ANTER"]
    for token in forbidden:
        if re.search(rf"\b{re.escape(token)}\b", section, flags=re.IGNORECASE):
            print(f"Forbidden corruption token remains in Control 17: {token}", file=sys.stderr)
            return 5

    if section.count("media/image9.png") != 1 or "<img " not in section:
        print("Control 17 image reference is invalid", file=sys.stderr)
        return 6

    if LEGACY_START.search(section):
        print("Legacy Control 17 heading remains after replacement", file=sys.stderr)
        return 7

    TARGET.write_text(updated, encoding="utf-8")
    print(f"Integrated reviewed Control 17 into {TARGET}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
