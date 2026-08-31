# Manual 19 — Exact Candidate Provenance and Deterministic QA

Date: 2026-08-31
Manual: 19 — FedRAMP / FISMA Controlled Implementation
Publication state: candidate; not yet published by this record

## Exact candidate build

- Candidate PR head: `cc09d80206ddcccd9e061dce8a4fc27d90e667c7`
- Candidate workflow: `19 - Manual 19 Candidate Build`
- Workflow run: `33366244377`
- Artifact ID: `9748385723`
- Artifact name: `manual19-six-binary-candidate`
- Artifact digest: `sha256:79b6718596eb218f1762ab07999e4978f2732cc7c5774a47c03051aafdcb543c`
- Candidate manifest source_commit recorded by the pull-request workflow merge ref: `3965fec98f374b7510d6681c7ec0e0b91d962bae`
- Dedicated candidate workflow, Workflow Security, Release Pipeline Meta QA, and Release Package QA completed successfully on the candidate PR.

## Exact six artifact identities

| Locale | Artifact | SHA-256 | Bytes |
|---|---|---|---:|
| en | `Manual_19_FedRAMP_FISMA_Controlled_EN.docx` | `8be565e36f5b5111aebe3954bf6a80f0bedc51d099575d80c0262ed520a04b0a` | 41094 |
| en | `Manual_19_FedRAMP_FISMA_Controlled_EN.pdf` | `30c873924814994d5ce0c96aa0d8d0433715a50d9dcd37701b5ff3b3e0bd8ed4` | 73984 |
| es-419 | `Manual_19_FedRAMP_FISMA_Controlled_ES-419.docx` | `026f15c21c3441be9688a314d22a0c7d3937f51ba4b7a10d5e22ce35bf33539e` | 41505 |
| es-419 | `Manual_19_FedRAMP_FISMA_Controlled_ES-419.pdf` | `639b039e2d918625fb3acff416ad0e2bcdc28573a8a959118c73f3bd5b78e7b4` | 77145 |
| pt-BR | `Manual_19_FedRAMP_FISMA_Controlled_PT-BR.docx` | `384480e1a212519b50dfe615fa4e87b1a01d9481288e680959e1a1aedbf7a6f3` | 41517 |
| pt-BR | `Manual_19_FedRAMP_FISMA_Controlled_PT-BR.pdf` | `43cacc4bcc1fe0883b9d2c9c8c6a777dd91dab3a1f795f43b16738418736cda6` | 77817 |

## Deterministic document and rendered QA

The exact downloaded artifact package was re-hash bound to the manifest above and subjected to deterministic document/rendered preflight without modifying the candidate bytes.

- All three PDFs open successfully, are unencrypted, are non-scanned/searchable, have no XFA, and contain 5 pages each.
- All three PDFs were rendered page-by-page at 160 DPI. Visual inspection found no clipping, overlap, malformed page break, broken glyph, unreadable text, or blank-page defect.
- All three DOCX candidates were independently rendered to page images and produced 5 pages each without a rendering failure.
- DOCX accessibility audit results: EN high=0 / medium=0 / low=0; es-419 high=0 / medium=0 / low=0; pt-BR high=0 / medium=0 / low=0.
- No deterministic defect requiring source or binary regeneration was identified.

## Release boundary

The es-419 and pt-BR source-localization release wording was corrected through PR #318 so that unofficial-translation status is preserved without creating a routine generic human-review gate. A genuine human judgment remains fail-closed only if a specific documented non-deterministic substantive question actually exists. Otherwise the repository canonical release rule applies.

This provenance record does not claim FedRAMP authorization, certification, FISMA attestation, an independent assessor conclusion, legal advice, or any human review that did not occur. Durable repository staging of these exact six bytes remains the next publication-control transaction. Once exact durable staging, applicable exact-head gates, predecessor state, and final catalog/release-registry reconciliation are green with no unresolved issue or error, standing release authorization requires publication without a separate generic approval step.
