# Manual 16 — ISO/IEC 27001 / 27002 Controlled Build Gate

**State:** active front-manual controlled build; not publication authorization  
**Series order:** 16  
**Predecessor:** Manual 15 — published  
**Authoritative baseline:** ISO/IEC 27001:2022 + ISO/IEC 27001:2022/Amd 1:2024 + ISO/IEC 27002:2022  
**Legacy English source blob:** `77568a9e61d6769d6eb3dbbed6b131a58d60e1f1`

## Exact lineage

Controlled construction must derive from the repository's original English implementation source and the merged 32-chapter migration architecture. Legacy DOCX/PDF and localized files are reference inputs only; they are not Manual 16 release candidates. Every authoritative assertion must remain within the current source-state boundaries recorded in `MANUAL_16_SOURCE_STATE_2026-08-30.md`.

## Controlled-English acceptance contract

The exact English controlled master must contain all 32 chapters defined in `MANUAL_16_LEGACY_TO_CONTROLLED_MIGRATION.md`. For each applicable chapter, implementation guidance must identify:

- purpose and organizational context;
- risk or management-system objective;
- accountable owner and supporting roles;
- implementable procedure or decision path;
- operating frequency or trigger;
- evidence object and evidence source/location;
- review, testing or measurement approach;
- exception, nonconformity or remediation path; and
- reassessment/change trigger.

No section may present ISO/IEC 27002 guidance as an ISO/IEC 27001 requirement. Statement-of-Applicability and control-selection decisions must remain risk- and context-based. Certification claims, audit conclusions and conformity decisions must not be represented as outcomes of this manual.

## Copyright and standards boundary

The controlled source must use original explanatory language. It must not reproduce protected ISO/IEC clauses, Annex A text, control text, tables or proprietary explanatory passages beyond legally permissible identifiers and brief quotations. Any legacy passage that appears to closely reproduce protected language is a fail-closed editorial/copyright finding and must be rewritten or reviewed before candidate freeze.

## Climate-amendment integration

Implementation treatment of the 2024 climate-action amendment belongs in organizational-context and interested-party analysis. It must describe the management-system action required at an implementation level without reproducing protected amendment wording or implying a particular relevance conclusion for every organization.

## Localization gate

Controlled es-419 and pt-BR editions must derive only from the exact frozen English controlled master. Legacy localized files may be consulted for terminology consistency but may not be promoted as controlled translations. Terminology, normative-strength distinctions, risk/context qualifiers, evidence semantics and certification boundaries must remain aligned across all three editions.

Where repository policy requires genuine semantic judgment, automation may prepare the review packet and deterministic parity evidence but may not invent reviewer identity, decision or findings.

## Publication-candidate gate

Before publication-state promotion, the exact trilingual candidate lineage must have:

1. current release-time authoritative-source delta verification;
2. complete 32-chapter controlled English source;
3. controlled es-419 and pt-BR sources tied to the exact English source identity;
4. deterministic structural and trilingual-parity QA;
5. DOCX/PDF generation for all three editions;
6. PDF content preflight and rendered content/accessibility/visual checks required by repository policy;
7. exact SHA-256 identities for all six binaries and source/provenance records;
8. durable binary staging on `main` without post-hash regeneration;
9. workflow-security and release-pipeline checks on the exact candidate;
10. no unresolved substantive source, legal/editorial, technical, localization-semantic, accessibility/visual, changed-scope, integrity or packaging finding; and
11. catalog and work-product release-registry reconciliation only after the durable candidate is proven on `main`.

Standing Final Human Release Approval is already active under the canonical repository rule and is not a separate blocker. Missing duplicate review paperwork alone may not halt a clean candidate, but an actual documented substantive defect remains fail-closed.

## Anti-halt handoff

While Manual 16 is completing controlled source, localization and candidate work, Manual 17 should continue candidate/pre-publication preparation, Manual 18 rendered/source/security/provenance preflight, and later manuals controlled architecture and source-watch work. Publication order remains sequential.
