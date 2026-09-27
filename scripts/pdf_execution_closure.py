#!/usr/bin/env python3
"""Hash the executable closure of the immutable PDF inspection toolchain."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def digest_inventory(path: Path) -> str:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        digest, filename = line.split(None, 1)
        if len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
            raise ValueError("invalid closure file digest")
        if not filename.startswith("/"):
            raise ValueError("closure inventory path must be absolute")
        rows.append({"path": filename, "sha256": digest})
    rows.sort(key=lambda row: row["path"])
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inventory", type=Path)
    args = parser.parse_args()
    print(digest_inventory(args.inventory))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
