#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

TARGET = Path("01-foundations/NIST_CSF_2/English_Source_NIST_CSF_2_Practical_GRC_and_Junior_Analyst_Manual_v1.0.md")
REPORT = Path("qa/NIST_CSF_2_ENGLISH_MASTER_AUDIT.md")

PATTERNS = {
    "conversion box glyph": re.compile(r"□"),
    "broken image marker": re.compile(r"^[■□]img\b", re.MULTILINE | re.IGNORECASE),
    "double heading marker": re.compile(r"^#\s+#\s+", re.MULTILINE),
    "raw separator line": re.compile(r"^-{20,}$", re.MULTILINE),
    "empty markdown link": re.compile(r"\[[^\]]+\]\(\s*\)"),
    "placeholder token": re.compile(r"\b(?:TBD|TODO|FIXME|PLACEHOLDER)\b", re.IGNORECASE),
    "malformed Word contents label": re.compile(r"\*\*True Word contents:\*\*", re.IGNORECASE),
}

REQUIRED_SECTIONS = [re.compile(rf"^#\s+{n}\.\s+", re.MULTILINE) for n in range(1, 25)]
REQUIRED_FACT_PATTERNS = {
    "106 Core outcomes": re.compile(r"\b106\s+(?:CSF\s+)?Core outcomes\b", re.IGNORECASE),
    "Govern Function": re.compile(r"^#\s+4\.\s+GOVERN Function$", re.MULTILINE),
    "Identify Function": re.compile(r"^#\s+5\.\s+IDENTIFY Function$", re.MULTILINE),
    "Protect Function": re.compile(r"^#\s+6\.\s+PROTECT Function$", re.MULTILINE),
    "Detect Function": re.compile(r"^#\s+7\.\s+DETECT Function$", re.MULTILINE),
    "Respond Function": re.compile(r"^#\s+8\.\s+RESPOND Function$", re.MULTILINE),
    "Recover Function": re.compile(r"^#\s+9\.\s+RECOVER Function$", re.MULTILINE),
    "Tier 1 Partial": re.compile(r"Tier\s*1\s*[-—:]?\s*Partial", re.IGNORECASE),
    "Tier 2 Risk Informed": re.compile(r"Tier\s*2\s*[-—:]?\s*Risk[- ]Informed", re.IGNORECASE),
    "Tier 3 Repeatable": re.compile(r"Tier\s*3\s*[-—:]?\s*Repeatable", re.IGNORECASE),
    "Tier 4 Adaptive": re.compile(r"Tier\s*4\s*[-—:]?\s*Adaptive", re.IGNORECASE),
}


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

    missing_sections = [str(i) for i, pattern in enumerate(REQUIRED_SECTIONS, start=1) if not pattern.search(text)]
    duplicate_sections = [str(i) for i, pattern in enumerate(REQUIRED_SECTIONS, start=1) if len(pattern.findall(text)) != 1]
    missing_facts = [label for label, pattern in REQUIRED_FACT_PATTERNS.items() if not pattern.search(text)]

    status = "PASS" if not findings and not missing_sections and not duplicate_sections and not missing_facts else "REVIEW REQUIRED"
    report = [
        "# NIST CSF 2.0 English Master Audit",
        "",
        f"Target: `{TARGET}`",
        "",
        "## Result",
        "",
        f"**{status}**",
        "",
        "## Summary",
        "",
    ]
    if counts:
        for label, count in sorted(counts.items()):
            report.append(f"- {label}: **{count}**")
    else:
        report.append("- No configured structural or placeholder markers found.")
    report.append(f"- Missing expected numbered sections: **{len(missing_sections)}**")
    report.append(f"- Sections not appearing exactly once: **{len(duplicate_sections)}**")
    report.append(f"- Missing required framework facts: **{len(missing_facts)}**")

    report.extend(["", "## Findings", ""])
    if findings:
        report.extend(["| Category | Line | Excerpt |", "|---|---:|---|"])
        for label, line, excerpt in sorted(findings, key=lambda item: (item[1], item[0])):
            report.append(f"| {label} | {line} | `{excerpt.replace('|', '\\|')}` |")
    else:
        report.append("No configured findings.")

    if missing_sections:
        report.extend(["", "### Missing sections", "", ", ".join(missing_sections)])
    if duplicate_sections:
        report.extend(["", "### Sections not appearing exactly once", "", ", ".join(duplicate_sections)])
    if missing_facts:
        report.extend(["", "### Missing required framework facts", "", "\n".join(f"- {item}" for item in missing_facts)])

    report.extend([
        "",
        "## Review boundary",
        "",
        "This automated baseline checks structural integrity, placeholders, section counts, six Functions, Tier names, and the stated Core-outcome count. It does not replace detailed technical, editorial, link, visual, accessibility, or standards-currentness review.",
        "",
    ])
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {REPORT}: {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
