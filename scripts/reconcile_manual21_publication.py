import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / '.compliance/manual-catalog.json'
REGISTRY = ROOT / '.compliance/work-product-releases.json'

catalog = json.loads(CATALOG.read_text(encoding='utf-8'))
manual_id = 'ot-ics-security-controlled'
entry = {
    'id': manual_id,
    'title': 'Manual 21 — OT / ICS Security Controlled Implementation',
    'path': '06-cloud-and-technology-risk/OT_ICS_Security_Controlled_Implementation',
    'status': 'published',
    'release_state': 'published',
    'layout': 'controlled-build',
    'series_order': 21,
}
existing = [m for m in catalog['manuals'] if m.get('id') == manual_id or m.get('series_order') == 21]
if existing:
    if len(existing) != 1 or existing[0] != entry:
        raise SystemExit(f'conflicting Manual 21 catalog entry: {existing}')
else:
    insert_at = next((i for i, m in enumerate(catalog['manuals']) if m.get('series_order', 10**9) > 21), len(catalog['manuals']))
    # Keep non-series toolkit entries after the controlled series.
    toolkit_i = next((i for i, m in enumerate(catalog['manuals']) if m.get('id') == 'ai-governance-audit-toolkit'), len(catalog['manuals']))
    insert_at = min(insert_at, toolkit_i)
    catalog['manuals'].insert(insert_at, entry)
CATALOG.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

registry = json.loads(REGISTRY.read_text(encoding='utf-8'))
release_entry = {
    'id': manual_id,
    'type': 'manual',
    'release_state': 'published',
    'release_evidence': (
        'Manual 21 controlled English was frozen to blob e0a7095d14ce988e988077327ba1f01a8ffbde88 and controlled es-419/pt-BR localizations were merged through PR #331. '
        'The exact six-binary candidate was generated successfully by workflow run 33369538327 / artifact 9749517564 at candidate head fa0efcc62b0819f7308765705e56f18357c55e5a, with artifact digest sha256:35f6104324627d43f8ce2189eea7d4e665d0a8a327b4f62202a13d39366751bc. '
        'Manual 21 Candidate Build, Workflow Security, Release Pipeline Meta QA, and Release Package QA passed on that exact candidate. PR #334 bound the six SHA-256 identities and deterministic rendered/document structure QA with no identified defect requiring regeneration. '
        'PR #335 durably staged the exact EN/es-419/pt-BR DOCX/PDF bytes after fail-closed hash verification; staging head 0777ee99056f8a5df037b8330329e80dd2a0bb59 passed Manual Structure QA, Trilingual Publication Parity, and Release Package QA before merge. '
        'Predecessor Manual 20 is published. Standing release authorization applies under the canonical no-errors/no-unresolved-material-issues rule because applicable objective gates are green and no unresolved material source, OT/ICS safety-boundary, localization, integrity, packaging, accessibility-structure, provenance, workflow-security, or substantive defect is recorded.'
    ),
}
existing_r = [r for r in registry['released_work_products'] if r.get('id') == manual_id]
if existing_r:
    if len(existing_r) != 1 or existing_r[0] != release_entry:
        raise SystemExit(f'conflicting Manual 21 release entry: {existing_r}')
else:
    registry['released_work_products'].append(release_entry)
REGISTRY.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

# Fail closed on sequential publication state.
series = sorted((m['series_order'], m['release_state']) for m in catalog['manuals'] if 'series_order' in m and m['series_order'] <= 21)
missing = [n for n in range(1, 22) if not any(order == n and state == 'published' for order, state in series)]
if missing:
    raise SystemExit(f'predecessor publication gap(s): {missing}')

print('Manual 21 catalog/release-registry reconciliation complete')
