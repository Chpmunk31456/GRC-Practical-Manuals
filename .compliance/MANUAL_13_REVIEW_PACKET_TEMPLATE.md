# Manual 13 — SOX ITGC / ICFR Consolidated Review Packet Template

**State:** PRE-STAGE / NOT RELEASE AUTHORIZATION  
**Series order:** 13  
**Planned title:** SOX — ITGC, ICFR and Technology Controls  
**Purpose:** Pre-stage a single fail-closed reviewer packet so human-review evidence can be captured against an exact candidate without late-cycle evidence design.

This template does not constitute a human review, approval, or release decision. Every required decision below must identify the reviewer, review date, exact candidate commit, exact artifact hashes, decision, evidence examined, findings, remediation, and any required re-review.

## 1. Exact candidate binding

The QA-passed publication-candidate workflow artifact is now cryptographically bound below. The candidate commit remains **PENDING** until these exact bytes are durably staged in the publication path on a repository head. Do not regenerate, resave, print-to-PDF, or otherwise transform these binaries while staging them.

- Candidate commit SHA: **PENDING — bind only after exact validated bytes are durably staged**
- Validated publication-candidate workflow run: **33330513993**
- Validated publication-candidate artifact ID: **9737505864**
- English controlled-source tree/hash: **PENDING**
- es-419 controlled-source tree/hash: **PENDING**
- pt-BR controlled-source tree/hash: **PENDING**
- EN DOCX SHA-256: `e30a7125c6a611b084f21ab9a8f3a60cd2a9934dc2a9128d976d8917b179d240`
- EN PDF SHA-256: `637f8122d361abdecb7b07f9f67069d3e735ff261b3f6524ed5981fde556e4eb`
- es-419 DOCX SHA-256: `b05b8bd88f7bc355ba56a8e8f9c4637fcab357017c601535d5578854bf322d9e`
- es-419 PDF SHA-256: `e3ceaeb100bee6285d3b5e4c61bbfa2241bf25f0de308e47893a49277ac49aca`
- pt-BR DOCX SHA-256: `41febef509b451d8eca3b900f60f4fea75e4537d2c2bd218aefcb9447fd8da5e`
- pt-BR PDF SHA-256: `75811ddc5912585983ac198d4938ceace361d3662e401a8e511b453d7a62760c`
- Publication-package / manifest SHA-256: **PENDING**
- Source-verification record hash: **PENDING**

Fail closed on byte drift. A repository upload that differs from any validated SHA-256 above is not the candidate and must not be merged merely because its filename, rendered appearance, or source content appears equivalent.

Any material change after a review decision must identify affected scopes and reopen those gates only.

## 2. Authoritative-source verification gate

Reviewer must confirm, for the candidate publication date:

- official statutory text for Sarbanes-Oxley Act Sections 302 and 404;
- current SEC Section 404 implementing rule and applicable management guidance;
- currently effective PCAOB AS 2201 text;
- explicit treatment of PCAOB amendments approved but not yet effective, including the 2026-12-15 effective-date watch identified in preflight;
- current filer-status, exemption, transition, and auditor-attestation boundaries;
- source URLs, retrieval/verification date, and any repository-required immutable evidence.

**Decision:** PENDING  
**Reviewer:** PENDING  
**Date:** PENDING  
**Evidence:** PENDING  
**Findings/remediation:** PENDING

## 3. SOX / ICFR legal-audit-editorial gate

Human reviewer must verify that the manual:

- keeps SOX/ICFR scope distinct from generic cybersecurity compliance;
- distinguishes management responsibilities from external-auditor responsibilities;
- uses material weakness, significant deficiency, reasonable assurance, assertions, control objectives, and related terminology consistently with controlling SEC/PCAOB sources;
- presents ITGCs only in their financially relevant ICFR context;
- does not elevate COSO or another framework into statutory/regulatory authority;
- handles automated controls, reports, interfaces, spreadsheets/EUC, cloud/SaaS, third parties, and AI/automation with explicit ICFR relevance;
- avoids unsupported applicability claims or legal conclusions.

**Decision:** PENDING  
**Reviewer:** PENDING  
**Date:** PENDING  
**Evidence:** PENDING  
**Findings/remediation:** PENDING

## 4. Control-mapping / practitioner-accuracy gate

Human reviewer must verify design-vs-operating-effectiveness treatment, evidence sufficiency, testing and sampling boundaries, deficiency escalation, remediation/retesting, management-certification support, and external-auditor evidence handoff. Mapping must preserve traceability to authoritative sources and clearly label practitioner guidance versus legal/audit requirements.

**Decision:** PENDING  
**Reviewer:** PENDING  
**Date:** PENDING  
**Evidence:** PENDING  
**Findings/remediation:** PENDING

## 5. Localization semantic gates

### es-419
Human semantic reviewer must verify faithful meaning, controlled terminology, legal/audit nuance, table/figure/caption parity, and absence of machine-literal distortions.

**Decision:** PENDING  
**Reviewer:** PENDING  
**Date:** PENDING  
**Evidence:** PENDING  
**Findings/remediation:** PENDING

### pt-BR
Human semantic reviewer must verify faithful meaning, controlled terminology, legal/audit nuance, table/figure/caption parity, and absence of machine-literal distortions.

**Decision:** PENDING  
**Reviewer:** PENDING  
**Date:** PENDING  
**Evidence:** PENDING  
**Findings/remediation:** PENDING

## 6. Rendered accessibility / visual gate

Review the exact DOCX/PDF artifacts for all three languages. At minimum verify headings, reading order, table structure, figures/alt text, captions, footer consistency, contrast, page breaks, clipping/overflow, links, language metadata, PDF tagging where required, and visual correspondence with the controlled source.

**Decision:** PENDING  
**Reviewer:** PENDING  
**Date:** PENDING  
**Evidence:** PENDING  
**Findings/remediation:** PENDING

## 7. Changed-scope reconciliation gate

Reviewer must compare the final candidate against the last reviewed candidate and identify every material change after prior review. Reopen only affected review scopes, but fail closed if the changed scope cannot be bounded confidently.

**Decision:** PENDING  
**Reviewer:** PENDING  
**Date:** PENDING  
**Evidence:** PENDING  
**Findings/remediation:** PENDING

## 8. Automated evidence that must accompany the human packet

Before release readiness is declared, attach or reference exact-head evidence for:

- manual structure/content QA;
- trilingual parity;
- document/package QA;
- provenance/checksum/manifest validation;
- workflow security and dependency-lineage checks;
- exact-head publication-candidate build;
- release-registry/catalog reconciliation logic;
- durable artifact presence.

Automation may support evidence collection but cannot substitute for the human decisions above.

## 9. Standing final release authorization

Standing Final Human Release Approval is already GREEN under the canonical program control and is not to be re-requested. Publication remains blocked until all substantive gates explicitly required to be genuine-human are complete for the exact final candidate.

## 10. Release handoff condition

Manual 13 may move from reviewer-ready to release-eligible only when all mandatory fields above are complete, exact candidate/artifact hashes are stable, automated exact-head gates are green, predecessor Manual 12 is published, and catalog/release-registry/provenance changes are prepared for the same release transaction.
