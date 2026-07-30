#!/usr/bin/env python3
"""Normalize generated publication headings and keep the manifest hash authoritative."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

TOP_LEVEL_RE = re.compile(r"^## (Chapter \d+\b.*|Appendix [A-Z]\b.*)$")


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--build-dir", default="build/eu-ai-act")
    args = parser.parse_args()

    build_dir = Path(args.build_dir)
    master_path = build_dir / "EU_AI_Act_GRC_Compliance_Manual_English_Controlled_Master.md"
    manifest_path = build_dir / "CANONICAL_BUILD_MANIFEST.json"

    text = master_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    promoted = 0

    for index, line in enumerate(lines):
        match = TOP_LEVEL_RE.match(line)
        if match:
            lines[index] = "# " + match.group(1)
            promoted += 1

    if promoted != 164:
        raise ValueError(f"Expected to promote 164 chapter/appendix headings; promoted {promoted}")

    normalized = "\n".join(lines).rstrip() + "\n"
    master_path.write_text(normalized, encoding="utf-8")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["heading_publication_policy"] = (
        "Chapter 1-138 and Appendix A-Z titles are level-one headings; internal sections retain their source hierarchy."
    )
    manifest["printed_toc_depth"] = 1
    manifest["master_sha256"] = digest(normalized)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"Promoted {promoted} chapter and appendix headings")
    print(f"Updated {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
