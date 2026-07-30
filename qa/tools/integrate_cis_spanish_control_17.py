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

START = "# 22."
END = "# 23."


def extract_rewrite(text: str) -> str:
    start = text.find("# 22. Control 17")
    if start < 0:
        raise ValueError("Reviewed rewrite is missing the # 22. Control 17 heading")
    end = text.find("## Criterios de aceptación", start)
    if end < 0:
        raise ValueError("Reviewed rewrite is missing its acceptance-criteria boundary")
    return text[start:end].rstrip() + "\n\n"


def main() -> int:
    if not TARGET.is_file() or not REWRITE.is_file():
        print("Missing target or reviewed rewrite", file=sys.stderr)
        return 2

    target = TARGET.read_text(encoding="utf-8")
    rewrite = extract_rewrite(REWRITE.read_text(encoding="utf-8"))

    starts = [m.start() for m in re.finditer(r"(?m)^# 22\.", target)]
    ends = [m.start() for m in re.finditer(r"(?m)^# 23\.", target)]
    if len(starts) != 1 or len(ends) != 1 or not starts[0] < ends[0]:
        print(f"Ambiguous section boundaries: starts={len(starts)}, ends={len(ends)}", file=sys.stderr)
        return 3

    updated = target[: starts[0]] + rewrite + target[ends[0] :]

    section = updated[updated.index("# 22.") : updated.index("# 23.")]
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

    TARGET.write_text(updated, encoding="utf-8")
    print(f"Integrated reviewed Control 17 into {TARGET}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
