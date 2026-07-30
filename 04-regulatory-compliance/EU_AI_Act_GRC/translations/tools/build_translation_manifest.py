#!/usr/bin/env python3
"""Generate fail-closed source manifests for es-419 and pt-BR translation work."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

CHAPTER_RE = re.compile(r"^(\d+)_.*_CORRECTED_MASTER\.md$")
APPENDIX_RE = re.compile(r"^Appendix_([A-Z])_.*_CORRECTED_MASTER\.md$")


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def select_unique(directory: Path, pattern: re.Pattern[str], expected: list[str]) -> list[Path]:
    grouped: dict[str, list[Path]] = {key: [] for key in expected}
    for path in sorted(directory.glob("*_CORRECTED_MASTER.md")):
        match = pattern.match(path.name)
        if match and match.group(1) in grouped:
            grouped[match.group(1)].append(path)
    failures = {key: values for key, values in grouped.items() if len(values) != 1}
    if failures:
        detail = "; ".join(f"{key}={len(values)}" for key, values in failures.items())
        raise SystemExit(f"Canonical source selection failed: {detail}")
    return [grouped[key][0] for key in expected]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--source-commit", required=True)
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    manual = root / "04-regulatory-compliance/EU_AI_Act_GRC"
    chapters = select_unique(
        manual / "chapters",
        CHAPTER_RE,
        [str(number) for number in range(1, 139)],
    )
    appendices = select_unique(
        manual / "appendices",
        APPENDIX_RE,
        [chr(code) for code in range(ord("A"), ord("Z") + 1)],
    )

    records = []
    for kind, paths in (("chapter", chapters), ("appendix", appendices)):
        for path in paths:
            relative = path.relative_to(root).as_posix()
            records.append(
                {
                    "kind": kind,
                    "source_path": relative,
                    "source_commit": args.source_commit,
                    "source_sha256": digest(path),
                    "es_419_target": relative.replace(
                        "04-regulatory-compliance/EU_AI_Act_GRC/",
                        "04-regulatory-compliance/EU_AI_Act_GRC/translations/es-419/source/",
                    ),
                    "pt_BR_target": relative.replace(
                        "04-regulatory-compliance/EU_AI_Act_GRC/",
                        "04-regulatory-compliance/EU_AI_Act_GRC/translations/pt-BR/source/",
                    ),
                    "es_419_status": "not_started",
                    "pt_BR_status": "not_started",
                }
            )

    output = manual / "translations/quality/TRANSLATION_SOURCE_MANIFEST.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "source_branch": "production/multilingual-grc-editions",
        "source_commit": args.source_commit,
        "chapter_count": len(chapters),
        "appendix_count": len(appendices),
        "record_count": len(records),
        "records": records,
    }
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {output} with {len(records)} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())