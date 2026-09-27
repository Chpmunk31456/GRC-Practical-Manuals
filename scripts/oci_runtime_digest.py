#!/usr/bin/env python3
"""Compute a stable digest for executable OCI runtime semantics."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import tarfile


def blob_name(digest: str) -> str:
    algo, value = digest.split(":", 1)
    if algo != "sha256" or len(value) != 64:
        raise ValueError("unsupported OCI digest")
    return f"blobs/sha256/{value}"


def _layer_records(raw: bytes) -> list[dict]:
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    records = []
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:") as layer:
        members = sorted(layer.getmembers(), key=lambda m: m.name)
        for member in members:
            record = {
                "path": member.name,
                "type": member.type.decode("latin1") if isinstance(member.type, bytes) else str(member.type),
                "mode": member.mode,
                "uid": member.uid,
                "gid": member.gid,
                "linkname": member.linkname or "",
            }
            if member.isfile():
                extracted = layer.extractfile(member)
                data = extracted.read() if extracted is not None else b""
                record["size"] = len(data)
                record["content_sha256"] = hashlib.sha256(data).hexdigest()
            records.append(record)
    return records


def runtime_contract(path: Path) -> dict:
    with tarfile.open(path, "r") as tf:
        index = json.load(tf.extractfile("index.json"))
        if len(index.get("manifests", [])) != 1:
            raise ValueError("expected one OCI manifest")
        manifest_desc = index["manifests"][0]
        manifest = json.load(tf.extractfile(blob_name(manifest_desc["digest"])))
        config = json.load(tf.extractfile(blob_name(manifest["config"]["digest"])))
        filesystem = []
        for layer_desc in manifest.get("layers", []):
            layer_raw = tf.extractfile(blob_name(layer_desc["digest"])).read()
            filesystem.extend(_layer_records(layer_raw))

    # Docker/BuildKit may emit different created/history timestamps and tar
    # mtimes/compression metadata for an otherwise identical runtime. Bind the
    # certification to executable config plus canonical filesystem semantics.
    return {
        "schema_version": 2,
        "architecture": config.get("architecture"),
        "os": config.get("os"),
        "config": config.get("config") or {},
        "filesystem": filesystem,
    }


def runtime_digest(path: Path) -> str:
    payload = json.dumps(
        runtime_contract(path),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("oci", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    contract = runtime_contract(args.oci)
    digest = runtime_digest(args.oci)
    if args.json:
        print(json.dumps({"runtime_digest": digest, "contract": contract}, indent=2))
    else:
        print(digest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
