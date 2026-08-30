# Manual 19 — FedRAMP / FISMA Preflight

**State:** downstream pre-stage only / not release-ready / not published  
**Series order:** 19  
**Preflight date:** 2026-08-30

## Purpose

Pre-stage the FedRAMP / FISMA manual against the current 2026 transition environment without claiming authorization, assessment equivalence, legal review, or publication readiness.

## Live source-state observations — 2026-08-30

Current FedRAMP official materials show an active transition from legacy Rev5 processes toward FedRAMP 20x and the Consolidated Rules for 2026. The Consolidated Rules for 2026 are already available, optional adoption began in July 2026 for several rule sets, and broader mandatory adoption dates extend into 2027. FedRAMP also states that new Rev5 Certification applications are targeted to end on 2027-06-11, while existing Rev5 certifications transition over a longer period.

Authoritative source targets to re-check at build and release time:

- FedRAMP official program and Consolidated Rules for 2026: https://www.fedramp.gov/
- FedRAMP Rev5 deadlines and transition guidance: https://www.fedramp.gov/2026/providers/updating/deadlines/rev5/
- NIST SP 800-53 current publication and control baselines.
- NIST Risk Management Framework sources.
- FISMA statutory and OMB/CISA policy sources applicable to the manual's scope.

## Principal source and scope risks

- Do not describe legacy Rev5 process mechanics as timeless FedRAMP requirements.
- Distinguish FedRAMP 20x, Rev5 transition rules, certification paths, agency authorization, and historical terminology.
- Distinguish FISMA statutory obligations from FedRAMP program requirements and from NIST implementation guidance.
- Treat RFCs and previews according to their actual status; do not present proposed material as binding unless formally adopted.
- Track machine-readable package requirements and OSCAL-related expectations independently from security-control content.
- Preserve agency-specific overlays and OMB/CISA requirements as separate applicability layers.

## Controlled-build architecture target

Prepare a 32-chapter controlled English architecture covering:

- federal governance and applicability boundaries;
- FISMA, NIST RMF, SP 800-53 and FedRAMP relationship model;
- system categorization and authorization context;
- control selection, tailoring, implementation, evidence, assessment and continuous monitoring;
- FedRAMP certification/authorization pathways and current transition rules;
- machine-readable authorization package concepts and evidence lifecycle;
- vulnerability, configuration, incident, supply-chain and service-provider evidence;
- Essential / Structured / Enhanced implementation paths;
- remediation, reassessment, ongoing authorization/certification maintenance and scenario training.

## Publication preflight controls

Before publication, Manual 19 must independently satisfy current-source verification, controlled English completion, es-419/pt-BR localization, exact-head automated QA, substantive controls required by repository policy, rendered/accessibility QA, durable DOCX/PDF staging, SHA-256 provenance, workflow-security checks, manifest/catalog/release-registry reconciliation, predecessor publication through Manual 18, and zero unresolved substantive or integrity defects.

Manual 19 may build in parallel but must never publish before Manual 18.
