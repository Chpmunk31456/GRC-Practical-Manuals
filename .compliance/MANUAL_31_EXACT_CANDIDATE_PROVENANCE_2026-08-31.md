# Manual 31 — Exact Candidate Provenance and Deterministic QA

**Manual:** 31 — NYDFS 23 NYCRR Part 500 Controlled Implementation  
**Candidate workflow run:** `33414345441`  
**Artifact ID:** `9766406222`  
**Artifact name:** `manual31-six-binary-candidate`  
**Artifact digest:** `sha256:9e1c5df829d29730fed5398ea432940b5f478cdac2af4567b0c3dd089052ca7d`  
**Workflow PR head:** `c6fb1a9a557942acded2775d049fbea38da649a8`  
**Manifest source commit:** `bcc1dea445e9a0dfcb4f8b3e2fc8b3008c4749da`

## Exact binary identities

| Locale | File | Bytes | SHA-256 |
|---|---|---:|---|
| en | `Manual_31_NYDFS_Part_500_Controlled_EN.docx` | 41674 | `e8676aea8a5464f7ef331c8bee94262157aa2cbbea30b60116d3c1254c4fe197` |
| en | `Manual_31_NYDFS_Part_500_Controlled_EN.pdf` | 70602 | `ed6053a6cd6aaa788d0fcf20b6152d31eaba138e451a7405feb999686cc609c4` |
| es-419 | `Manual_31_NYDFS_Part_500_Controlled_ES-419.docx` | 40978 | `330610eedc9deab8c77829a3564b79f7a8401cb27f7c902f1a414d8ee5707752` |
| es-419 | `Manual_31_NYDFS_Part_500_Controlled_ES-419.pdf` | 68635 | `0d2b973c27c47ab27d77a2a9f6452a9a3ed29aa3f57b11ce4f6bc4ecae2d6d72` |
| pt-BR | `Manual_31_NYDFS_Part_500_Controlled_PT-BR.docx` | 40985 | `8c7026112e19a4cd6eb3aee2286e0f99538a7fe9412d32fc2d3dec44781356b3` |
| pt-BR | `Manual_31_NYDFS_Part_500_Controlled_PT-BR.pdf` | 68919 | `7df1da4dde791798c8e6ea66ec191572b9e30555e33b958c4eb96bf174d034de` |

## Deterministic QA on downloaded artifact

The artifact ZIP was downloaded directly from the successful workflow and inspected without regenerating any reviewed binary.

- Every binary SHA-256 and byte count matched `MANUAL_31_CANDIDATE_MANIFEST.json`.
- EN DOCX/PDF: 32 chapter markers; PDF 6 pages and searchable text.
- es-419 DOCX/PDF: 32 chapter markers; PDF 5 pages and searchable text.
- pt-BR DOCX/PDF: 32 chapter markers; PDF 5 pages and searchable text.
- DOCX accessibility audit: EN high=0, medium=0, low=0; es-419 high=0, medium=0, low=0; pt-BR high=0, medium=0, low=0.
- PDF preflight: all three PDFs openable, unencrypted, non-scanned, and without XFA.
- Rendered visual QA: all 16 PDF pages and all 15 locally rendered DOCX pages were inspected. No clipping, overlap, missing text, blank-content defect, or broken glyph was identified. DOCX renderer pagination may differ from the workflow-produced PDFs, but content/chapter completeness is intact.

## Source and release boundary

Release-time source verification on 2026-08-31 confirmed the current baseline remains 23 NYCRR Part 500 as amended by the Second Amendment effective November 1, 2023. The controlled package distinguishes binding regulation from DFS explanatory/advisory resources, organization practice, and legal determinations. Predecessor Manual 30 is published.

No deterministic defect requiring candidate regeneration was identified. These six binary identities are frozen for exact-byte staging. Publication state remains unchanged until durable staging, ordinary exact-head QA, and final catalog/work-product release reconciliation succeed.