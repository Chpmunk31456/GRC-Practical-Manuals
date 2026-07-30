#!/usr/bin/env python3
"""Assemble the controlled English EU AI Act manual from canonical Markdown sources.

The script is intentionally conservative:
- it never edits source chapters or appendices;
- it prefers corrected masters;
- it fails on missing numbers, duplicate canonical selections, empty sources, or ambiguity;
- it converts very wide Markdown tables into readable record blocks for portrait DOCX/PDF;
- it writes a machine-readable manifest and one integrated Markdown master.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

ROOT_REL = Path("04-regulatory-compliance/EU_AI_Act_GRC")
CHAPTER_RE = re.compile(r"^(?P<number>\d{1,3})_(?P<title>.+)\.md$")
APPENDIX_RE = re.compile(r"^Appendix_(?P<letter>[A-Z])_(?P<title>.+)\.md$")
TABLE_DIVIDER_RE = re.compile(r"^\s*\|?(?:\s*:?-{3,}:?\s*\|)+\s*$")
WIDE_TABLE_COLUMN_LIMIT = 5


@dataclass(frozen=True)
class SourceRecord:
    item: str
    path: str
    sha256: str
    bytes: int
    lines: int


def read_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        raise ValueError(f"Empty canonical source: {path}")
    return text.replace("\r\n", "\n").replace("\r", "\n")


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def split_table_row(line: str) -> list[str]:
    """Split a simple pipe table row while preserving ordinary text."""
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def readable_wide_tables(text: str) -> str:
    """Convert tables wider than five columns into portrait-friendly record blocks.

    Source Markdown remains unchanged. Empty template rows are retained as blank fields.
    Narrow tables remain real tables. This avoids unreadable one-word-per-line columns in
    generated DOCX/PDF while preserving every header and cell value.
    """
    lines = text.splitlines()
    output: list[str] = []
    index = 0
    converted = 0

    while index < len(lines):
        if (
            lines[index].lstrip().startswith("|")
            and index + 1 < len(lines)
            and TABLE_DIVIDER_RE.match(lines[index + 1])
        ):
            block: list[str] = []
            cursor = index
            while cursor < len(lines) and lines[cursor].lstrip().startswith("|"):
                block.append(lines[cursor])
                cursor += 1

            headers = split_table_row(block[0])
            if len(headers) > WIDE_TABLE_COLUMN_LIMIT:
                rows = [split_table_row(row) for row in block[2:]]
                output.append(f"**Readable record format ({len(headers)} source columns):**")
                output.append("")
                if not rows:
                    rows = [[""] * len(headers)]
                for row_number, row in enumerate(rows, start=1):
                    padded = row + [""] * (len(headers) - len(row))
                    if len(rows) > 1:
                        output.append(f"**Record {row_number}**")
                        output.append("")
                    for header, value in zip(headers, padded):
                        label = header or "Field"
                        output.append(f"- **{label}:** {value}")
                    output.append("")
                converted += 1
                index = cursor
                continue

        output.append(lines[index])
        index += 1

    if converted:
        output.append("")
        output.append(f"<!-- publication-builder: converted {converted} wide table(s) to readable record format -->")
    return "\n".join(output).strip() + "\n"


def choose_chapter(paths: Iterable[Path], number: int) -> Path:
    candidates = list(paths)
    if not candidates:
        raise ValueError(f"Missing Chapter {number}")

    corrected_master = [p for p in candidates if p.stem.endswith("_CORRECTED_MASTER")]
    corrected = [p for p in candidates if "_CORRECTED" in p.stem and p not in corrected_master]
    originals = [p for p in candidates if "_CORRECTED" not in p.stem]

    explicit = {
        6: "06_Application_Timeline_and_Transitional_Rules_CORRECTED.md",
        20: "20_High_Risk_Classification_CORRECTED.md",
        21: "21_Annex_I_and_Annex_III_Analysis_CORRECTED.md",
        34: "34_New_Prohibitions_for_Non_Consensual_Intimate_Content_and_Child_Sexual_Abuse_Material_CORRECTED.md",
        71: "71_AI_Vendor_Due_Diligence_CORRECTED_MASTER.md",
        72: "72_Contract_Clauses_CORRECTED_MASTER.md",
        73: "73_Provider_Documentation_Review_CORRECTED_MASTER.md",
        74: "74_Model_Cards_System_Cards_and_Limitations_CORRECTED_MASTER.md",
        75: "75_Audit_Rights_and_Incident_Notification_CORRECTED_MASTER.md",
        76: "76_Cloud_API_and_Model_Dependency_Risk_CORRECTED_MASTER.md",
        77: "77_Open_Source_and_Component_Governance_CORRECTED_MASTER.md",
        78: "78_Ongoing_Vendor_Monitoring_CORRECTED_MASTER.md",
        79: "79_Exit_Portability_and_Continuity_Planning_CORRECTED_MASTER.md",
    }
    if number in explicit:
        matches = [p for p in candidates if p.name == explicit[number]]
        if len(matches) != 1:
            raise ValueError(
                f"Chapter {number} explicit canonical source missing or duplicated: {explicit[number]}"
            )
        return matches[0]

    if len(corrected_master) == 1:
        return corrected_master[0]
    if len(corrected_master) > 1:
        raise ValueError(
            f"Ambiguous corrected masters for Chapter {number}: "
            + ", ".join(p.name for p in corrected_master)
        )
    if len(corrected) == 1:
        return corrected[0]
    if len(corrected) > 1:
        raise ValueError(
            f"Ambiguous corrected sources for Chapter {number}: "
            + ", ".join(p.name for p in corrected)
        )
    if len(originals) == 1:
        return originals[0]
    raise ValueError(
        f"Ambiguous original sources for Chapter {number}: "
        + ", ".join(p.name for p in originals)
    )


def choose_appendix(paths: Iterable[Path], letter: str) -> Path:
    candidates = list(paths)
    if not candidates:
        raise ValueError(f"Missing Appendix {letter}")
    corrected = [p for p in candidates if p.stem.endswith("_CORRECTED_MASTER")]
    if len(corrected) == 1:
        return corrected[0]
    if len(corrected) > 1:
        raise ValueError(
            f"Ambiguous corrected masters for Appendix {letter}: "
            + ", ".join(p.name for p in corrected)
        )
    if len(candidates) == 1:
        return candidates[0]
    raise ValueError(
        f"Ambiguous original sources for Appendix {letter}: "
        + ", ".join(p.name for p in candidates)
    )


def demote_top_heading(text: str) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("# "):
            lines[index] = "## " + line[2:]
            break
    return "\n".join(lines).strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--out-dir", default="build/eu-ai-act")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    root = repo_root / ROOT_REL
    chapters_dir = root / "chapters"
    appendices_dir = root / "appendices"
    out_dir = repo_root / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    chapter_map: dict[int, list[Path]] = {}
    for path in sorted(chapters_dir.glob("*.md")):
        match = CHAPTER_RE.match(path.name)
        if match:
            chapter_map.setdefault(int(match.group("number")), []).append(path)

    appendix_map: dict[str, list[Path]] = {}
    for path in sorted(appendices_dir.glob("*.md")):
        match = APPENDIX_RE.match(path.name)
        if match:
            appendix_map.setdefault(match.group("letter"), []).append(path)

    selected_chapters = [choose_chapter(chapter_map.get(n, []), n) for n in range(1, 139)]
    selected_appendices = [
        choose_appendix(appendix_map.get(chr(code), []), chr(code))
        for code in range(ord("A"), ord("Z") + 1)
    ]

    front_matter = """---
