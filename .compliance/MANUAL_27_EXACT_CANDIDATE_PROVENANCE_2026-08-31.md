# Manual 27 — Exact Candidate Provenance and Deterministic QA

## Candidate identity

- Manual: 27 — Data Governance & Privacy Engineering Controlled Implementation
- Candidate workflow run: `33395518151`
- Candidate artifact: `9759165368` (`manual27-six-binary-candidate`)
- Artifact digest: `sha256:89bc8bd17f6d120590165713e96abc2814dca456d6f306c79a5ac4107ce5cbe9`
- Candidate PR head: `191237d37a697f4c2791b3212d91135d0df696a8`
- Candidate workflow manifest source commit: `b10e21dc3754d2e67e44d01bdf55cb11a773bcc9`
- Candidate build transaction merged through PR #371 at `98e42a0518420a1bf50fd1755c0783aff26f5862`.
- Publication state remains unchanged until exact durable staging and final catalog/release-registry reconciliation.

## Exact six artifact identities

| Locale | Artifact | Bytes | SHA-256 |
|---|---|---:|---|
| en | `Manual_27_Data_Governance_Privacy_Engineering_Controlled_EN.docx` | 39216 | `209d494e8af35c414f431a7cbed17b994dd2e5fadcd1fa3866fa89df67cf41f1` |
| en | `Manual_27_Data_Governance_Privacy_Engineering_Controlled_EN.pdf` | 65274 | `be0df850f2aec17aad520fe0a20fb6aef0ec7bb2de063f11d215b943419c88c0` |
| es-419 | `Manual_27_Data_Governance_Privacy_Engineering_Controlled_ES-419.docx` | 39443 | `a83679c60ad6d54e795b98e3058e7bba453b23cc99a7b997a32665d3f8f48abf` |
| es-419 | `Manual_27_Data_Governance_Privacy_Engineering_Controlled_ES-419.pdf` | 67030 | `9fdb609b0917f841013e369a422865b2b6ab44e8e7e26385c2933932cdc2dd93` |
| pt-BR | `Manual_27_Data_Governance_Privacy_Engineering_Controlled_PT-BR.docx` | 39484 | `266125f144dba620c9017424b282e552f46b794e9cfb7708a7e110111f819f9f` |
| pt-BR | `Manual_27_Data_Governance_Privacy_Engineering_Controlled_PT-BR.pdf` | 67637 | `df4dc0c3a2e9d69848649f568766e852bbdbe4ca93d282d9f56227cf391b0126` |

## Deterministic document/render checks

The exact downloaded artifact was inspected without regeneration.

- Candidate Build: PASS.
- Workflow Security: PASS.
- Release Pipeline Meta QA: PASS.
- Release Package QA / release-readiness: PASS.
- Exact SHA-256 identities matched the workflow manifest for all six binaries: PASS.
- PDF preflight: all three PDFs openable, unencrypted, non-scanned/searchable, 4 pages each: PASS.
- Chapter completeness: all three PDFs and all three DOCX files contain chapter markers 01 through 32 exactly as required: PASS.
- DOCX package validation: valid `word/document.xml` in all three files: PASS.
- DOCX accessibility audit: EN 0 high / 0 medium / 0 low; es-419 0 / 0 / 0; pt-BR 0 / 0 / 0: PASS.
- Full rendered page review: all 12 PDF pages and all 12 DOCX-rendered pages inspected; no identified clipping, overlap, broken glyphs, missing chapters, or malformed page output: PASS.
- No deterministic defect requiring candidate regeneration was identified.

These checks are deterministic technical evidence. They do not fabricate or substitute for any genuinely required unresolved human judgment. No specific unresolved material substantive defect is currently documented for this exact candidate.

## Release handling

These six hashes are the immutable Manual 27 candidate identities. Durable staging must retrieve workflow run `33395518151` / artifact `9759165368`, fail closed unless all six SHA-256 identities match, copy the exact bytes without regeneration into the Manual 27 publication tree, preserve published Manual 26 as predecessor, and submit the exact staged head to normal repository QA. Final publication requires catalog and work-product release-registry reconciliation after the exact staged head remains green.