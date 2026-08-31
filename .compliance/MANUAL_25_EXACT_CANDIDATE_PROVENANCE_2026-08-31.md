# Manual 25 — Exact Candidate Provenance and Deterministic QA

## Candidate identity

- Manual: 25 — ISO 22301 Business Continuity Management Controlled Implementation
- Candidate workflow run: `33390353180`
- Candidate artifact: `9757204066` (`manual25-six-binary-candidate`)
- Artifact digest: `sha256:9f2f3e0775bab4d813f5c34f749bc33f570f1c3005b3fce5e7f86b800fc86342`
- Candidate workflow head: `b74add557e94dc7c985e9ff17fc24d747bed6160`
- Manifest source commit recorded by workflow: `387e0f270c9e314b1c32298dbc2752b4fef8f50e`
- Publication state: unchanged until exact durable staging and final catalog/release-registry reconciliation.

## Exact six artifact identities

| Locale | Artifact | Bytes | SHA-256 |
|---|---|---:|---|
| en | `Manual_25_ISO_22301_Controlled_EN.docx` | 39449 | `74f9ff06517466ba8d74f3774e1f6eeea0075b198a092fa1da83f11d9221f77c` |
| en | `Manual_25_ISO_22301_Controlled_EN.pdf` | 56039 | `9623dcaa191eba3ca803ebafbd34992975f0a2543b135558ecdbc10a0f0bec46` |
| es-419 | `Manual_25_ISO_22301_Controlled_ES-419.docx` | 39726 | `df448cdc7c09aed1f55f32dd8878dcf699a0173bfccd8d1c5c2e9f237d2250a9` |
| es-419 | `Manual_25_ISO_22301_Controlled_ES-419.pdf` | 68195 | `618111659d75c1e3a8c3c0d05c7897e8a4a3788a185495a54613d7f9632e4586` |
| pt-BR | `Manual_25_ISO_22301_Controlled_PT-BR.docx` | 39720 | `d5f754019672a42bed1d6090e7abc7e1d3d78067b5ef39c4bbe63f8f71294e22` |
| pt-BR | `Manual_25_ISO_22301_Controlled_PT-BR.pdf` | 67870 | `fd07431ca5366435c753a9fb02e93e600c87b07aee78acbdb05eab8bfa908e45` |

## Deterministic document/render checks

The exact downloaded candidate package was checked without regeneration.

- Candidate build workflow: PASS.
- Nonblank PDF preflight: PASS.
- Workflow Security: PASS.
- Release Pipeline Meta QA: PASS.
- Release Package QA: PASS.
- Exact artifact SHA-256 identities matched the workflow manifest for all six binaries: PASS.
- PDF page/render review: EN 3 pages; es-419 4 pages; pt-BR 4 pages. No identified clipping, overlap, broken glyphs, missing headings, or malformed output.
- DOCX page/render review: EN 4 pages; es-419 4 pages; pt-BR 4 pages. No identified clipping, overlap, broken glyphs, missing headings, or malformed output.
- PDF text extraction confirmed all 32 numbered chapter markers are present in EN, es-419, and pt-BR.
- DOCX XML extraction confirmed all 32 numbered chapter markers are present in EN, es-419, and pt-BR.
- DOCX accessibility audit reported zero high-, medium-, or low-severity findings for EN, es-419, and pt-BR.
- No deterministic defect was identified that requires candidate regeneration.

These checks are deterministic technical evidence only and do not fabricate or substitute for any genuinely required unresolved human judgment. No specific unresolved non-deterministic substantive issue is currently documented for this exact candidate.

## Source-state boundary

Release-time source revalidation is recorded in `05-operational-resilience/ISO_22301_Controlled_Implementation/qa/MANUAL_25_SOURCE_STATE_2026-08-31.md`: ISO 22301:2019 plus Amd 1:2024 remain the published requirements baseline; ISO/CD 22301 Edition 3 remains under-development change-watch; ISO 22313:2020 remains current published guidance; ISO/AWI 22313 Edition 3 remains under-development change-watch. Protected ISO normative text is not reproduced.

## Release handling

The six hashes above are the immutable candidate identities for durable staging. Any staging transaction must download workflow run `33390353180` / artifact `9757204066`, verify all six SHA-256 values fail closed, copy the exact bytes without regeneration, and preserve predecessor sequencing behind published Manual 24. Standing release authorization applies only after all applicable objective gates remain green and durable staging/provenance/catalog/release-registry reconciliation is complete.