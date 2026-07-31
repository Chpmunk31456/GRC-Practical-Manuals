# Legal and Citation Audit — Batch 04 (Chapters 71–79)

## Scope

This audit covers third-party and supply-chain risk chapters 71–79 of the English master.

## Controlling legal baseline

- Regulation (EU) 2024/1689, as amended.
- Regulation (EU) 2026/1744 where relevant.
- Current consolidated EUR-Lex text.
- Official European Commission and EU AI Office guidance, identified as non-binding unless the source itself has binding legal effect.

## Required legal corrections

### Chapter 71 — AI Vendor Due Diligence

- Distinguish statutory obligations of providers, deployers, importers, distributors, authorised representatives, and product manufacturers from recommended procurement controls.
- Require role, intended-purpose, high-risk, GPAI, transparency, prohibited-practice, and substantial-modification analysis.
- Require evidence supporting downstream access to technical documentation, instructions, logs, incident information, and conformity evidence where applicable.

### Chapter 72 — Contract Clauses

- Do not imply that contracts transfer statutory responsibility away from the legally regulated actor.
- Require clauses for information access, change notification, incident cooperation, audit evidence, prohibited-use restrictions, data and security controls, continuity, and exit.
- Separate mandatory legal obligations from negotiated risk allocation and indemnity.

### Chapter 73 — Provider Documentation Review

- Distinguish Annex IV technical documentation, Article 13 instructions for use, declarations, conformity evidence, registrations, model/system cards, and voluntary summaries.
- Require version and release linkage.
- Treat missing documentation as a release blocker where the deployer cannot meet its own obligations safely and lawfully.

### Chapter 74 — Model Cards, System Cards, and Limitations

- State clearly that model cards and system cards are supporting artifacts and do not automatically satisfy statutory documentation duties.
- Require limitations, intended purpose, prohibited and unsupported uses, performance boundaries, subgroup evidence, security constraints, and update history.

### Chapter 75 — Audit Rights and Incident Notification

- Align contractual notification windows with the fastest applicable statutory deadline.
- Require evidence preservation, regulator cooperation, causal-link analysis, affected-version identification, and supplemental reporting support.
- Avoid clauses that obstruct competent-authority access or statutory reporting.

### Chapter 76 — Cloud, API, and Model Dependency Risk

- Treat dependency concentration, provider change, model substitution, endpoint change, service-region change, and silent model update as legal and operational reassessment triggers.
- Require evidence of data location, subprocessor and supply-chain changes, logging availability, service continuity, and version transparency.

### Chapter 77 — Open-Source and Component Governance

- Do not treat open-source status as a blanket exclusion.
- Assess whether the specific obligations, exceptions, commercialisation conditions, downstream integration, GPAI treatment, cybersecurity, and substantial modification rules apply.
- Require provenance, licence, component, vulnerability, and maintainer evidence.

### Chapter 78 — Ongoing Vendor Monitoring

- Require monitoring of legal role, classifications, certifications, documentation, incidents, model changes, security posture, service performance, and regulatory actions.
- Link monitoring results to risk reassessment, corrective action, suspension, and exit.

### Chapter 79 — Exit, Portability, and Continuity Planning

- Require safe suspension, evidence export, log and documentation retention, migration validation, data return/deletion, affected-person protection, and regulatory continuity.
- Ensure termination does not destroy records needed for legal retention, incident investigation, conformity, or audit.

## Cross-chapter controls

1. Contract language must not be presented as changing statutory actor status by itself.
2. Every supplier record must identify the exact legal entity and role for each system, model, release, and jurisdiction.
3. Supplier evidence must be version-linked and dated.
4. Material supplier, model, service, purpose, geography, or control changes must trigger reassessment.
5. Procurement approval must be blocked where required evidence is absent or unresolved legal uncertainty remains.

## Closure criteria

This batch is not closed until Chapters 71–79 and the related vendor, contract, evidence, change, and exit appendices use the corrected legal distinctions and pass consistency review.