#!/usr/bin/env python3
"""Certify Phase 9 immutable production-environment prerequisites fail-closed."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

from repository_publication_qa import ROOT, read_json

SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_contract(root: Path = ROOT) -> dict:
    lock_path = root / "config/production_dependency_lock.json"
    dockerfile = root / "Dockerfile.production"
    toolchain = read_json(root / "config/production_toolchain.json")
    lock = read_json(lock_path)

    errors = []
    digest = lock.get("base_image", {}).get("manifest_digest", "")
    if not SHA256.fullmatch(digest):
        errors.append("base_image_manifest_digest_invalid")
    if lock.get("base_image", {}).get("platform") != "linux/amd64":
        errors.append("production_platform_not_linux_amd64")
    if lock.get("python") != toolchain.get("python"):
        errors.append("python_contract_mismatch")
    if lock.get("python_dependencies") != toolchain.get("python_dependencies"):
        errors.append("python_dependency_contract_mismatch")
    if lock.get("networked_package_installation_allowed") is not False:
        errors.append("networked_package_installation_not_prohibited")

    text = dockerfile.read_text(encoding="utf-8")
    expected_from = (
        "FROM " + lock["base_image"]["name"] + "@" + lock["base_image"]["manifest_digest"]
    )
    if expected_from not in text.splitlines()[:1]:
        errors.append("dockerfile_base_digest_mismatch")
    lowered = text.lower()
    for forbidden in ("apt-get install", "pip install", "curl ", "wget "):
        if forbidden in lowered:
            errors.append("dockerfile_contains_network_install")
    lock_sha = sha256(lock_path)
    build = toolchain.get("build_environment", {})
    configured_lock = build.get("generator_dependency_lock_sha256")
    configured_container = build.get("container_digest")
    evidence = build.get("certification_evidence") or {}
    if configured_lock != lock_sha:
        errors.append("configured_dependency_lock_sha256_mismatch")
    build_verified = (
        bool(SHA256.fullmatch(configured_container or ""))
        and build.get("certification_status") == "VERIFIED_REPRODUCIBLE_OCI_MANIFEST"
        and evidence.get("independent_build_count", 0) >= 2
        and isinstance(evidence.get("workflow_run"), int)
        and isinstance(evidence.get("certification_job"), int)
    )

    return {
        "errors": sorted(set(errors)),
        "dependency_lock_sha256": lock_sha,
        "base_image_manifest_digest": digest,
        "configured_build_container_digest": configured_container,
        "immutable_build_image_verified": build_verified,
        "contract_status": "PASS" if not errors else "FAIL",
    }


def docker_available() -> bool:
    try:
        subprocess.run(
            ["docker", "version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
            timeout=20,
        )
        return True
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return False


def inspect_image(image: str) -> dict:
    raw = subprocess.check_output(
        ["docker", "image", "inspect", image, "--format", "{{json .}}"],
        text=True,
    )
    data = json.loads(raw)
    image_id = data.get("Id", "")
    return {
        "image_id": image_id,
        "image_id_valid": bool(SHA256.fullmatch(image_id)),
        "repo_digests": sorted(data.get("RepoDigests") or []),
    }


def run(root: Path = ROOT, require_docker: bool = False) -> dict:
    contract = validate_contract(root)
    available = docker_available()
    result = {
        "schema_version": 1,
        "kind": "phase9_production_environment_certification",
        **contract,
        "docker_available": available,
        "immutable_build_image_verified": contract["immutable_build_image_verified"],
        "immutable_pdf_toolchain_verified": False,
        "status": "BLOCKED",
        "publication_authorized": False,
    }
    if contract["contract_status"] != "PASS":
        result["reason"] = "immutable_contract_invalid"
        return result
    if require_docker and not available:
        result["reason"] = "docker_runtime_unavailable"
        return result
    result["reason"] = (
        "immutable_pdf_toolchain_digest_evidence_required"
        if contract["immutable_build_image_verified"]
        else (
            "production_image_build_and_pdf_toolchain_digest_evidence_required"
            if available
            else "docker_runtime_and_production_digest_evidence_required"
        )
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--require-docker", action="store_true")
    args = parser.parse_args()
    result = run(require_docker=args.require_docker)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("Phase 9 production environment: " + result["status"])
    return 0 if result["contract_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
