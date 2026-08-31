#!/usr/bin/env python3
import json
from pathlib import Path

CATALOG = Path('.compliance/manual-catalog.json')
RELEASES = Path('.compliance/work-product-releases.json')
MID = 'incident-response-cyber-crisis-controlled'
TITLE = 'Manual 26 — Incident Response & Cyber Crisis Management Controlled Implementation'
ROOT = '05-operational-resilience/Incident_Response_Cyber_Crisis_Management'

EXPECTED = [
    Path(ROOT) / 'publication/en/Manual_26_Incident_Response_Cyber_Crisis_Controlled_EN.docx',
    Path(ROOT) / 'publication/en/Manual_26_Incident_Response_Cyber_Crisis_Controlled_EN.pdf',
    Path(ROOT) / 'publication/es-419/Manual_26_Incident_Response_Cyber_Crisis_Controlled_ES-419.docx',
    Path(ROOT) / 'publication/es-419/Manual_26_Incident_Response_Cyber_Crisis_Controlled_ES-419.pdf',
    Path(ROOT) / 'publication/pt-BR/Manual_26_Incident_Response_Cyber_Crisis_Controlled_PT-BR.docx',
    Path(ROOT) / 'publication/pt-BR/Manual_26_Incident_Response_Cyber_Crisis_Controlled_PT-BR.pdf',
]

catalog = json.loads(CATALOG.read_text(encoding='utf-8'))
releases = json.loads(RELEASES.read_text(encoding='utf-8'))

if not any(x.get('series_order') == 25 and x.get('status') == 'published' for x in catalog['manuals']):
    raise SystemExit('Manual 25 predecessor is not published in catalog')
if not any(x.get('id') == 'iso-22301-controlled' and x.get('release_state') == 'published' for x in releases['released_work_products']):
    raise SystemExit('Manual 25 predecessor is not published in release registry')

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
    'series_order': 26,
}
existing = next((x for x in catalog['manuals'] if x.get('id') == MID), None)
if existing:
    existing.update(catalog_entry)
else:
    idx = next((i for i, x in enumerate(catalog['manuals']) if x.get('id') == 'ai-governance-audit-toolkit'), len(catalog['manuals']))
    catalog['manuals'].insert(idx, catalog_entry)

release_evidence = (
    'Manual 26 Incident Response & Cyber Crisis controlled EN/es-419/pt-BR package merged through PR #365 after release-time NIST SP 800-61 Rev. 3 source revalidation. '
    'The exact six-binary candidate was generated successfully by workflow run 33391892785 / artifact 9757790333 with artifact digest sha256:b9242766f85c1e61df372d3b686cb3bf72e95c76989c9775770b4f837b8a1622. '
    'Candidate Build, Workflow Security, Release Pipeline Meta QA, Manual Structure QA, Trilingual Publication Parity, and Release Package QA passed. '
    'PR #367 bound all six immutable SHA-256 identities plus deterministic PDF/DOCX integrity, accessibility, structural-completeness, and full 24-page render-review evidence with no identified defect requiring regeneration. '
    'PR #368 durably staged the exact EN/es-419/pt-BR DOCX/PDF bytes after fail-closed hash verification; its owner-authored exact staging head 32f8dbfc6baf750d7a94912e9445d7daebbbb2fe passed Manual Structure QA, Trilingual Publication Parity, and Release Package QA before merge at 1287d8053c35641d3a52015b64305524f46d9376. '
    'Predecessor Manual 25 is published. Standing release authorization applies because applicable objective gates are green and no unresolved material source, applicability, technical, localization, integrity, packaging, accessibility, provenance, workflow-security, or substantive defect is recorded.'
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
print('Manual 26 publication state reconciled.')
