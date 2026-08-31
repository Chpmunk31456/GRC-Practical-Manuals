#!/usr/bin/env python3
import json
from pathlib import Path

CATALOG = Path('.compliance/manual-catalog.json')
RELEASES = Path('.compliance/work-product-releases.json')
MID = 'data-governance-privacy-engineering-controlled'
TITLE = 'Manual 27 — Data Governance & Privacy Engineering Controlled Implementation'
ROOT = '04-regulatory-compliance/Data_Governance_Privacy_Engineering'

EXPECTED = [
    Path(ROOT) / 'publication/en/Manual_27_Data_Governance_Privacy_Engineering_Controlled_EN.docx',
    Path(ROOT) / 'publication/en/Manual_27_Data_Governance_Privacy_Engineering_Controlled_EN.pdf',
    Path(ROOT) / 'publication/es-419/Manual_27_Data_Governance_Privacy_Engineering_Controlled_ES-419.docx',
    Path(ROOT) / 'publication/es-419/Manual_27_Data_Governance_Privacy_Engineering_Controlled_ES-419.pdf',
    Path(ROOT) / 'publication/pt-BR/Manual_27_Data_Governance_Privacy_Engineering_Controlled_PT-BR.docx',
    Path(ROOT) / 'publication/pt-BR/Manual_27_Data_Governance_Privacy_Engineering_Controlled_PT-BR.pdf',
]

catalog = json.loads(CATALOG.read_text(encoding='utf-8'))
releases = json.loads(RELEASES.read_text(encoding='utf-8'))

if not any(x.get('series_order') == 26 and x.get('status') == 'published' and x.get('release_state') == 'published' for x in catalog['manuals']):
    raise SystemExit('Manual 26 predecessor is not published in catalog')
if not any(x.get('id') == 'incident-response-cyber-crisis-controlled' and x.get('release_state') == 'published' for x in releases['released_work_products']):
    raise SystemExit('Manual 26 predecessor is not published in release registry')

missing = [str(p) for p in EXPECTED if not p.is_file() or p.stat().st_size == 0]
if missing:
    raise SystemExit('Missing or empty exact publication artifacts: ' + ', '.join(missing))

catalog_entry = {
    'id': MID,
    'title': TITLE,
    'path': ROOT,
    'status': 'published',
    'release_state': 'published',
    'layout': 'controlled-build',
    'series_order': 27,
}
existing = next((x for x in catalog['manuals'] if x.get('id') == MID), None)
if existing:
    existing.update(catalog_entry)
else:
    idx = next((i for i, x in enumerate(catalog['manuals']) if x.get('id') == 'ai-governance-audit-toolkit'), len(catalog['manuals']))
    catalog['manuals'].insert(idx, catalog_entry)

release_evidence = (
    'Manual 27 Data Governance & Privacy Engineering controlled EN/es-419/pt-BR package merged through PR #370 after release-time source-state verification using NIST Privacy Framework 1.0 as the stable published NIST baseline and NISTIR 8062 as a privacy-engineering reference, while keeping jurisdiction-specific legal requirements separate. '
    'The exact six-binary candidate was generated successfully by workflow run 33395518151 / artifact 9759165368 with artifact digest sha256:89bc8bd17f6d120590165713e96abc2814dca456d6f306c79a5ac4107ce5cbe9. '
    'Candidate Build, Workflow Security, Release Pipeline Meta QA, Manual Structure QA, Trilingual Publication Parity, and Release Package QA passed. '
    'PR #378 bound all six immutable SHA-256 identities plus deterministic PDF/DOCX integrity, 32-chapter completeness, accessibility, and full 24-page render-review evidence with no identified defect requiring regeneration and no documented unresolved material substantive issue. '
    'PR #379 durably staged the exact EN/es-419/pt-BR DOCX/PDF bytes after fail-closed hash verification; its owner-authored exact staging head b82e0f8b7ddb4542358e7d5d41978798be3d33ae passed Manual Structure QA, Trilingual Publication Parity, and Release Package QA before merge at 1e0bf6593760f7361ed4f8061af550b095931159. '
    'Predecessor Manual 26 is published. Standing release authorization applies because applicable objective gates are green and no unresolved material source, applicability, technical, localization, integrity, packaging, accessibility, provenance, workflow-security, or substantive defect is recorded.'
)
release_entry = {'id': MID, 'type': 'manual', 'release_state': 'published', 'release_evidence': release_evidence}
existing_release = next((x for x in releases['released_work_products'] if x.get('id') == MID), None)
if existing_release:
    existing_release.update(release_entry)
else:
    releases['released_work_products'].append(release_entry)

catalog['last_updated'] = '2026-08-31'
releases['last_updated'] = '2026-08-31'
CATALOG.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
RELEASES.write_text(json.dumps(releases, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Manual 27 publication state reconciled.')
