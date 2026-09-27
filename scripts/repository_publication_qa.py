#!/usr/bin/env python3
"""Discover controlled manuals and run every Phase 4 gate without approval inference."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path, PurePosixPath
import re
import time

import controlled_publication_qa as publication
import publication_accessibility_qa as accessibility
import publication_layout_qa as layout
import publication_roundtrip_qa as roundtrip

ROOT = Path(__file__).resolve().parents[1]
INDEX = "config/controlled_publications/index.json"
GATES = ("publication", "roundtrip", "layout", "accessibility")
CONTROLS = (
    "require_report_hash_match", "require_checksum_match", "require_docx_integrity",
    "require_pdf_integrity", "require_page_qa_pass", "require_stale_artifact_check",
    "require_roundtrip", "require_accessibility",
)
LOCALES = {"en", "es-419", "pt-BR"}


def contained(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or "\\" in relative or ":" in relative:
        raise ValueError("invalid relative path")
    rel = PurePosixPath(relative)
    if rel.is_absolute() or ".." in rel.parts:
        raise ValueError("path escapes controlled root")
    result = (root / relative).resolve()
    if not result.is_relative_to(root.resolve()) or result == root.resolve():
        raise ValueError("path escapes controlled root")
    return result


def read_json(path: Path) -> dict:
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result
    result = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique)
    if not isinstance(result, dict):
        raise ValueError("expected JSON object")
    return result


def validate(manifest: dict, root: Path) -> None:
    if publication.validate_manifest_shape(manifest):
        raise ValueError("invalid publication manifest")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", manifest["manual_id"]):
        raise ValueError("invalid manual identifier")
    count = manifest["expected_chapters"]
    if type(count) is not int or count < 1:
        raise ValueError("invalid chapter count")
    if set(manifest["languages"]) != LOCALES:
        raise ValueError("all controlled locales are required")
    if any(manifest["release_controls"].get(key) is not True for key in CONTROLS):
        raise ValueError("mandatory publication control disabled or missing")
    manual_root = contained(root, manifest["manual_root"])
    if not manual_root.is_dir():
        raise ValueError("manual directory missing")
    for key in ("publication_report", "checksum_manifest", "page_qa"):
        contained(manual_root, manifest[key])
    records = manifest.get("review_records")
    if not isinstance(records, list) or not records:
        raise ValueError("review records are required")
    for record in records:
        contained(manual_root, record["path"])
        markers = record["required_markers"]
        if not isinstance(markers, list) or not markers or any(not isinstance(x, str) or not x.strip() for x in markers):
            raise ValueError("review markers are required")
    for cfg in manifest["languages"].values():
        patterns = cfg["source_globs"]
        if not isinstance(patterns, list) or not patterns:
            raise ValueError("source inventory is required")
        for pattern in patterns:
            contained(manual_root, pattern)
            matches = list(manual_root.glob(pattern))
            for match in matches:
                if not match.resolve().is_relative_to(manual_root):
                    raise ValueError("source link escapes manual")
        regex = re.compile(cfg["chapter_heading_pattern"])
        if regex.groups != 1:
            raise ValueError("chapter pattern must have one capture")
        if not cfg.get("required_terms"):
            raise ValueError("controlled terms are required")
        for kind in ("docx", "pdf"):
            artifact = contained(manual_root, cfg["artifacts"][kind])
            if artifact.suffix != "." + kind:
                raise ValueError("artifact type mismatch")


def discover(root: Path = ROOT, index: str = INDEX) -> tuple[list[tuple[Path, dict]], list[dict]]:
    index_path = contained(root, index)
    data = read_json(index_path)
    active = data.get("manifests")
    candidates = data.get("candidate_manifests", [])
    if not isinstance(active, list) or not isinstance(candidates, list):
        raise ValueError("invalid rollout lanes")
    paths = active + candidates
    if data.get("schema_version") != 1 or not isinstance(paths, list) or not paths:
        raise ValueError("nonempty versioned rollout index required")
    if len(paths) != len(set(paths)):
        raise ValueError("duplicate manifest registration")
    catalog = read_json(root / ".compliance/manual-catalog.json")["manuals"]
    catalog_roots = {item["path"] for item in catalog}
    manifests = []
    ids, roots = set(), set()
    for relative in paths:
        path = contained(root, relative)
        if path.parent != index_path.parent or path == index_path or path.suffix != ".json":
            raise ValueError("manifest outside canonical configuration directory")
        manifest = read_json(path)
        manifest = dict(manifest, rollout_lane="active" if relative in active else "candidate")
        validate(manifest, root)
        if manifest["manual_id"] in ids or manifest["manual_root"] in roots:
            raise ValueError("duplicate manual registration")
        if manifest["manual_root"] not in catalog_roots:
            raise ValueError("manual absent from canonical catalog")
        ids.add(manifest["manual_id"])
        roots.add(manifest["manual_root"])
        manifests.append((path, manifest))
    available = {p.resolve() for p in index_path.parent.glob("*.json") if p != index_path}
    if available != {path for path, _ in manifests}:
        raise ValueError("unregistered publication configuration")
    inventory = [{"manual_id": item["id"], "manual_root": item["path"],
                  "rollout": next((m["rollout_lane"] for _, m in manifests if m["manual_root"] == item["path"]), "onboarding_required")}
                 for item in catalog]
    return manifests, inventory


def execute_gate(name: str, path: Path, manifest: dict) -> dict:
    if name == "publication":
        return publication.run_manifest(path)
    return {"roundtrip": roundtrip.run, "layout": layout.run,
            "accessibility": accessibility.run}[name](manifest)


def validate_manual(item) -> dict:
    path, manifest = item
    gates = {}
    for name in GATES:
        start = time.perf_counter()
        try:
            result = execute_gate(name, path, manifest)
            status = "PASS" if result.get("status") == "PASS" else "FAIL"
            record = {"status": status}
        except Exception as exc:
            record = {"status": "FAIL", "error_type": type(exc).__name__}
        record["seconds"] = round(time.perf_counter() - start, 6)
        gates[name] = record
    return {"manual_id": manifest["manual_id"], "rollout_lane": manifest["rollout_lane"], "gates": gates,
            "status": "PASS" if all(x["status"] == "PASS" for x in gates.values()) else "FAIL"}


def run(root: Path = ROOT, index: str = INDEX, workers: int = 2) -> dict:
    if type(workers) is not int or not 1 <= workers <= 4:
        raise ValueError("worker count must be between 1 and 4")
    started = time.perf_counter()
    manifests, inventory = discover(root, index)
    if workers == 1:
        results = [validate_manual(item) for item in manifests]
    else:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            results = list(pool.map(validate_manual, manifests))
    return {"schema_version": 1, "kind": "publication", "inventory": inventory,
            "status": "PASS" if all(x["status"] == "PASS" for x in results) else "FAIL",
            "human_publication_approval": "NOT_EVALUATED", "results": results,
            "seconds": round(time.perf_counter() - started, 6), "workers": workers,
            "validation_cache_used": False}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", default=INDEX)
    parser.add_argument("--discover", action="store_true")
    parser.add_argument("--workers", type=int, choices=(1, 2, 3, 4), default=2)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        if args.discover:
            _, inventory = discover(ROOT, args.index)
            result = {"schema_version": 1, "status": "PASS", "inventory": inventory}
        else:
            result = run(ROOT, args.index, args.workers)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result = {"schema_version": 1, "status": "FAIL", "error_type": type(exc).__name__}
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("Repository publication validation: " + result["status"])
    for item in result.get("results", []):
        print(item["manual_id"] + ": " + ", ".join(name + "=" + record["status"] for name, record in item["gates"].items()))
    print("Automated validation does not grant human publication approval.")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
