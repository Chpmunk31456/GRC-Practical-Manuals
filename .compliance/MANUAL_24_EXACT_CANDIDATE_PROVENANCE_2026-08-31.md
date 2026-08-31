# Manual 24 — Exact Candidate Provenance and Deterministic QA

## Candidate identity

- Manual: 24 — NIS2 Controlled Implementation
- Candidate workflow run: `33386933300`
- Candidate artifact: `9755945218` (`manual24-six-binary-candidate`)
- Artifact digest: `sha256:b71c5087324fbf8c192d1cc709d5beed8695014ad24b3b0afcff0f57aa5e9f32`
- Candidate workflow head: `fd22bff52e8c31a7733843273c6676f0cd290052`
- Manifest source commit recorded by workflow: `e8cb6a09e8d9334e8b2de43facc1b94faad903da`
- Publication state: unchanged until exact durable staging and final catalog/release-registry reconciliation.

## Exact six artifact identities

| Locale | Artifact | Bytes | SHA-256 |
|---|---|---:|---|
| en | `Manual_24_NIS2_Controlled_EN.docx` | 43939 | `5cd618a0ef6fd2e14b2ca5af9ee87d6f87eb70085f543ae7108719f44038e222` |
| en | `Manual_24_NIS2_Controlled_EN.pdf` | 90296 | `b6e64f9058dd7f673942f0efc60498f252f3f36e1816454024fceeac94f178e9` |
| es-419 | `Manual_24_NIS2_Controlled_ES-419.docx` | 44541 | `d6cce898c4606a27dc7bc500b667568f5d3336becc9a050a9e2cf9bbb45fda66` |
| es-419 | `Manual_24_NIS2_Controlled_ES-419.pdf` | 94318 | `b2fe9222b79750f4a3dabf69292184a4cd5f4008980514947b40616d0ae6667c` |
| pt-BR | `Manual_24_NIS2_Controlled_PT-BR.docx` | 44577 | `185783033f3880c5f1654e6342632f7c2bbeb924438efddd252c7129ad606631` |
| pt-BR | `Manual_24_NIS2_Controlled_PT-BR.pdf` | 94683 | `4ffc1eb318ad1d9c399036828fbf5c46691659a84c1b2817ef51a511604a1a8e` |

## Deterministic document/render checks

The exact downloaded candidate package was checked without regeneration.

- Candidate build workflow: PASS.
- Nonblank PDF preflight: PASS.
- Workflow Security: PASS.
- Release Pipeline Meta QA: PASS.
- Release Package QA: PASS.
- Exact artifact SHA-256 identities matched the workflow manifest for all six binaries: PASS.
- PDF preflight confirmed all three PDFs are openable, unencrypted, non-scanned documents: EN 8 pages; es-419 9 pages; pt-BR 9 pages.
- PDF text extraction confirmed nonblank rendered content: EN 22481 characters; es-419 26449 characters; pt-BR 26619 characters.
- DOCX package validation confirmed valid `word/document.xml` in all three DOCX files; extracted XML sizes were EN 31625, es-419 35588, pt-BR 35758 bytes.
- DOCX accessibility audit reported zero high-, medium-, or low-severity findings for EN, es-419, and pt-BR.
- Full-page DOCX and PDF render review confirmed no identified clipping, overlap, broken glyphs, missing headings, or malformed page output across EN, es-419, and pt-BR.
- No deterministic defect was identified that requires candidate regeneration.

These checks are deterministic technical evidence only and do not fabricate or substitute for any genuinely required unresolved human judgment. No specific unresolved non-deterministic substantive issue is currently documented for this exact candidate.

## Release handling

The six hashes above are the immutable candidate identities for durable staging. Any staging transaction must download workflow run `33386933300` / artifact `9755945218`, verify all six SHA-256 values fail closed, copy the exact bytes without regeneration, and preserve predecessor sequencing behind published Manual 23. Standing release authorization applies only after all applicable objective gates remain green and durable staging/provenance/catalog/release-registry reconciliation is complete.