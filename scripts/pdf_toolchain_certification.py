#!/usr/bin/env python3
"""Validate immutable Phase 9 PDF-toolchain certification evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from repository_publication_qa import ROOT, read_json

SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(root: Path = ROOT) -> dict:
    lock_path = root / "config/pdf_toolchain_lock.json"
    lock = read_json(lock_path)
    toolchain = read_json(root / "config/production_toolchain.json")
    pdf = toolchain.get("pdf_toolchain", {})
    errors = []

    if lock.get("ubuntu_snapshot_id") != "20260927T120000Z":
        errors.append("snapshot_id_drift")
    if lock.get("packages", {}).get("poppler-utils") != "24.02.0-1ubuntu9.9":
        errors.append("poppler_lock_drift")
    if lock.get("expected_tools", {}).get("pdftotext") != "pdftotext version 24.02.0":
        errors.append("pdftotext_lock_drift")
    if lock.get("expected_tools", {}).get("pdfinfo") != "pdfinfo version 24.02.0":
        errors.append("pdfinfo_lock_drift")

    lock_sha = sha256(lock_path)
    configured_lock = pdf.get("lock_sha256")
    if configured_lock not in (None, lock_sha):
        errors.append("pdf_lock_sha256_mismatch")

    digest = pdf.get("container_digest")
    evidence = pdf.get("certification_evidence") or {}
    verified = (
        bool(SHA256.fullmatch(digest or ""))
        and pdf.get("certification_status") == "VERIFIED_REPRODUCIBLE_OCI_MANIFEST"
        and evidence.get("independent_build_count", 0) >= 2
        and isinstance(evidence.get("workflow_run"), int)
        and isinstance(evidence.get("certification_job"), int)
    )

    return {
        "schema_version": 1,
        "kind": "phase9_pdf_toolchain_certification",
        "status": "VERIFIED" if verified and not errors else "BLOCKED",
        "errors": errors,
        "pdf_lock_sha256": lock_sha,
        "container_digest": digest,
        "immutable_pdf_toolchain_verified": verified and not errors,
        "publication_authorized": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("Phase 9 PDF toolchain: " + result["status"])
    return 0 if not result["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
