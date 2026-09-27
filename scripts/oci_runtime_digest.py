#!/usr/bin/env python3
"""Compute a stable digest for executable OCI runtime semantics."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import tarfile


def blob_name(digest: str) -> str:
    algo, value = digest.split(":", 1)
    if algo != "sha256" or len(value) != 64:
        raise ValueError("unsupported OCI digest")
    return f"blobs/sha256/{value}"


def runtime_contract(path: Path) -> dict:
    with tarfile.open(path, "r") as tf:
        index = json.load(tf.extractfile("index.json"))
        if len(index.get("manifests", [])) != 1:
            raise ValueError("expected one OCI manifest")
        manifest_desc = index["manifests"][0]
        manifest = json.load(tf.extractfile(blob_name(manifest_desc["digest"])))
        config = json.load(tf.extractfile(blob_name(manifest["config"]["digest"])))

    normalized_config = config.get("config") or {}
    rootfs = config.get("rootfs") or {}
    layers = [
        {
            "mediaType": layer.get("mediaType"),
            "digest": layer.get("digest"),
            "size": layer.get("size"),
        }
        for layer in manifest.get("layers", [])
    ]
    return {
        "schema_version": 1,
        "architecture": config.get("architecture"),
        "os": config.get("os"),
        "config": normalized_config,
        "rootfs": rootfs,
        "layers": layers,
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
