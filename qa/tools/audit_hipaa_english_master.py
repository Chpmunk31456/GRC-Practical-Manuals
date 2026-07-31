#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

TARGET = Path("04-regulatory-compliance/HIPAA/English_Source_HIPAA_Practical_Manager_and_Junior_Analyst_Manual_v1.0.md")
REPORT = Path("qa/HIPAA_ENGLISH_MASTER_AUDIT.md")

PATTERNS = {
    "conversion box glyph": re.compile(r"□"),
    "broken image marker": re.compile(r"^[■□]img\b", re.MULTILINE | re.IGNORECASE),
    "double heading marker": re.compile(r"^#\s+#\s+", re.MULTILINE),
    "raw separator line": re.compile(r"^-{20,}$", re.MULTILINE),
    "empty markdown link": re.compile(r"\[[^\]]+\]\(\s*\)"),
    "placeholder token": re.compile(r"\b(?:TBD|TODO|FIXME|PLACEHOLDER)\b", re.IGNORECASE),
    "malformed Word contents label": re.compile(r"\*\*True Word contents:\*\*", re.IGNORECASE),
}

REQUIRED_SECTIONS = [re.compile(rf"^#\s+{n}\.\s+", re.MULTILINE) for n in range(1, 23)]
REQUIRED_FACTS = {
    "Security Rule proposed status": "proposed rule, not the current final Security Rule",
    "Privacy Rule": "Privacy Rule",
    "Security Rule": "Security Rule",
    "Breach Notification Rule": "Breach Notification Rule",
    "Enforcement Rule": "Enforcement Rule",
    "Part 2": "42 CFR Part 2",
    "reproductive-health status section": "Reproductive-health rule status",
    "tracking technologies section": "Online tracking technologies",
    "30-day access deadline": "Generally 30 days",
    "breach four-factor assessment": "four-factor assessment",
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
    missing_facts = [label for label, marker in REQUIRED_FACTS.items() if marker not in text]

    status = "PASS" if not findings and not missing_sections and not duplicate_sections and not missing_facts else "REVIEW REQUIRED"
    report = [
        "# HIPAA English Master Audit", "", f"Target: `{TARGET}`", "", "## Result", "", f"**{status}**", "", "## Summary", ""
    ]
    if counts:
        report.extend(f"- {label}: **{count}**" for label, count in sorted(counts.items()))
    else:
        report.append("- No configured structural or placeholder markers found.")
    report.extend([
        f"- Missing expected numbered sections: **{len(missing_sections)}**",
        f"- Sections not appearing exactly once: **{len(duplicate_sections)}**",
        f"- Missing required framework facts: **{len(missing_facts)}**",
        "", "## Findings", ""
    ])
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
        report.extend(["", "### Missing required framework facts", "", *[f"- {item}" for item in missing_facts]])
    report.extend([
        "", "## Review boundary", "",
        "This automated baseline checks structural integrity, placeholders, section counts, core HIPAA rule markers, and time-sensitive status markers. It does not replace detailed legal, technical, editorial, link, visual, accessibility, or standards-currentness review.", ""
    ])
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {REPORT}: {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
