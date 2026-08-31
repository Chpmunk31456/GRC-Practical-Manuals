# Manual 20 — Exact Candidate Provenance and Deterministic QA

Manual: 20 — CIS Controls v8.1 Controlled Implementation

Candidate workflow run: `33367617544`
Candidate artifact: `9748837052` (`manual20-six-binary-candidate`)
Candidate head: `fe199355f0d5a4027f3601fd37eb6b9e93e6daed`
Artifact digest: `sha256:963e9e39fbebe354fad4a3d3452dc3fe0163f561e50edb57bacf8d68e2b9429c`
Frozen English source blob: `d257e418e8839fe8694ca943760c65e43c7e1644`

## Exact six publication artifacts

- EN DOCX — `c7b1981e0849f2153812129d4b304d6009d7a08bc4c98844b3fef63e9662789f` — 40,262 bytes
- EN PDF — `ade9df0a2a42b2a01ccfa514f3f8ccac8b5ab1c6dafa1997b9a11bf801a675ca` — 68,793 bytes
- es-419 DOCX — `775ead3373fd89f972ed93ff0e2eacd458d4e3d205d6a201aa9eda5dcf230482` — 40,701 bytes
- es-419 PDF — `472620add4a3943a7c1bb9f18cba8ee7869af9523a4e5fc3157fa4fe439f33de` — 72,680 bytes
- pt-BR DOCX — `6c7e88a9c7af6e161407782350b097380a40dd495970c4509a29548b62b97293` — 40,687 bytes
- pt-BR PDF — `c7e3151a9e660ff11f1ea73ccb211d899b9c939e1e628acf896ffdef4175de0c` — 73,383 bytes

Candidate manifest SHA-256: `b4ee3d069e380ad90c1ba40503853616445e355e8470cf5ad00da7c2c5d393c4`.

## Deterministic QA

Exact-head candidate-stage checks passed: Manual 20 Candidate Build, Workflow Security, Release Pipeline Meta QA, and Release Package QA.

The exact candidate package was independently downloaded and re-hashed. All six artifact identities and sizes matched the candidate package. Each PDF was rendered page-by-page at 160 DPI and visually inspected. EN rendered as 4 pages; es-419 and pt-BR rendered as 5 pages each. No clipping, overlap, broken glyphs, malformed page breaks, or unreadable content was identified. Each DOCX was independently rendered page-by-page and checked for layout defects. DOCX accessibility audit results were high=0, medium=0, low=0 for EN, es-419, and pt-BR.

No deterministic source, localization, document, rendering, accessibility, integrity, packaging, provenance, or workflow-security defect requiring candidate regeneration was identified.

## Release interpretation

The project translations remain explicitly unofficial. CIS Controls, Safeguards, Implementation Groups, CIS Benchmarks, crosswalks, organization-specific procedures, and assessment judgment remain distinct. No CIS certification or endorsement is implied.

Under the repository-wide canonical rule, no separate routine human approval is required for an otherwise clean candidate. Any genuinely non-deterministic specialist judgment remains required only when a specific documented substantive issue actually calls for it. No such unresolved issue is presently identified for this candidate.

Next transaction: durably stage these exact six bytes without regeneration, re-run applicable exact-head release gates, then reconcile publication state because predecessor Manual 19 is published.