title: "EU Artificial Intelligence Act GRC Compliance Manual"
subtitle: "Practical Governance, Risk, Compliance, Control, Evidence, Audit, and Implementation Guide"
author: "Al Leiva, with AI-assisted drafting and review support"
date: "30 July 2026"
lang: en-US
toc: true
toc-depth: 3
numbersections: true
---

# EU Artificial Intelligence Act GRC Compliance Manual

> **Publication status:** Controlled English review edition. This edition is not legal advice and is not approved for external release until final owner authorization.

## Legal and educational disclaimer

This manual is an educational and operational governance resource. It does not replace qualified legal advice, conformity assessment, notified-body review, competent-authority direction, sector-specific obligations, or the current consolidated text of applicable law. Legal conclusions must be verified against Regulation (EU) 2024/1689, as amended by Regulation (EU) 2026/1744, and the current consolidated EUR-Lex text.

## How to use this manual

Use each chapter to identify the applicable requirement, understand it in plain English, apply the GlobalWay Travel Services example, define control activity, retain evidence, and perform an audit test. Distinguish binding legal duties from organization-imposed controls, recommended practices, contractual duties, and optional enhancements.

## Controlled legal baseline

- Regulation (EU) 2024/1689, as amended.
- Regulation (EU) 2026/1744.
- Current consolidated EUR-Lex text.
- Official European Commission and EU AI Office material, identified as non-binding guidance unless incorporated through a binding instrument.

"""

    parts = [front_matter]
    records: list[SourceRecord] = []

    for number, path in enumerate(selected_chapters, start=1):
        source_text = read_text(path)
        records.append(
            SourceRecord(
                item=f"Chapter {number}",
                path=str(path.relative_to(repo_root)),
                sha256=digest(source_text),
                bytes=len(source_text.encode("utf-8")),
                lines=len(source_text.splitlines()),
            )
        )
        publication_text = readable_wide_tables(source_text)
        parts.append("\n\\newpage\n\n" + demote_top_heading(publication_text))

    parts.append("\n\\newpage\n\n# Appendices\n")
    for code, path in zip(range(ord("A"), ord("Z") + 1), selected_appendices):
        letter = chr(code)
        source_text = read_text(path)
        records.append(
            SourceRecord(
                item=f"Appendix {letter}",
                path=str(path.relative_to(repo_root)),
                sha256=digest(source_text),
                bytes=len(source_text.encode("utf-8")),
                lines=len(source_text.splitlines()),
            )
        )
        publication_text = readable_wide_tables(source_text)
        parts.append("\n\\newpage\n\n" + demote_top_heading(publication_text))

    master = "\n".join(parts).rstrip() + "\n"
    master_path = out_dir / "EU_AI_Act_GRC_Compliance_Manual_English_Controlled_Master.md"
    master_path.write_text(master, encoding="utf-8")

    manifest = {
        "title": "EU AI Act GRC Compliance Manual - English Controlled Master",
        "source_branch": "manual/eu-ai-act-grc-compliance",
        "chapter_count": len(selected_chapters),
        "appendix_count": len(selected_appendices),
        "wide_table_publication_policy": "Tables with more than five columns are rendered as readable record blocks; source Markdown is unchanged.",
        "master_sha256": digest(master),
        "records": [asdict(record) for record in records],
    }
    manifest_path = out_dir / "CANONICAL_BUILD_MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote {master_path}")
    print(f"Wrote {manifest_path}")
    print(f"Chapters: {len(selected_chapters)}; appendices: {len(selected_appendices)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # fail closed with an actionable message
        print(f"BUILD ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
