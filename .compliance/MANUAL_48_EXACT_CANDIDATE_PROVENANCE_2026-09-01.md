# Manual 48 — Exact Candidate Provenance and QA

**Manual:** Manual 48 — Singapore AI Governance: MGF, GenAI, AI Verify & Agentic AI  
**Frozen candidate workflow run:** `33541996729`  
**Frozen artifact ID:** `9814046725`  
**Artifact name:** `manual48-six-binary-candidate`  
**Artifact ZIP digest:** `sha256:61fea4a55fc4aee171088104ae2ee1d870824e8b0cdaf993f79931f8e1fa9ba7`  
**Controlled branch head:** `db607244b29c9d7c137d1d73a5e0bc7161846fb9`  
**Workflow test-merge/source commit recorded in manifest:** `ea4ca6279b26570e8096b7e1c8c6a6d773e50678`

## Immutable six-binary identities

- EN DOCX — `6cbde3b69a37e4220f41d41661e9e73b1b6bd2ce3f88a3119290f446f8f21857` — 46,914 bytes
- EN PDF — `2a0d6dd54435be259306fe71b78884fa80ef9ab67fd66f147507336eb2b43a84` — 268,762 bytes
- es-419 DOCX — `78639be77b77ab4c7d4083eb83c2dc1c1abe730c85797f71ce9222b1ec072b06` — 40,104 bytes
- es-419 PDF — `714f903a9c31bb358be97a07ec5150ee9903ac7e4b8f33eb8f3be4fdaf26e6f8` — 89,865 bytes
- pt-BR DOCX — `29062553b59dff1ad6d6958838cb5af6958754542c3119e911e385823abe68e0` — 40,082 bytes
- pt-BR PDF — `3c69d49ac910c754fc7541afdb2f3b3e44e891be46cca006d6eec75f5863c37f` — 91,101 bytes

## Independent verification

The exact workflow artifact was downloaded after the successful candidate run and extracted without regeneration. Independent `sha256sum` verification matched all six manifest identities byte-for-byte.

PDF structure inspection recorded:

- EN PDF — 15 pages, Letter, nonzero file size;
- es-419 PDF — 5 pages, Letter, nonzero file size;
- pt-BR PDF — 5 pages, Letter, nonzero file size.

All 25 PDF pages were raster-rendered for verification. Automated non-white-content checks found no blank page. Visual inspection of the first rendered page for EN, es-419 and pt-BR confirmed visible readable text, expected headings and no obvious clipping, overlap or broken glyph blocks on those inspected pages. The workflow's PDF content preflight independently passed all three PDFs.

## Objective GitHub gates

The exact Stage-4 head passed:

- Manual Structure QA;
- Trilingual Publication Parity;
- Workflow Security;
- Release Pipeline Meta QA;
- Release Package QA; and
- dedicated Manual 48 Candidate Build.

Controlled Stage-4 build was then merged to `main` through PR #493 without modifying the candidate bytes.

## Retained substantive-review boundary

Objective build, provenance and rendered-document checks do not replace genuine-human substantive judgment. Before final publication, retain and evidence any repository-required human technical/governance review, es-419 and pt-BR semantic review, accessibility/visual review, source-mapping review or changed-scope reconciliation applicable to this exact candidate. Do not fabricate those records.

Standing final release authorization applies automatically after retained genuine-human substantive review evidence is actually present and all exact-head objective gates remain green.