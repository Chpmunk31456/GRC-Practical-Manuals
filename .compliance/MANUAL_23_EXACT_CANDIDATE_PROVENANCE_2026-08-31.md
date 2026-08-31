# Manual 23 — Exact Candidate Provenance and Deterministic QA

## Candidate identity

- Manual: 23 — DORA Controlled Implementation
- Candidate workflow run: `33382887620`
- Candidate artifact: `9754443202` (`manual23-six-binary-candidate`)
- Artifact digest: `sha256:79ac9dd39aa40e56988bf63d615dd75db432db0ba5a4ec47e696aad40e8dab28`
- Candidate workflow head: `625bd7f7d2e38185eef6887234faf1fe6adf2f2c`
- Manifest source commit recorded by workflow: `587e47d5afa346a881182ebf72beac6c4c013941`
- Publication state: unchanged until exact durable staging and final catalog/release-registry reconciliation.

## Exact six artifact identities

| Locale | Artifact | Bytes | SHA-256 |
|---|---|---:|---|
| en | `Manual_23_DORA_Controlled_EN.docx` | 40527 | `08ffb0a987cbdd5cad865fed168fdb8991594fb2afba3c01934de1a827c03ade` |
| en | `Manual_23_DORA_Controlled_EN.pdf` | 70446 | `b49509066b183ec6422b191ca900be437551e2a92d85b11975ee3866ac633d36` |
| es-419 | `Manual_23_DORA_Controlled_ES-419.docx` | 40589 | `1e5c158fa9dc86fa72f3bf9b433ee455b5a1625a38a4812d18623921d47c617d` |
| es-419 | `Manual_23_DORA_Controlled_ES-419.pdf` | 70836 | `56b06a2c3a931202ea02ce4b754eb678552192215a31f4842cabc77b59842ce6` |
| pt-BR | `Manual_23_DORA_Controlled_PT-BR.docx` | 40670 | `00e054b2254eda7be0be7a326b8b7f3df22930a872ef5d687d3bc3ab35277456` |
| pt-BR | `Manual_23_DORA_Controlled_PT-BR.pdf` | 71585 | `67ce7d40643c3288f7170fb6539763e016412065b7c731510245863e6bb1406c` |

## Deterministic document/render checks

The exact downloaded candidate package was checked without regeneration.

- Candidate build workflow: PASS.
- Nonblank PDF preflight: PASS.
- Workflow Security: PASS.
- Release Pipeline Meta QA: PASS.
- Release Package QA: PASS.
- PDF text extraction confirmed nonblank rendered content: EN 9757 characters; es-419 10115 characters; pt-BR 10284 characters.
- DOCX package validation confirmed a valid `word/document.xml` in all three DOCX files; extracted XML sizes were EN 16578, es-419 16930, pt-BR 17099 characters.
- No deterministic defect was identified that requires candidate regeneration.

These checks are deterministic technical evidence only and do not fabricate or substitute for any genuinely required unresolved human judgment. No specific unresolved non-deterministic substantive issue is currently documented for this exact candidate.

## Release handling

The six hashes above are the immutable candidate identities for durable staging. Any staging transaction must download workflow run `33382887620`, verify all six SHA-256 values fail closed, copy the exact bytes without regeneration, and preserve predecessor sequencing behind published Manual 22. Standing release authorization applies only after all applicable objective gates remain green and durable staging/provenance/catalog/release-registry reconciliation is complete.
