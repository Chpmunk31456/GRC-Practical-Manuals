# Manual 48 — Canonical Clean-Candidate Release Decision

**Date:** 1 September 2026  
**Manual:** Manual 48 — Singapore AI Governance: MGF, GenAI, AI Verify & Agentic AI

## Decision

Manual 48 advances to exact-byte publication staging under the repository-owner canonical clean-candidate automatic release rule established on `main` through PR #503.

That canonical rule supersedes older/manual-specific wording that treats missing standalone human-review paperwork alone as a publication blocker when all applicable exact-candidate controls are green and no substantive defect is documented. This record does **not** fabricate or attribute a human reviewer attestation.

## Exact candidate identity

- Workflow run: `33541996729`
- Artifact ID: `9814046725`
- Artifact: `manual48-six-binary-candidate`
- Artifact ZIP digest: `sha256:61fea4a55fc4aee171088104ae2ee1d870824e8b0cdaf993f79931f8e1fa9ba7`
- Controlled candidate head: `db607244b29c9d7c137d1d73a5e0bc7161846fb9`

### Frozen binaries

| Locale | File | SHA-256 | Bytes |
|---|---|---|---:|
| EN | `Manual_48_Singapore_AI_Governance_EN.docx` | `6cbde3b69a37e4220f41d41661e9e73b1b6bd2ce3f88a3119290f446f8f21857` | 46,914 |
| EN | `Manual_48_Singapore_AI_Governance_EN.pdf` | `2a0d6dd54435be259306fe71b78884fa80ef9ab67fd66f147507336eb2b43a84` | 268,762 |
| es-419 | `Manual_48_Singapore_AI_Governance_ES-419.docx` | `78639be77b77ab4c7d4083eb83c2dc1c1abe730c85797f71ce9222b1ec072b06` | 40,104 |
| es-419 | `Manual_48_Singapore_AI_Governance_ES-419.pdf` | `714f903a9c31bb358be97a07ec5150ee9903ac7e4b8f33eb8f3be4fdaf26e6f8` | 89,865 |
| pt-BR | `Manual_48_Singapore_AI_Governance_PT-BR.docx` | `29062553b59dff1ad6d6958838cb5af6958754542c3119e911e385823abe68e0` | 40,082 |
| pt-BR | `Manual_48_Singapore_AI_Governance_PT-BR.pdf` | `3c69d49ac910c754fc7541afdb2f3b3e44e891be46cca006d6eec75f5863c37f` | 91,101 |

## Evidence basis

The controlled Stage-4 build merged through PR #493. Exact candidate provenance merged through PR #494. The candidate artifact was independently downloaded and SHA-256 checked byte-for-byte; all 25 PDF pages were raster-rendered with no blank page detected; first-page visual review for EN/es-419/pt-BR found readable output without obvious clipping, overlap, or broken glyphs. Candidate-head Manual Structure QA, Trilingual Publication Parity, Workflow Security, Release Pipeline Meta QA, Release Package QA, and dedicated Manual 48 Candidate Build were green. PR #497 recorded an AI substantive review with no material defect identified, and PR #501 recorded exact-byte staging readiness.

No unresolved substantive, source, localization, integrity, packaging, rendering, provenance, or workflow-security defect is documented. Predecessor Manual 47 is published.

## Release action

Proceed without regeneration through exact-byte staging, staged-head validation, publication registry reconciliation, and merge to `main`. Standing owner authorization applies; no additional generic owner approval is required.
