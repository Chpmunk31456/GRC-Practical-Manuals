# Manual 22 — Exact Candidate Provenance and Deterministic QA

Status: exact candidate bound; no publication-state change in this record.

## Controlling source

- Manual: 22 — Cloud Security Controlled Implementation
- Frozen controlled-English blob: `a056997ce359c3a37acc5b931e5f808cc09921be`
- Controlled es-419 and pt-BR sources are bound to that exact English source through the merged localization lane.
- Primary current reference state remains CSA CCM v4.1, with the documented release-time source/version/transition recheck retained.

## Exact candidate generation

- Candidate head: `e822132a5328c8f79350964de494f09dcdcb7030`
- Workflow run: `33370864191`
- Artifact ID: `9750008264`
- Artifact name: `manual22-six-binary-candidate`
- Artifact digest: `sha256:5b48e263701761cdcf8a545c827dafd537bfaed2a6afd37d69ad996e5e515c90`
- Candidate manifest SHA-256: `e0ec0ccbb28719292419cf18f17d5635199cc3b5daee71e5cff27b67f7b546b1`

## Exact six publication-candidate identities

| Locale | File | Bytes | SHA-256 |
|---|---|---:|---|
| en | `Manual_22_Cloud_Security_Controlled_EN.docx` | 42631 | `f9d97cd18bcc947eb2fe455c9968b94a88277b41bd4d07f2a6dc49c7d60b8e05` |
| en | `Manual_22_Cloud_Security_Controlled_EN.pdf` | 79486 | `8678bb1816866d2f5718eee32a9c242ce8335ba78c5c537bd1366558cd9c9ecc` |
| es-419 | `Manual_22_Cloud_Security_Controlled_ES-419.docx` | 40936 | `5b1a4c66244cace28b566a21a9e8069467cb1666817c237ea50294743684ca17` |
| es-419 | `Manual_22_Cloud_Security_Controlled_ES-419.pdf` | 76097 | `2ba27181dcc1f37e1a7fe91be4cc09f4dce200405261efefdaccc48291d40213` |
| pt-BR | `Manual_22_Cloud_Security_Controlled_PT-BR.docx` | 40936 | `bacc1dd78a028acd722f693929578d72c7fda34dfc812206b681520b723668ab` |
| pt-BR | `Manual_22_Cloud_Security_Controlled_PT-BR.pdf` | 77758 | `896c98b935491b88ba62d470be5a331885f174bc2d39361f8031ff91b75fa76d` |

## Objective QA evidence

The exact candidate head passed the applicable repository checks before merge: Manual Structure QA, Trilingual Publication Parity, Release Package QA, Workflow Security, Release Pipeline Meta QA, and the dedicated Manual 22 Candidate Build.

The exact downloaded artifact was independently checked without modifying candidate bytes. PDF rendering produced EN 6 pages, es-419 5 pages, and pt-BR 5 pages. The page-count difference reflects localization density and is not itself a defect. Render review found no identified clipping, overlap, broken glyphs, malformed page breaks, or unreadable content requiring regeneration. DOCX accessibility audit results were high=0, medium=0, low=0 for EN, es-419, and pt-BR.

A duplicate pt-BR source filename discovered during the localization-to-candidate transition was removed before candidate generation; the candidate uses the single canonical exact-English-bound pt-BR source. No unresolved deterministic source, localization, rendering, accessibility, integrity, workflow-security, packaging, or provenance defect is recorded.

## Release progression

Manual 21 is published. Manual 22 therefore proceeds to durable staging of these exact six bytes without regeneration. After exact staging-head gates pass, the canonical release rule applies: no errors + no unresolved material issues + all applicable objective gates green + predecessor published = standing authorization satisfied = publish immediately.
