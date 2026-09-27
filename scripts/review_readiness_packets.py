#!/usr/bin/env python3
"""Generate deterministic, fail-closed reviewer-readiness packets for candidate manuals."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

from repository_publication_qa import ROOT, discover, read_json, contained
from controlled_publication_qa import sha256


def canonical_hash(value: dict) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_revision(root: Path = ROOT) -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()


def source_inventory(manifest: dict, root: Path = ROOT) -> dict:
    manual_root = contained(root, manifest["manual_root"])
    result = {}
    for locale, cfg in manifest["languages"].items():
        files = []
        seen = set()
        for pattern in cfg["source_globs"]:
            for path in sorted(manual_root.glob(pattern)):
                resolved = path.resolve()
                if not resolved.is_file() or resolved in seen:
                    continue
                seen.add(resolved)
                rel = resolved.relative_to(root.resolve()).as_posix()
                files.append({"path": rel, "sha256": sha256(resolved)})
        result[locale] = files
    return result


def artifact_inventory(manifest: dict, root: Path = ROOT) -> dict:
    manual_root = contained(root, manifest["manual_root"])
    result = {}
    for locale, cfg in manifest["languages"].items():
        result[locale] = {}
        for kind in ("docx", "pdf"):
            path = contained(manual_root, cfg["artifacts"][kind])
            result[locale][kind] = {
                "path": path.relative_to(root.resolve()).as_posix(),
                "sha256": sha256(path),
            }
    return result


def review_inventory(manifest: dict, root: Path = ROOT) -> list[dict]:
    manual_root = contained(root, manifest["manual_root"])
    rows = []
    for record in manifest["review_records"]:
        path = contained(manual_root, record["path"])
        rows.append({
            "path": path.relative_to(root.resolve()).as_posix(),
            "sha256": sha256(path),
            "required_markers": list(record["required_markers"]),
            "status": "REVIEW_REQUIRED",
        })
    return rows


def repository_blockers(root: Path = ROOT) -> list[str]:
    blockers = []
    source = read_json(root / "config/source_monitoring.json")
    if not source.get("baselines"):
        blockers.append("approved_source_baselines_missing")
    translation = read_json(root / "config/translation_lifecycle.json")
    if not translation.get("dependencies") or not translation.get("reviews"):
        blockers.append("hash_bound_translation_reviews_missing")
    accessibility = read_json(root / "config/accessibility_reviews.json")
    if not accessibility.get("reviews"):
        blockers.append("independent_accessibility_reviews_missing")
    toolchain = read_json(root / "config/production_toolchain.json")
    if toolchain.get("status") != "VERIFIED":
        blockers.append("production_toolchain_not_verified")
    release = read_json(root / "config/release_policy.json")
    if len(release.get("reviewers", [])) < max(2, release.get("minimum_independent_reviewers", 2)):
        blockers.append("authorized_release_reviewers_missing")
    return blockers


def build_packet(path: Path, manifest: dict, revision: str, blockers: list[str], root: Path = ROOT) -> dict:
    payload = {
        "schema_version": 1,
        "kind": "review_readiness_packet",
        "source_revision": revision,
        "manual_id": manifest["manual_id"],
        "manual_root": manifest["manual_root"],
        "rollout_lane": manifest["rollout_lane"],
        "readiness_status": manifest.get("readiness_status", "REVIEW_REQUIRED"),
        "manifest": {
            "path": path.relative_to(root.resolve()).as_posix(),
            "sha256": sha256(path),
        },
        "sources": source_inventory(manifest, root),
        "artifacts": artifact_inventory(manifest, root),
        "review_records": review_inventory(manifest, root),
        "repository_blockers": list(blockers),
        "publication_authorized": False,
        "boundary": "This packet organizes exact evidence for human review; it does not approve publication, translations, legal conclusions, accessibility, or release.",
    }
    payload["packet_sha256"] = canonical_hash(payload)
    return payload


def run(root: Path = ROOT) -> dict:
    revision = git_revision(root)
    manifests, _ = discover(root)
    blockers = repository_blockers(root)
    packets = [
        build_packet(path, manifest, revision, blockers, root)
        for path, manifest in manifests
        if manifest["rollout_lane"] == "candidate"
    ]
    queue = [{
        "manual_id": packet["manual_id"],
        "readiness_status": packet["readiness_status"],
        "packet_sha256": packet["packet_sha256"],
        "required_review_records": [row["path"] for row in packet["review_records"]],
        "repository_blockers": packet["repository_blockers"],
        "status": "REVIEW_REQUIRED",
    } for packet in packets]
    return {
        "schema_version": 1,
        "kind": "review_readiness_queue",
        "source_revision": revision,
        "status": "REVIEW_REQUIRED" if queue else "NO_CANDIDATES",
        "candidate_count": len(queue),
        "queue": queue,
        "publication_authorized": False,
        "boundary": "Queue status is informational and fail-closed. Human approvals must be independently recorded and verified by the controlled release gate.",
        "packets": packets,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path, required=True)
    parser.add_argument("--packet-dir", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.packet_dir.mkdir(parents=True, exist_ok=True)
    for packet in result["packets"]:
        target = args.packet_dir / (packet["manual_id"] + ".json")
        target.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    queue = dict(result)
    queue.pop("packets")
    args.queue.write_text(json.dumps(queue, indent=2) + "\n", encoding="utf-8")
    print(f"Review readiness: {result['status']} ({result['candidate_count']} candidates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
