#!/usr/bin/env python3
"""Attest the executable CI toolchain without claiming immutable production verification."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import platform
import subprocess
import sys

from repository_publication_qa import ROOT, read_json


def command_output(command: list[str]) -> str:
    run = subprocess.run(command, capture_output=True, text=True, check=True)
    return (run.stdout or run.stderr).strip()


def probe() -> dict:
    package_version = command_output(["dpkg-query", "-W", "-f=${Version}", "poppler-utils"])
    pdftotext = command_output(["pdftotext", "-v"]).splitlines()[0]
    pdfinfo = command_output(["pdfinfo", "-v"]).splitlines()[0]
    return {
        "python": platform.python_version(),
        "validation_environment": "ubuntu-24.04" if sys.platform == "linux" else sys.platform,
        "runner_image": os.environ.get("ImageOS"),
        "runner_image_version": os.environ.get("ImageVersion"),
        "poppler_package_version": package_version,
        "pdftotext_version": pdftotext,
        "pdfinfo_version": pdfinfo,
    }


def verify(config: dict, observed: dict) -> list[str]:
    errors = []
    if observed["python"] != config["python"]:
        errors.append("python_version_mismatch")
    expected = config["pdf_toolchain"]["poppler_package_version"]
    if observed["poppler_package_version"] != expected:
        errors.append("poppler_package_version_mismatch")
    for key in ("pdftotext_version", "pdfinfo_version"):
        expected_tool = config["pdf_toolchain"][key]
        if observed[key] != expected_tool:
            errors.append(key + "_mismatch")
    baseline_image = config["hosted_ci_attestation"]["runner_image_version"]
    if observed.get("runner_image_version") and observed["runner_image_version"] != baseline_image:
        errors.append("runner_image_version_drift")
    return errors


def run(root: Path = ROOT) -> dict:
    config = read_json(root / "config/production_toolchain.json")
    observed = probe()
    errors = verify(config, observed)
    return {
        "schema_version": 1,
        "kind": "hosted_ci_toolchain_attestation",
        "status": "PASS" if not errors else "DRIFT",
        "observed": observed,
        "errors": errors,
        "production_status": config["status"],
        "immutable_production_environment": False,
        "publication_authorized": False,
        "boundary": "A matching hosted-CI baseline is operational evidence only. It is not an immutable production environment and does not authorize release.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("Hosted CI toolchain attestation: " + result["status"])
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
