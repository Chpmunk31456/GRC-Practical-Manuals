# Manual 18 — GLBA / FTC Safeguards Rule Preflight

**State:** downstream pre-stage only / not release-ready / not published  
**Series order:** 18  
**Preflight date:** 2026-08-30

## Purpose

Pre-stage the GLBA / FTC Safeguards Rule manual so source, applicability, architecture, localization, evidence, and publication controls are ready before Manual 18 becomes front-of-line. This file does not assert legal review, semantic review, release readiness, or publication.

## Authoritative-source targets

Build and release verification must prioritize primary U.S. government sources:

1. Gramm-Leach-Bliley Act statutory provisions and codified U.S. Code text applicable to financial institutions and safeguarding customer information.
2. Federal Trade Commission Safeguards Rule, 16 CFR Part 314, including current official regulatory text.
3. FTC official Safeguards Rule guidance, amendments, compliance resources, and effective-date notices.
4. Other federal financial regulator requirements only where their jurisdiction and covered-entity applicability are explicitly distinguished from FTC jurisdiction.

## Principal source and applicability risks

- Do not imply that every GLBA-covered entity is regulated by the FTC.
- Distinguish statute, regulation, regulator guidance, enforcement materials, and implementation practice.
- Track amendments and effective dates rather than treating historical Safeguards Rule text as current.
- Preserve institution-type and regulator-overlap boundaries.
- Do not represent operational guidance as legal advice or as an official regulator interpretation unless directly sourced.
- Do not imply that a control crosswalk establishes legal equivalence or certification.

## Controlled-build architecture target

Prepare a 32-chapter controlled English architecture covering:

- scope, definitions, institution/applicability analysis, and regulator boundaries;
- governance, qualified individual/accountability, risk assessment, safeguards design and maintenance;
- access control, authentication, encryption, secure development/change, logging/monitoring, testing, service-provider oversight, incident response and reporting dependencies;
- evidence architecture, exception/remediation management, reassessment triggers, management assurance and maturity paths;
- Essential / Structured / Enhanced implementation paths;
- scenario-based implementation and failure-mode training.

Each implementation chapter should carry: applicability -> objective -> owner -> procedure -> frequency -> evidence artifact -> evidence location -> reviewer/test method -> exception/remediation -> reassessment trigger.

## Localization architecture

Pre-stage es-419 and pt-BR terminology without claiming semantic approval. Preserve U.S.-law/regulator terms where translation could imply a different legal concept; include controlled-language glossaries and jurisdiction notes where needed.

## Publication preflight controls

Before publication, Manual 18 must independently satisfy:

- live authoritative-source and amendment/effective-date verification;
- controlled English completion;
- es-419 and pt-BR controlled localized drafts;
- legal/source-boundary and structural QA;
- terminology/cross-language parity QA;
- exact-head DOCX/PDF candidate generation;
- rendered page, accessibility, link, table, heading, language-metadata and visual QA;
- SHA-256 provenance and exact durable binary staging;
- workflow-security and dependency-lineage checks;
- catalog/release-registry/manifest reconciliation;
- predecessor publication clearance through Manual 17;
- no unresolved technical, integrity, source, packaging, or substantive defect.

Manual 18 must not publish ahead of Manual 17. Safe build and QA work may proceed in parallel under the rolling anti-halt rule.
