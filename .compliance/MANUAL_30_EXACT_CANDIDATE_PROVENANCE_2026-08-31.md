# Manual 30 — Exact Candidate Provenance and QA

Date: 2026-08-31
Status: exact candidate bound; publication state unchanged pending durable exact-byte staging and final reconciliation.

## Candidate transaction

- Candidate workflow: `53 - Manual 30 Candidate Build`
- Workflow run: `33409871076`
- Candidate PR: `#394`
- Workflow head: `90d8c526225c0deee4838699691c11e0e2aff5fc`
- Artifact ID: `9764680408`
- Artifact name: `manual30-six-binary-candidate`
- Artifact digest: `sha256:4142932df810e97d88b243905cb1ead50e147f743654439893f5ee48301a0ac5`
- Manifest source commit: `76c69c842e577db7a2c901f68b7afee18b2534dc`

## Exact binary identities

| Locale | File | Bytes | SHA-256 |
|---|---|---:|---|
| en | `Manual_30_Enterprise_GRC_Integration_Crosswalks_Controlled_EN.docx` | 40636 | `9c8ab6e1cc6e167ba541274d9178d7468767ed44c6f85bcedb8bbe167d753492` |
| en | `Manual_30_Enterprise_GRC_Integration_Crosswalks_Controlled_EN.pdf` | 65557 | `0c862907c4e8c5c98c7bb932a3a0d3cff1ad0a29db2ffc64983d9f1f88efabc8` |
| es-419 | `Manual_30_Enterprise_GRC_Integration_Crosswalks_Controlled_ES-419.docx` | 40496 | `e40f0e6b37c154af1ce7478b72e5a93b86c7f5acbd6ffea116ac1485df70e7fa` |
| es-419 | `Manual_30_Enterprise_GRC_Integration_Crosswalks_Controlled_ES-419.pdf` | 66350 | `933bf7e6d3b789362a0b1bff9dec5b45dc01e815d15b98ec8274de1989cb5423` |
| pt-BR | `Manual_30_Enterprise_GRC_Integration_Crosswalks_Controlled_PT-BR.docx` | 40464 | `4d77a25896d6e6915079cf532b3c80274265999b567ecb2aa88e79f93bd61207` |
| pt-BR | `Manual_30_Enterprise_GRC_Integration_Crosswalks_Controlled_PT-BR.pdf` | 67169 | `b65ef04c3dd24a2613fd0c885c5f03df1081cd71a83f4615f9296b3edb5a55f0` |

## Deterministic QA on downloaded exact artifact

- All six local SHA-256 values and byte sizes matched the workflow manifest exactly.
- PDF preflight: all three PDFs openable, unencrypted, non-scanned/searchable, no XFA; 5 pages each.
- Chapter completeness: Chapters 01–32 present in every exact DOCX and every exact PDF.
- DOCX accessibility audit: EN 0 high / 0 medium / 0 low; es-419 0/0/0; pt-BR 0/0/0.
- Exact PDF renders: 15 pages visually reviewed across EN/es-419/pt-BR.
- Exact DOCX renders: 12 pages visually reviewed across EN/es-419/pt-BR. Local LibreOffice pagination is tighter than the candidate-build PDF export, but content completeness is identical and no layout defect was found.
- Visual review: no clipping, overlap, missing section, broken glyph, or unreadable layout identified.
- No deterministic defect requiring regeneration was identified. The candidate bytes are therefore frozen for publication staging.

## Controlled boundary

Manual 30 is an original enterprise GRC integration/crosswalk methodology. It does not replace authoritative laws, regulations, standards, frameworks, contracts, or the source manuals. Mappings must preserve source/version, directionality, rationale, confidence, applicability, gaps, and explicit non-equivalence.

## Sequential release gate

Manual 29 is published. Manual 30 may proceed to exact-byte durable staging, ordinary exact-head repository QA, and final catalog/work-product release reconciliation. No reviewed publication binary may be regenerated or modified after this provenance binding unless a documented deterministic defect requires a new candidate transaction.