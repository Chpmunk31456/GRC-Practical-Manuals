#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / ".compliance" / "manual-catalog.json"
REGISTRY = ROOT / ".compliance" / "work-product-releases.json"
BASE = ROOT / "04-regulatory-compliance" / "Colombia_Data_Protection_Habeas_Data_Controlled_Implementation"
PROVENANCE = ROOT / ".compliance" / "MANUAL_37_EXACT_CANDIDATE_PROVENANCE_2026-08-31.md"
HANDOFF = ROOT / ".compliance" / "MANUAL_37_PUBLICATION_HANDOFF_2026-08-31.md"

EXPECTED = {
    "publication/en/Manual_37_Colombia_Data_Protection_Habeas_Data_Controlled_EN.docx": (42318, "a485455e05dc54b92057251fc206912da0dff8015c081efbaa24acb0427fc471"),
    "publication/en/Manual_37_Colombia_Data_Protection_Habeas_Data_Controlled_EN.pdf": (79631, "86fca9617a054fa2c0c70af0194749ac964a1c8ed0beb10670e357bdfd8819c6"),
    "publication/es-419/Manual_37_Colombia_Data_Protection_Habeas_Data_Controlled_ES-419.docx": (41556, "3b28627cea09b28d09c4af033bb408c5d0a8931009db39e2fc2e88fb4a265125"),
    "publication/es-419/Manual_37_Colombia_Data_Protection_Habeas_Data_Controlled_ES-419.pdf": (75452, "d54fa99ad668b9d00a3477c8d909cc4ac17a6ccf813ed3ff75358b185295ad73"),
    "publication/pt-BR/Manual_37_Colombia_Data_Protection_Habeas_Data_Controlled_PT-BR.docx": (41588, "97feac328e1f9a5c87ff1095af7c55bdd09dc1bfb16151db38ad8773d62556b2"),
    "publication/pt-BR/Manual_37_Colombia_Data_Protection_Habeas_Data_Controlled_PT-BR.pdf": (75959, "52d80a7e6cd0a918074ab3c3e9771d722287089444d7afe916737881e5d40991"),
}


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def published_catalog(data, manual_id):
    return any(m.get("id") == manual_id and m.get("status") == "published" and m.get("release_state") == "published" for m in data.get("manuals", []))


def published_registry(data, manual_id):
    return any(m.get("id") == manual_id and m.get("release_state") == "published" for m in data.get("released_work_products", []))


catalog = load_json(CATALOG)
registry = load_json(REGISTRY)

if not published_catalog(catalog, "brazil-lgpd-controlled"):
    raise SystemExit("FAIL: predecessor Manual 36 is not published in manual-catalog.json")
if not published_registry(registry, "brazil-lgpd-controlled"):
    raise SystemExit("FAIL: predecessor Manual 36 is not published in work-product-releases.json")

prov = PROVENANCE.read_text(encoding="utf-8")
for required in ["33429536240", "9772063050", "sha256:c5a17dd5fd611d43d6e9bd0ba7a3b5bf3726a06c0351c29051f1f4ca855defd7"]:
    if required not in prov:
        raise SystemExit(f"FAIL: provenance does not contain required identity {required}")

for rel, (size, digest) in EXPECTED.items():
    path = BASE / rel
    if not path.is_file():
        raise SystemExit(f"FAIL: missing staged artifact {rel}")
    raw = path.read_bytes()
    if len(raw) != size:
        raise SystemExit(f"FAIL: byte-size mismatch for {rel}: {len(raw)} != {size}")
    actual = hashlib.sha256(raw).hexdigest()
    if actual != digest:
        raise SystemExit(f"FAIL: SHA-256 mismatch for {rel}: {actual} != {digest}")

manual_id = "colombia-data-protection-habeas-data-controlled"
manual_entry = {
    "id": manual_id,
    "title": "Manual 37 — Colombia Data Protection / Habeas Data Controlled Implementation",
    "path": "04-regulatory-compliance/Colombia_Data_Protection_Habeas_Data_Controlled_Implementation",
    "status": "published",
    "release_state": "published",
    "layout": "controlled-build",
    "series_order": 37,
}

existing = [m for m in catalog.get("manuals", []) if m.get("id") == manual_id]
if existing:
    existing[0].update(manual_entry)
else:
    catalog.setdefault("manuals", []).append(manual_entry)

release_evidence = (
    "Manual 37 Colombia Data Protection / Habeas Data controlled EN/es-419/pt-BR package merged through PR #429 after release-time verification of Ley 1581 de 2012, applicable Decreto 1074 de 2015 provisions, current SIC Circular Única/RNBD instructions, incident-reporting controls, transfer-versus-transmission distinctions, and current 2026 SIC international-transfer conformity controls. "
    "Exact six-binary candidate workflow run 33429536240 / artifact 9772063050 is bound to artifact digest sha256:c5a17dd5fd611d43d6e9bd0ba7a3b5bf3726a06c0351c29051f1f4ca855defd7. "
    "PR #435 bound all six exact SHA-256/byte identities plus 32-chapter completeness, zero-finding DOCX accessibility audits, searchable PDF checks, and full rendered-page visual review without regeneration. "
    "PR #437 durably staged the exact six binaries after fail-closed SHA-256 verification; exact staging head 4754a246fbce81731d49590f63d58b2369055e7f passed Manual Structure QA, Trilingual Publication Parity, and Release Package QA. "
    "Predecessor Manual 36 is published; no unresolved material source, applicability, localization, integrity, packaging, accessibility, provenance, workflow-security, copyright-boundary, or substantive defect is recorded."
)
registry_entry = {
    "id": manual_id,
    "type": "manual",
    "release_state": "published",
    "release_evidence": release_evidence,
}
existing_r = [m for m in registry.get("released_work_products", []) if m.get("id") == manual_id]
if existing_r:
    existing_r[0].update(registry_entry)
else:
    registry.setdefault("released_work_products", []).append(registry_entry)

catalog["last_updated"] = "2026-08-31"
registry["last_updated"] = "2026-08-31"
CATALOG.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
REGISTRY.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

HANDOFF.write_text(
    "# Manual 37 — Final Publication Handoff\n\n"
    "Manual 37 — Colombia Data Protection / Habeas Data Controlled Implementation is reconciled to `published` in both central release registries.\n\n"
    "- Predecessor Manual 36 verified published in both registries before reconciliation.\n"
    "- Exact candidate: workflow run `33429536240`, artifact `9772063050`, digest `sha256:c5a17dd5fd611d43d6e9bd0ba7a3b5bf3726a06c0351c29051f1f4ca855defd7`.\n"
    "- Exact staged binary hashes and byte sizes were reverified before registry mutation.\n"
    "- Exact staging head `4754a246fbce81731d49590f63d58b2369055e7f` passed Manual Structure QA, Trilingual Publication Parity, and Release Package QA.\n"
    "- This transaction does not regenerate, resave, or modify any reviewed publication binary.\n"
    "- Standing clean-candidate release authorization applies because predecessor order is satisfied and no unresolved material defect is recorded.\n",
    encoding="utf-8",
)

print("PASS: Manual 37 publication state reconciled with exact-byte verification")
