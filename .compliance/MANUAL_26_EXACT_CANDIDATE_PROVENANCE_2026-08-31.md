# Manual 26 — Exact Candidate Provenance and Deterministic QA

## Candidate identity

- Manual: 26 — Incident Response & Cyber Crisis Management Controlled Implementation
- Candidate workflow run: `33391892785`
- Candidate artifact: `9757790333` (`manual26-six-binary-candidate`)
- Artifact digest: `sha256:b9242766f85c1e61df372d3b686cb3bf72e95c76989c9775770b4f837b8a1622`
- Candidate workflow head: `685b37f0e2fae845ec386c07417b579df0204a6d`
- Manifest source commit: `2f0381776040aba52a1f2fa25bde85797ffbbfe3`
- Publication state: unchanged until exact durable staging and final catalog/release-registry reconciliation.

## Exact six artifact identities

| Locale | Artifact | Bytes | SHA-256 |
|---|---|---:|---|
| en | `Manual_26_Incident_Response_Cyber_Crisis_Controlled_EN.docx` | 39510 | `bd5198b29e75a5b27555674452af97c17896315ae652578e7118c60afadabafa` |
| en | `Manual_26_Incident_Response_Cyber_Crisis_Controlled_EN.pdf` | 57833 | `3de26e8361dee87ed5594f1db1eb6a0df56b4e6081d511364039f90cde3184cc` |
| es-419 | `Manual_26_Incident_Response_Cyber_Crisis_Controlled_ES-419.docx` | 39791 | `eb9ff6773cbb06b883cdc71857c04f909c5202939eaeb12597978772deb69db7` |
| es-419 | `Manual_26_Incident_Response_Cyber_Crisis_Controlled_ES-419.pdf` | 69120 | `412a1597938dc28fc37ecb8e364399d6259cfa1586e9947ed04ade0c8bd36e18` |
| pt-BR | `Manual_26_Incident_Response_Cyber_Crisis_Controlled_PT-BR.docx` | 39794 | `5e0a7ca31d441e092deb6781ea2fbc02f43ca5c84a4cf0882bae1726e8914a0a` |
| pt-BR | `Manual_26_Incident_Response_Cyber_Crisis_Controlled_PT-BR.pdf` | 68686 | `6f57f7c9dd8ab7488ce45d197cbcb75e19185a588dfa9d444f1607211a09dceb` |

## Deterministic document/render checks

The exact downloaded candidate archive was re-extracted before final QA and all six SHA-256 identities were matched against the workflow manifest before review. Rendering was performed from isolated copies so the exact candidate bytes remained unchanged.

- Candidate Build: PASS.
- Workflow Security: PASS.
- Release Pipeline Meta QA: PASS.
- Release Package QA: PASS.
- Exact six SHA-256 identities matched workflow manifest: PASS.
- PDF preflight: EN/es-419/pt-BR are each 4 pages, openable, unencrypted, searchable/non-scanned, and non-XFA: PASS.
- DOCX package/accessibility audit: zero high-, medium-, or low-severity accessibility findings for EN, es-419, and pt-BR: PASS.
- Structural completeness: all 32 chapter markers present in each DOCX and PDF candidate: PASS.
- Full rendered-page inspection: all 24 pages across exact PDF renders and isolated DOCX renders were reviewed; no clipping, overlap, broken glyphs, missing sections, malformed headings, or unusable page output was identified: PASS.
- No deterministic defect requiring regeneration was identified.

These checks are deterministic technical evidence only and do not fabricate or replace any genuinely required unresolved human judgment. No specific unresolved non-deterministic substantive defect is currently documented for this exact candidate.

## Release handling

The six hashes above are the immutable candidate identities for durable staging. Any staging transaction must download workflow run `33391892785` / artifact `9757790333`, verify all six SHA-256 values fail closed, copy the exact bytes without regeneration, and preserve predecessor sequencing behind published Manual 25. Standing release authorization applies only after all applicable objective gates remain green and durable staging/provenance/catalog/release-registry reconciliation is complete.