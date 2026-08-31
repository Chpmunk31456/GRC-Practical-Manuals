import json
from pathlib import Path

catalog_path = Path('.compliance/manual-catalog.json')
registry_path = Path('.compliance/work-product-releases.json')

catalog = json.loads(catalog_path.read_text(encoding='utf-8'))
registry = json.loads(registry_path.read_text(encoding='utf-8'))

pred_id = 'ai-privacy-automated-decision-governance-controlled'
manual_id = 'software-ai-supply-chain-assurance-controlled'

pred_catalog = next((m for m in catalog['manuals'] if m.get('id') == pred_id), None)
pred_registry = next((m for m in registry['released_work_products'] if m.get('id') == pred_id), None)
assert pred_catalog and pred_catalog.get('status') == 'published' and pred_catalog.get('release_state') == 'published', 'Manual 28 not published in catalog'
assert pred_registry and pred_registry.get('release_state') == 'published', 'Manual 28 not published in release registry'

base = Path('06-cloud-and-technology-risk/Software_AI_Supply_Chain_Assurance/publication')
files = [
 base/'en/Manual_29_Software_AI_Supply_Chain_Assurance_Controlled_EN.docx',
 base/'en/Manual_29_Software_AI_Supply_Chain_Assurance_Controlled_EN.pdf',
 base/'es-419/Manual_29_Software_AI_Supply_Chain_Assurance_Controlled_ES-419.docx',
 base/'es-419/Manual_29_Software_AI_Supply_Chain_Assurance_Controlled_ES-419.pdf',
 base/'pt-BR/Manual_29_Software_AI_Supply_Chain_Assurance_Controlled_PT-BR.docx',
 base/'pt-BR/Manual_29_Software_AI_Supply_Chain_Assurance_Controlled_PT-BR.pdf',
]
for p in files:
    assert p.exists() and p.stat().st_size > 0, f'missing/empty staged artifact: {p}'

record = {
  'id': manual_id,
  'title': 'Manual 29 — Software / AI Supply Chain Assurance Controlled Implementation',
  'path': '06-cloud-and-technology-risk/Software_AI_Supply_Chain_Assurance',
  'status': 'published',
  'release_state': 'published',
  'layout': 'controlled-build',
  'series_order': 29
}
existing = next((m for m in catalog['manuals'] if m.get('id') == manual_id), None)
if existing:
    existing.update(record)
else:
    idx = next(i for i,m in enumerate(catalog['manuals']) if m.get('id') == pred_id)
    catalog['manuals'].insert(idx+1, record)

release_record = {
  'id': manual_id,
  'type': 'manual',
  'release_state': 'published',
  'release_evidence': 'Manual 29 Software / AI Supply Chain Assurance controlled EN/es-419/pt-BR package merged through PR #386 after release-time source verification. The exact six-binary candidate was generated successfully by workflow run 33403413629 / artifact 9762169998 with artifact digest sha256:6abe47518c493b6c67447c0e21ca9d855b5a6189e78205f30f2eee3ec461b6b0. Candidate Build, Manual Structure QA, Trilingual Publication Parity, and Release Package QA passed. PR #388 bound all six immutable SHA-256 identities plus deterministic DOCX/PDF package integrity, 32-chapter completeness, accessibility with zero findings, searchable/tagged PDF checks, and full rendered review with no identified defect requiring regeneration. PR #389 durably staged the exact EN/es-419/pt-BR DOCX/PDF bytes after fail-closed verification of all six SHA-256 identities; its exact staging head 88566aed0b5ae894f0df90338de01b0777edc4ed passed Manual Structure QA, Trilingual Publication Parity, and Release Package QA before merge at 3284ccb7b6f25749f0bb9bb351af9f121e098cfe. Predecessor Manual 28 is published. Standing release authorization applies because applicable objective gates are green and no unresolved material source, applicability, technical, localization, integrity, packaging, accessibility, provenance, workflow-security, or substantive defect is recorded.'
}
existing_r = next((m for m in registry['released_work_products'] if m.get('id') == manual_id), None)
if existing_r:
    existing_r.update(release_record)
else:
    idx = next(i for i,m in enumerate(registry['released_work_products']) if m.get('id') == pred_id)
    registry['released_work_products'].insert(idx+1, release_record)

catalog['last_updated'] = '2026-08-31'
registry['last_updated'] = '2026-08-31'
catalog_path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
registry_path.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('Manual 29 publication state reconciled')
