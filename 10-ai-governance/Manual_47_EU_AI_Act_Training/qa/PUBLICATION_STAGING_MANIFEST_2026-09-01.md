# Manual 47 — Publication Staging Manifest

Status: ACTIVE PUBLICATION STAGING
Date: 2026-09-01

This branch is the publication branch for Manual 47 — EU AI Act Training & Operationalization.

## Exact candidate identity

- Candidate workflow run: `33529251541`
- Artifact ID: `9809032518`
- Artifact name: `manual47-six-binary-candidate`
- Artifact digest: `sha256:d3c668a9cd5330dbb56a0bd7d4af6b9d947eb14d69ee41d9000c412e187bc213`
- Controlled candidate head: `3c3303fb55da9e76aab1cb63362a2657cde4481c`
- Clean-candidate release decision merged by PR #503 to main at `cb800fdb63ec2dad81b6127ca5e2b8f7b5d58a14`.

## Frozen publication binaries

| Language | Format | SHA-256 | Bytes |
|---|---|---|---:|
| EN | DOCX | `e2a4b770952ebf67ead3a9806a29534b16fc052fb8f24221a790ca63c37b73f3` | 46,406 |
| EN | PDF | `eaf3aa6e7b5dea8ebe018393879e792c27dfc25ec964f7c52ca66aeaa48edc25` | 234,886 |
| es-419 | DOCX | `b867a54d28505fa6957c9a7c7d35a9e0b276535f4c78a2ebc25c00ebf760eaef` | 40,565 |
| es-419 | PDF | `2d92b5a168571f50c042a8c1a08b8659aef6b4c857f29f6ec9c7a52d9dbcff53` | 79,581 |
| pt-BR | DOCX | `648f87ab3f78603b8ecd52fe009ed0d2eadb049f4587749e94f4d1ca3ec9a15d` | 40,522 |
| pt-BR | PDF | `0c1cc67879558c5f36aff941c8103fdd180a14ab39114ea1145ce4883608e3ce` | 79,607 |

## Publication sequence

1. Stage the six frozen exact binaries without regeneration.
2. Run exact staged-head QA and workflow-security/package checks.
3. Reconcile `.compliance/manual-catalog.json` to `published` for Manual 47.
4. Reconcile `.compliance/work-product-releases.json` with exact artifact provenance.
5. Merge publication PR to `main` only after exact-head checks are green.
6. Verify the six binaries plus catalog and release registry from `main`.
7. Immediately advance Manual 48 through the same clean-candidate publication sequence.

The repository-owner standing Final Human Release Approval remains active. Missing standalone review paperwork alone is not a blocker under `.compliance/CANONICAL_CLEAN_CANDIDATE_AUTO_RELEASE_RULE.md`. No human reviewer is fabricated by this record.
