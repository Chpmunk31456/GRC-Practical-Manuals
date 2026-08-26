#!/usr/bin/env python3
"""Fail closed when a controlled manual branch drifts too far behind its upstream dependency."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / ".compliance/manual-dependency-chain.json"


def git(*args: str) -> str:
    proc = subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip())
    return proc.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--branch", help="Branch to validate; defaults to current branch")
    parser.add_argument("--max-behind", type=int, default=None)
    args = parser.parse_args()

    data = json.loads(CONFIG.read_text(encoding="utf-8"))
    current = args.branch or git("rev-parse", "--abbrev-ref", "HEAD")
    record = next((x for x in data["chains"] if x["branch"] == current), None)
    if record is None:
        print(f"Dependency freshness: SKIP ({current} is not a controlled manual branch)")
        return 0

    upstream = record["upstream"]
    threshold = args.max_behind if args.max_behind is not None else int(data["max_allowed_behind_commits"])
    remote_ref = f"origin/{upstream}"
    if upstream == "main":
        remote_ref = "origin/main"

    git("fetch", "--no-tags", "origin", upstream)
    behind = int(git("rev-list", "--count", f"HEAD..{remote_ref}"))
    ahead = int(git("rev-list", "--count", f"{remote_ref}..HEAD"))
    print(f"Manual {record['manual']} dependency freshness: branch={current} upstream={upstream} ahead={ahead} behind={behind} threshold={threshold}")

    if behind > threshold:
        print("FAIL: downstream branch drift exceeds the controlled threshold; reconcile before additional release work.")
        return 1

    print("PASS: dependency drift is within the controlled threshold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
