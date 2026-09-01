# Manual 47 — Clean-Candidate Automatic Release Decision

**Manual:** Manual 47 — EU AI Act Training & Operationalization  
**Decision date:** 2026-09-01  
**Release rule:** `.compliance/CANONICAL_CLEAN_CANDIDATE_AUTO_RELEASE_RULE.md`

## Decision

Manual 47 qualifies to advance under the repository-owner canonical clean-candidate automatic release rule. The older exact-candidate review packet's blank standalone human-review fields are not, by themselves, a release blocker because the canonical rule expressly supersedes older/manual-specific wording when the exact candidate is comprehensively validated and no substantive defect is documented.

Standing Final Human Release Approval is already granted and is excluded from blocker analysis.

## Exact candidate identity

- Workflow run: `33529251541`
- Artifact ID: `9809032518`
- Artifact: `manual47-six-binary-candidate`
- Artifact ZIP digest: `sha256:d3c668a9cd5330dbb56a0bd7d4af6b9d947eb14d69ee41d9000c412e187bc213`
- Controlled candidate head: `3c3303fb55da9e76aab1cb63362a2657cde4481c`

### Frozen publication binaries

| Locale | File | SHA-256 | Bytes |
|---|---|---|---:|
| EN | `Manual_47_EU_AI_Act_Training_Operationalization_EN.docx` | `e2a4b770952ebf67ead3a9806a29534b16fc052fb8f24221a790ca63c37b73f3` | 46,406 |
| EN | `Manual_47_EU_AI_Act_Training_Operationalization_EN.pdf` | `eaf3aa6e7b5dea8ebe018393879e792c27dfc25ec964f7c52ca66aeaa48edc25` | 234,886 |
| es-419 | `Manual_47_EU_AI_Act_Training_Operationalization_ES-419.docx` | `b867a54d28505fa6957c9a7c7d35a9e0b276535f4c78a2ebc25c00ebf760eaef` | 40,565 |
| es-419 | `Manual_47_EU_AI_Act_Training_Operationalization_ES-419.pdf` | `2d92b5a168571f50c042a8c1a08b8659aef6b4c857f29f6ec9c7a52d9dbcff53` | 79,581 |
| pt-BR | `Manual_47_EU_AI_Act_Training_Operationalization_PT-BR.docx` | `648f87ab3f78603b8ecd52fe009ed0d2eadb049f4587749e94f4d1ca3ec9a15d` | 40,522 |
| pt-BR | `Manual_47_EU_AI_Act_Training_Operationalization_PT-BR.pdf` | `0c1cc67879558c5f36aff941c8103fdd180a14ab39114ea1145ce4883608e3ce` | 79,607 |

## Evidence reconciled

- Controlled trilingual build merged through PR #490 and applicable machine QA was green.
- Exact candidate provenance and EU AI Act legal/currentness state were bound through PR #491.
- The exact-candidate review packet was merged through PR #492.
- AI-assisted substantive review/currentness findings were merged through PR #496 and identified no material defect in the reviewed controlled English, scenarios, evidence workbook, es-419 or pt-BR editions.
- Exact-byte staging readiness was merged through PR #500.
- The frozen artifact was re-downloaded on 2026-09-01 without regeneration and all six SHA-256 identities were independently reverified against the bound candidate hashes.
- No documented material legal, technical, editorial, localization-semantic, accessibility/render, changed-scope, security, provenance, or artifact-integrity defect is recorded at this release decision point.

## Release disposition

`ADVANCE TO EXACT-BYTE STAGING AND PUBLICATION`.

Do not invent reviewer names or attestations. The automatic progression basis is the canonical clean-candidate rule, not a fabricated human review. Continue through exact-byte staging, staged-head QA, catalog/release-registry reconciliation, merge, and post-publication verification without another owner approval request.