#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

TARGET = Path(
    "01-foundations/CIS_Controls_v8.1/Espanol/"
    "CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md"
)
REPORT = Path("qa/CIS_CONTROLS_V8_1_ES_FULL_MANUAL_AUDIT.md")

CORRUPTION_PATTERNS = {
    "TEN token": re.compile(r"\bTEN(?:ED|ER|EDO|RI|CIÓN|ENDO)?\b", re.IGNORECASE),
    "tención token": re.compile(r"\btención\b", re.IGNORECASE),
    "Silencioso token": re.compile(r"\bSilencios[oa]s?\b", re.IGNORECASE),
    "tóxico token": re.compile(r"\btóxic[oa]s?\b", re.IGNORECASE),
    # Match the uppercase corruption family only. Do not flag legitimate
    # Spanish words such as "anterior".
    "ANTER corruption": re.compile(r"\bANTER[A-ZÁÉÍÓÚÑ]*\b"),
    "arrow artifact": re.compile(r"^[^\n]*←", re.MULTILINE),
    "broken image marker": re.compile(r"^[■□]img\b", re.MULTILINE | re.IGNORECASE),
    "ellipsis table delimiter": re.compile(r"^\|\.\.\.\s*\|$", re.MULTILINE),
}

ENGLISH_PHRASES = [
    "Conduct Routine Incident Response",
    "Third-Party Risk Analyst",
    "Cybersecurity Program Analyst",
    "Endpoint monitoring",
    "Vulnerability assessment",
    "Penetration Test Findings",
    "Trace finding to owner",
]

REQUIRED_SECTIONS = [f"# {n}." for n in range(1, 31)]


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def main() -> int:
    if not TARGET.is_file():
        print(f"Missing target: {TARGET}", file=sys.stderr)
        return 2

    text = TARGET.read_text(encoding="utf-8")
    findings: list[tuple[str, int, str]] = []
    counts: Counter[str] = Counter()

    for label, pattern in CORRUPTION_PATTERNS.items():
        for match in pattern.finditer(text):
            line = line_number(text, match.start())
            excerpt = text.splitlines()[line - 1].strip()[:220]
            findings.append((label, line, excerpt))
            counts[label] += 1

    for phrase in ENGLISH_PHRASES:
        start = 0
        while True:
            pos = text.find(phrase, start)
            if pos < 0:
                break
            line = line_number(text, pos)
            excerpt = text.splitlines()[line - 1].strip()[:220]
            findings.append((f"English phrase: {phrase}", line, excerpt))
            counts["residual English phrases"] += 1
            start = pos + len(phrase)

    missing_sections = [marker for marker in REQUIRED_SECTIONS if marker not in text]

    report = [
        "# CIS Controls v8.1 Spanish Full-Manual Audit",
        "",
        f"Target: `{TARGET}`",
        "",
        "## Result",
        "",
    ]

    passed = not findings and not missing_sections
    report.append("**PASS**" if passed else "**FAIL — publication blocking defects remain**")
    report.extend(["", "## Summary", ""])

    if counts:
        for label, count in sorted(counts.items()):
            report.append(f"- {label}: **{count}**")
    else:
        report.append("- No configured corruption markers found.")

    report.append(f"- Missing expected numbered sections: **{len(missing_sections)}**")
    if missing_sections:
        report.append(f"  - {', '.join(missing_sections)}")

    report.extend(["", "## Findings", ""])
    if findings:
        report.append("| Category | Line | Excerpt |")
        report.append("|---|---:|---|")
        for label, line, excerpt in sorted(findings, key=lambda item: (item[1], item[0])):
            safe = excerpt.replace("|", "\\|")
            report.append(f"| {label} | {line} | `{safe}` |")
    else:
        report.append("No configured findings.")

    report.extend(
        [
            "",
            "## Publication rule",
            "",
            "This automated audit is a minimum corruption gate. A PASS does not replace native-language, visual, accessibility, link, or factual review.",
            "",
        ]
    )
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {REPORT}")
    print("PASS" if passed else f"FAIL: {len(findings)} findings")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
