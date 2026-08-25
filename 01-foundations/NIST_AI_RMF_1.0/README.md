# Manual 03 — NIST AI Risk Management Framework Implementation

**Current controlled baseline:** NIST AI RMF 1.0 (NIST AI 100-1), published 26 January 2023

**Development status:** controlled build — English master and current-source verification complete; localization and publication QA pending

**Author and accountable human creator:** Alberto “Al” Leiva

[Main repository](../../README.md) | [GRC foundations](../README.md) | [AI-assistance disclosure](../../AI_ASSISTANCE_DISCLOSURE.md) | [Visual-learning standard](../../VISUAL_LEARNING_STANDARD.md)

## Important version notice

NIST AI RMF 1.0 remains the current published AI Risk Management Framework as of 25 August 2026, but NIST states that **AI RMF 1.0 is being updated and a revised version is in progress**. NIST also states that the AI RMF Playbook will be updated after the AI RMF 1.0 revision.

This manual therefore uses a fail-closed, version-aware publication model:

- current final material is identified by exact NIST publication/version;
- material known to be under revision is clearly marked;
- developing profiles and concept notes are not represented as current requirements;
- source-watch QA must detect baseline changes before release claims are made; and
- a future NIST revision will trigger impact analysis rather than silent replacement of the controlled baseline.

## Start here

1. Read [Manual 03 implementation paths](./MANUAL_03_IMPLEMENTATION_PATHS.md).
2. Establish an AI inventory and identify AI actors, lifecycle stages, affected parties, business context, and risk ownership.
3. Operationalize the four AI RMF Core functions — **GOVERN, MAP, MEASURE, and MANAGE** — as an integrated cycle rather than a checklist.
4. Add NIST AI 600-1 when generative AI is in scope.
5. Map AI RMF outcomes to existing governance, security, privacy, risk, quality, supplier, incident, and assurance processes rather than duplicating them.
6. Retain evidence showing decisions, tests, limitations, residual risk, approvals, monitoring, incidents, corrective actions, and reassessment.

## What this manual covers

- AI RMF purpose, voluntary-use boundary, scope, and organizational applicability;
- AI actors, lifecycle responsibilities, governance, accountability, and culture;
- practical implementation of GOVERN, MAP, MEASURE, and MANAGE;
- risk identification, context, impact, harm, opportunity, likelihood, severity, uncertainty, and prioritization;
- trustworthy-AI characteristics and tradeoffs without treating them as independent checkboxes;
- testing, evaluation, verification, and validation (TEVV);
- human oversight, affected-party considerations, feedback, complaints, incidents, and redress;
- data, model, software, infrastructure, cybersecurity, privacy, resilience, and third-party dependencies;
- generative-AI integration using NIST AI 600-1;
- metrics, monitoring, change control, residual-risk decisions, and continual improvement;
- practical evidence registers, manager decisions, analyst workpapers, and audit/assurance handoffs;
- integration with ISO/IEC 42001, the EU AI Act, NIST CSF 2.0, NIST Privacy Framework, and applicable sector obligations; and
- scalable implementation for micro/small, midsize, and large/complex organizations.

## Core implementation model

The AI RMF is not an ordered certification checklist. This manual treats the Core as an operating system for AI risk management:

- **GOVERN** establishes policies, responsibilities, culture, authority, risk tolerance, accountability, and oversight that cut across the other functions.
- **MAP** establishes context: intended purposes, actors, affected parties, dependencies, impacts, benefits, harms, assumptions, and boundaries.
- **MEASURE** evaluates risk and trustworthiness using appropriate qualitative and quantitative methods, TEVV, uncertainty analysis, and evidence.
- **MANAGE** prioritizes and treats risks, makes go/no-go or conditional decisions, monitors controls and residual risk, responds to incidents, and drives improvement.

## Evidence toolkit

The controlled branch includes reusable CSV records under `templates/`:

- `AI_SYSTEM_AND_USE_CASE_REGISTER.csv`
- `AI_RISK_AND_IMPACT_REGISTER.csv`
- `AI_CONTROL_AND_EVIDENCE_MATRIX.csv`
- `AI_DECISION_AND_APPROVAL_LOG.csv`
- `AI_MONITORING_AND_METRICS_REGISTER.csv`
- `AI_INCIDENT_CHANGE_AND_REASSESSMENT_LOG.csv`
- `AI_AUDIT_WORKPAPER_INDEX.csv`
- `MANUAL_03_EVIDENCE_CROSSWALK.csv`

These records support traceability and accountable decisions; completing them does not establish compliance, certification, trustworthy-AI achievement, control effectiveness, or an audit opinion.

## Generative AI boundary

NIST AI 600-1 is a final cross-sectoral profile and companion resource for AI RMF 1.0. Manual 03 uses it when generative AI is in scope while preserving a clear distinction between:

- general AI RMF outcomes and practices;
- additional or emphasized generative-AI risks and actions; and
- organization-specific legal, contractual, safety, security, privacy, sector, and product obligations.

## Controlled source identifiers

- `nist-ai-rmf-1-0` — NIST AI RMF 1.0; status `final-under-revision`
- `nist-ai-600-1` — NIST AI 600-1 Generative AI Profile; status `final`

Current-source verification evidence is recorded at `qa/manual03-source-verification/NIST_AI_RMF_MANUAL_03_SOURCE_VERIFICATION_2026-08-25.md`.

## Assurance boundary

Passing repository QA means that the controlled structure, official-source references, version state, accessibility, and evidence expectations are internally consistent. It does **not** mean that an organization complies with law, satisfies a regulator, has eliminated AI risk, has achieved certification, or has received an audit opinion.

NIST AI RMF is voluntary guidance. Organizations remain responsible for determining which laws, regulations, contracts, standards, policies, and risk decisions apply to their actual systems and contexts.

## Development roadmap

- [x] Establish Manual 03 on the released Manual 02 baseline.
- [x] Confirm through current official NIST sources that AI RMF 1.0 remains published while a revision is in progress.
- [x] Confirm NIST AI 600-1 as the published Generative AI Profile companion to AI RMF 1.0.
- [x] Establish the controlled Manual 03 baseline and dedicated fail-closed QA workflow.
- [x] Build Essential, Structured, and Enhanced implementation paths with accessible memory graphics.
- [x] Build the 32-chapter controlled English source across GOVERN, MAP, MEASURE, and MANAGE.
- [x] Build evidence templates, crosswalk, manager-decision records, monitoring records, change/reassessment records, and analyst workpaper index.
- [x] Reverify current official NIST source state for the 2026-08-25 candidate.
- [ ] Complete terminology, accessibility, copyright, and visual QA across the candidate package.
- [ ] Produce semantically localized Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) implementation entries and chapter-source drafts.
- [ ] Complete explicit human semantic-review approval for both localized editions.
- [ ] Generate accessible DOCX/PDF release candidates and complete document QA.
- [ ] Record Final Human Release Approval before merge/release.

## Official starting points

- NIST AI Risk Management Framework
- NIST AI RMF Playbook
- NIST Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1
- NIST Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile, NIST AI 600-1
- NIST AI Resource Center (AIRC)

Verify the current NIST publication state immediately before publication or release packaging.
