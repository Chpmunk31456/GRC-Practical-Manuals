# CIS Controls v8.1 Spanish — Exact-SHA Controlled Release Gate

## Exact candidate

- Repository: `Chpmunk31456/GRC-Practical-Manuals`
- Branch: `production/multilingual-grc-editions`
- Exact candidate SHA: `46235c5f80e13209b425758b293e5898abea7082`
- Parent validated build SHA: `5b1a4ccc05a1553006bb44a9401d3208c3386e5b`
- Pull request: `#3` — open, draft, unmerged

A comparison of the parent validated build SHA to the exact candidate SHA shows one added file only: `qa/release/CIS_SPANISH_OWNER_APPROVAL_2026-07-30.md`. No CIS Spanish source, DOCX, PDF, media, build script, or audit output changed between those SHAs.

## Automated gates

| Gate | Result |
|---|---|
| CIS Spanish configured corruption audit | PASS |
| Configured corruption findings | 0 |
| Missing expected numbered sections | 0 |
| Spanish Markdown present | PASS |
| Rebuilt Spanish DOCX present and non-empty | PASS |
| Rebuilt Spanish PDF present and non-empty | PASS |
| DOCX ZIP integrity during build | PASS |
| PDF searchable text during build | PASS |
| Multilingual package inventory | PASS — no missing deliverables |

## Owner acceptance

Repository owner Alberto (Al) Leiva approved continued processing of the controlled-review candidate on 30 July 2026. The approval is documented in `qa/release/CIS_SPANISH_OWNER_APPROVAL_2026-07-30.md`.

## Gate decision

**PASS for controlled-review use of the CIS Spanish candidate.**

This decision means the configured source-corruption, structure, rebuild, file-integrity, searchable-text, and inventory gates have passed and owner acceptance is documented.

## Residual limitations

The following are not independently certified by this gate:

- native-language editorial quality across every page;
- technical, legal, regulatory, and standards currency;
- page-by-page visual layout of every DOCX and PDF page;
- accessibility reading order, semantic tagging, metadata, and assistive-technology behavior;
- link validity and external-source currency;
- publication readiness of the other multilingual manuals in PR #3.

## Merge and publication rule

This CIS-specific controlled gate does not authorize merging or publishing PR #3. The broader pull request remains draft and unmerged until repository-wide gates are completed or the owner explicitly accepts the outstanding residual risks for the full repository candidate.
