# Manual 46 — AI Governance Training — Controlled Build Gate

Date: 2026-09-01
Status: BUILD ACTIVE / NOT PUBLISHED
Branch: `build/manual46-ai-governance-training`

## Objective

Begin the Manual 46+ AI-governance training series without weakening the repository's publication, source, localization, security, provenance, accessibility, or artifact-integrity controls.

## Manual 46 scope

Manual 46 is the foundational **Enterprise AI Governance Training** manual. It is designed for practitioner learning and senior-manager/interview preparation while remaining implementation-oriented.

Core framework coverage:

- EU AI Act
- ISO/IEC 42001
- ISO/IEC 23894
- NIST AI RMF 1.0
- NIST AI 600-1 Generative AI Profile
- Singapore AI governance frameworks, including agentic-AI governance
- ISO/IEC 27001 integration
- privacy and data governance
- responsible AI
- GenAI/RAG/vector-database governance
- agentic AI
- third-party AI
- AI assurance, monitoring, incident, change, and evidence governance

## Fail-closed build rules

1. Regulatory and standards claims must be source-verified before controlled-English freeze.
2. Do not reproduce copyrighted standards text beyond permitted use; teach implementation through original explanation and properly scoped references.
3. Distinguish binding law, standards, voluntary frameworks, regulator guidance, and recommended practices.
4. Date-sensitive legal claims require explicit source-state verification.
5. Do not fabricate human-review evidence.
6. Deterministic defects are repaired automatically and affected QA rerun.
7. Stable publication candidates are not regenerated without a material reason.
8. EN/es-419/pt-BR parity is required before publication.
9. Rendered DOCX/PDF artifacts require visual/document/accessibility QA before publication.
10. Checksums, provenance, manifest integrity, workflow security, durable artifacts, predecessor state, and release reconciliation remain mandatory.

## Build sequence

1. Curriculum architecture — STARTED
2. Authoritative source-state verification — NEXT
3. Controlled English content build
4. Source/citation and terminology QA
5. Controlled-English freeze
6. es-419 localization
7. pt-BR localization
8. Localization parity QA
9. DOCX/PDF generation
10. Rendered/document/accessibility QA
11. Exact candidate provenance and checksums
12. Workflow-security/release-package QA
13. Durable artifact staging
14. Sequential publication reconciliation

## Initial quality objective

The training manual must teach learners to answer five questions for every AI use case:

1. What is the system and what decision/action does it influence?
2. Who owns it and what role does the organization play?
3. What laws, standards, contractual obligations, and internal policies apply?
4. What risks and controls must be demonstrated before and after deployment?
5. What evidence proves the governance process actually operated?

This gate records build initiation only. It does not represent publication eligibility.