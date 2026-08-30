# Manual 16 — ISO/IEC 27001 / 27002 Authoritative Preflight Baseline

Status: downstream preflight only; not publication authorization.

## Authoritative baseline

- ISO/IEC 27001:2022 is the current published third edition of the Information Security Management Systems requirements standard.
- ISO/IEC 27001:2022/Amd 1:2024 is a published amendment applying to ISO/IEC 27001:2022 and must be treated as part of the current release-time baseline.
- ISO/IEC 27002:2022 is the current published third edition providing information-security control guidance; it is guidance rather than a certifiable requirements standard.
- Release-time re-verification against official ISO pages is mandatory before promotion to release candidate.

Official ISO metadata sources:
- https://www.iso.org/standard/27001
- https://www.iso.org/standard/88435.html
- https://www.iso.org/standard/75652.html

## Copyright and standards-use boundary

Manual 16 must not reproduce copyrighted ISO/IEC standard text, tables, clauses, Annex A control text, or proprietary explanatory content beyond what is legally permitted. The manual may use official ISO metadata, public summaries, original implementation guidance, original control/evidence structures, and references to clause/control identifiers where appropriate.

Do not present this manual as an ISO-authorized translation, substitute for the standards, certification decision, or legal/compliance guarantee. Users requiring normative wording must obtain the applicable ISO/IEC publications from an authorized source.

## Scope boundary

The controlled manual must distinguish:
- ISO/IEC 27001 requirements from ISO/IEC 27002 implementation guidance;
- ISMS management-system requirements from individual security controls;
- certification/audit activities from implementation guidance;
- Annex A/control selection from claims that every control is mandatory in every context;
- risk treatment and Statement of Applicability decisions from generic cybersecurity checklists;
- ISO/IEC requirements from NIST, CIS, COBIT, PCI DSS, SOC 2, legal/regulatory, or customer-contract requirements unless a crosswalk is explicitly labeled as non-normative guidance.

## Controlled architecture

Pre-stage content around:
1. ISMS context, interested parties, scope, governance and leadership.
2. Information-security risk assessment and risk treatment.
3. Information-security objectives, planning and documented information.
4. Resources, competence, awareness and communications.
5. Operational planning and control.
6. Performance evaluation, monitoring, measurement, internal audit and management review.
7. Nonconformity, corrective action and continual improvement.
8. Statement of Applicability governance and control-selection rationale.
9. ISO/IEC 27002 control-guidance usage without reproducing normative/copyrighted text.
10. Evidence design, ownership, operating frequency and auditability.
11. Supplier, cloud, identity, cryptography, logging, incident, resilience and secure-development implementation patterns mapped through original guidance.
12. Climate-action amendment applicability/context checks from ISO/IEC 27001:2022/Amd 1:2024 without reproducing copyrighted amendment text.
13. Essential / Structured / Enhanced implementation paths.
14. Scenario exercises, evidence examples, maturity checks and practitioner assessment questions.

## Localization architecture

- English is the controlled source language for this manual.
- es-419 and pt-BR editions must be translated from the controlled English manual, not copied from copyrighted ISO text.
- Human semantic review is required for each localized edition, including management-system terminology, risk-treatment language, audit terminology, captions, figures, tables and cross-references.
- No locale may claim to be an official or authorized ISO translation unless demonstrable authorization exists.

## Fail-closed release gates

Before publication require:
- release-time ISO edition/amendment status verification;
- competent ISO/IEC 27001/27002 technical and management-system review;
- copyright/editorial boundary review;
- es-419 semantic review tied to exact candidate/artifact hashes;
- pt-BR semantic review tied to exact candidate/artifact hashes;
- rendered accessibility and visual/page review;
- exact changed-scope reconciliation after material changes;
- exact-head automated structure, localization, package, provenance and workflow-security QA;
- durable DOCX/PDF artifacts, checksums and release manifest;
- predecessor publication confirmation;
- standing Final Human Release Approval after all other required gates are green.

## Release-time watch

At candidate time re-check whether ISO has published a new edition, corrigendum, amendment, interpretation or status change affecting ISO/IEC 27001:2022, ISO/IEC 27001:2022/Amd 1:2024 or ISO/IEC 27002:2022. Any material source change reopens affected technical/editorial, localization, changed-scope and rendered-document gates.
