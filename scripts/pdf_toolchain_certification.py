#!/usr/bin/env python3
"""Validate Phase 9 immutable PDF-toolchain certification evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re

from repository_publication_qa import ROOT, read_json

SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(root: Path = ROOT) -> dict:
    lock_path = root / "config/production_pdf_dependency_lock.json"
    dockerfile = root / "Dockerfile.pdf.production"
    toolchain = read_json(root / "config/production_toolchain.json")
    lock = read_json(lock_path)
    errors = []

    base = lock.get("base_image", {})
    poppler = lock.get("poppler", {})
    pdf = toolchain.get("pdf_toolchain", {})
    if not SHA256.fullmatch(base.get("manifest_digest", "")):
        errors.append("pdf_base_image_manifest_invalid")
    if lock.get("platform") != "linux/amd64":
        errors.append("pdf_platform_not_linux_amd64")
    if not poppler.get("package_version"):
        errors.append("poppler_package_version_missing")

    text = dockerfile.read_text(encoding="utf-8")
    expected_from = "FROM " + base["name"] + "@" + base["manifest_digest"]
    if text.splitlines()[0] != expected_from:
        errors.append("pdf_dockerfile_base_digest_mismatch")
    expected_arg = "ARG POPPLER_VERSION=" + poppler["package_version"]
    if expected_arg not in text:
        errors.append("pdf_dockerfile_poppler_version_mismatch")

    configured = pdf.get("container_digest")
    evidence = pdf.get("certification_evidence") or {}
    verified = (
        bool(SHA256.fullmatch(configured or ""))
        and pdf.get("certification_status") == "VERIFIED_REPRODUCIBLE_OCI_MANIFEST"
        and evidence.get("independent_build_count", 0) >= 2
        and isinstance(evidence.get("workflow_run"), int)
        and isinstance(evidence.get("certification_job"), int)
        and pdf.get("poppler_package_version") == poppler["package_version"]
        and pdf.get("pdftotext_version") == poppler["pdftotext_version"]
        and pdf.get("pdfinfo_version") == poppler["pdfinfo_version"]
    )

    return {
        "schema_version": 1,
        "kind": "phase9_pdf_toolchain_certification",
        "contract_status": "PASS" if not errors else "FAIL",
        "errors": sorted(set(errors)),
        "dependency_lock_sha256": sha256(lock_path),
        "configured_pdf_container_digest": configured,
        "immutable_pdf_toolchain_verified": verified,
        "publication_authorized": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = validate()
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("Phase 9 PDF toolchain: " + ("VERIFIED" if result["immutable_pdf_toolchain_verified"] else "BLOCKED"))
    return 0 if result["contract_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
