#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

TARGET = Path(
    "01-foundations/CIS_Controls_v8.1/Portugues_BR/"
    "CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md"
)
REPORT = Path("qa/CIS_CONTROLS_V8_1_PTBR_FULL_MANUAL_AUDIT.md")

# These rules target known conversion and Markdown-corruption signatures only.
# Valid ordered lists and balanced bold paragraphs are intentionally excluded.
PATTERNS = {
    "conversion box glyph": re.compile(r"□"),
    "broken image marker": re.compile(r"^[■□]img\b", re.MULTILINE | re.IGNORECASE),
    "double heading marker": re.compile(r"^#\s+#\s+", re.MULTILINE),
    "ellipsis-only table row": re.compile(r"^(?:\|\s*)?(?:\.\s*){3,}(?:\|\s*)?$", re.MULTILINE),
    "raw separator line": re.compile(r"^-{20,}$", re.MULTILINE),
    "malformed leading emphasis": re.compile(r"^(?:No interior:|\*Conteúdo:)\*\*", re.MULTILINE | re.IGNORECASE),
    "comma subsection numbering": re.compile(r"^#{0,3}\s*(?:24|29|30),\d+\b", re.MULTILINE),
}

REQUIRED_SECTIONS = [f"# {n}." for n in range(1, 31)]


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def main() -> int:
    text = TARGET.read_text(encoding="utf-8")
    findings: list[tuple[str, int, str]] = []
    counts: Counter[str] = Counter()

    for label, pattern in PATTERNS.items():
        for match in pattern.finditer(text):
            line = line_number(text, match.start())
            excerpt = text.splitlines()[line - 1].strip()[:220]
            findings.append((label, line, excerpt))
            counts[label] += 1

    missing = [marker for marker in REQUIRED_SECTIONS if marker not in text]
    passed = not findings and not missing

    report = [
        "# CIS Controls v8.1 Brazilian Portuguese Full-Manual Audit",
        "",
        f"Target: `{TARGET}`",
        "",
        "## Result",
        "",
        "**PASS**" if passed else "**FAIL — publication-blocking defects remain**",
        "",
        "## Summary",
        "",
    ]
    if counts:
        for label, count in sorted(counts.items()):
            report.append(f"- {label}: **{count}**")
    else:
        report.append("- No configured corruption markers found.")
    report.append(f"- Missing expected numbered sections: **{len(missing)}**")
    if missing:
        report.append(f"  - {', '.join(missing)}")

    report.extend(["", "## Findings", ""])
    if findings:
        report.extend(["| Category | Line | Excerpt |", "|---|---:|---|"])
        for label, line, excerpt in sorted(findings, key=lambda item: (item[1], item[0])):
            report.append(f"| {label} | {line} | `{excerpt.replace('|', '\\|')}` |")
    else:
        report.append("No configured findings.")

    report.extend([
        "",
        "## Publication rule",
        "",
        "This automated audit is a minimum structural-corruption gate. A PASS does not replace native-language, visual, accessibility, link, or factual review.",
        "",
    ])
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {REPORT}: {'PASS' if passed else 'FAIL'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
