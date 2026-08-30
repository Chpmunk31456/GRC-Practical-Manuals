# Manual 15 — Legacy SOC 2 source to controlled 32-chapter mapping

**Source asset:** `03-assurance-and-audit/SOC2_Audit_Readiness_Bilingual_v1.0/English/How_to_Prepare_for_a_SOC_2_Audit_English_v1.0.md`

**Controlled target:** `04-regulatory-compliance/SOC_2_Controlled_Implementation`

**Purpose:** Preserve useful original implementation material while rebuilding it into the Manual 15 controlled architecture. The legacy manual is source material, not proof of publication readiness, current authoritative status, or semantic equivalence in localized editions.

## Mapping

| Controlled chapter | Controlled topic | Primary legacy source | Migration treatment |
|---|---|---|---|
| 01 | Purpose, audience, engagement context | §1, §17 | Reframe audience, readiness boundary, CPA independence and non-certification language. |
| 02 | Service-organization boundary and system definition | §4 | Expand products/services, components, locations, people, processes, data and dependencies. |
| 03 | Management responsibilities and assertion | §1, §3, §16 | Separate management ownership/assertion from practitioner responsibilities. |
| 04 | System description and description criteria | §16 | Expand controlled description-quality and change-maintenance evidence. |
| 05 | Trust Services Criteria structure | §5 | Preserve risk-to-control framing; avoid reproducing copyrighted criteria text. |
| 06 | Security/common criteria implementation model | §5, §7–10 | Consolidate governance, access, operations, change and monitoring evidence. |
| 07 | Availability implementation model | §11 | Expand capacity, resilience, backup, recovery, monitoring and commitments. |
| 08 | Processing integrity implementation model | §5, §9 | Add completeness, validity, accuracy, timeliness and authorization implementation patterns without copying criteria text. |
| 09 | Confidentiality implementation model | §12 | Separate confidentiality commitments, classification, access and lifecycle protections. |
| 10 | Privacy implementation model | §12 | Separate privacy lifecycle, notices, choices/requests, retention, disclosure and disposal. |
| 11 | Risk assessment and control design | §6 | Expand risk criteria, fraud/change/vendor considerations and traceability. |
| 12 | Governance and policy management | §3, §7 | Preserve ownership/RACI and document-control model; add exception/change triggers. |
| 13 | Logical access and identity lifecycle | §8 | Expand joiner/mover/leaver, service identities, contractors and evidence populations. |
| 14 | Privileged access and MFA | §8 | Separate privileged and strong-authentication assurance, emergency access and review. |
| 15 | System operations and monitoring | §10 | Expand operational monitoring, alert ownership, escalation and evidence retention. |
| 16 | Vulnerability and configuration management | §9–10 | Separate vulnerability/configuration lifecycle, exceptions, remediation and validation. |
| 17 | Incident response and recovery | §10–11 | Combine incident governance with recovery, lessons learned and change-trigger reassessment. |
| 18 | Change management and SDLC | §9 | Expand authorization, testing, segregation, emergency change and deployment evidence. |
| 19 | Logging, alerting and evidence retention | §10, §14 | Separate log coverage/retention from general evidence-management practice. |
| 20 | Backup, resilience and availability monitoring | §11 | Deepen recovery testing, capacity, RTO/RPO support and exception evidence. |
| 21 | Vendor and subservice-organization governance | §13 | Preserve due diligence/monitoring; expand responsibility and assurance dependencies. |
| 22 | Complementary user-entity controls | §4, §16 | Separate CUEC identification, communication, ownership and system-description treatment. |
| 23 | Cloud/shared-responsibility considerations | §4, §13 | Add cloud control ownership, inherited controls, service dependencies and evidence boundaries. |
| 24 | Privacy operations and data lifecycle | §12 | Deepen operational privacy evidence while retaining distinction from confidentiality. |
| 25 | Evidence population and sampling readiness | §14–15 | Preserve completeness/accuracy/population principles; add provenance and reproducibility. |
| 26 | Type 1 versus Type 2 readiness | §2 | Preserve distinction; expand design/implementation vs operating-effectiveness evidence planning. |
| 27 | Exception, deviation and remediation governance | §15, §18 | Consolidate exception classification, root cause, remediation, retest and repeat-failure escalation. |
| 28 | Management review and continuous monitoring | §3, §18–19 | Add control-health reporting, missed evidence, aging, changes and management decisions. |
| 29 | Auditor interaction and request management | §17 | Preserve independence boundary and add request-log, evidence-transfer and issue-resolution controls. |
| 30 | Report-reading, qualifications and findings | §17–18 | Add controlled interpretation of report scope, period, exceptions, qualifications and user responsibilities. |
| 31 | Continuous compliance and change triggers | §18–19 | Convert readiness roadmap into recurring evidence/control monitoring and reassessment triggers. |
| 32 | Release, reassessment and evidence lifecycle | §20 | Reframe portfolio/checklist material into controlled release, retention, reassessment and safe-publication rules. |

## Reuse and copyright boundaries

The legacy source is original repository material and may be adapted, but the controlled manual must still be revalidated against the current official AICPA source state. No legacy passage is automatically authoritative. The controlled manual must not reproduce AICPA Trust Services Criteria, Description Criteria, paid guide text, illustrative reports, or practitioner-only material beyond legally permissible identifiers and brief quotations.

Existing legacy DOCX/PDF files and localized editions remain historical/source artifacts. They must not be relabeled as Manual 15 controlled publication binaries. New controlled artifacts must be generated from the exact controlled sources and independently hash-bound.

## Controlled chapter acceptance criteria

Every controlled chapter must, where applicable, identify:

- purpose and scope;
- risk or assurance objective;
- accountable owner and operating roles;
- implementation procedure;
- operating frequency or trigger;
- population or system boundary;
- evidence artifact and source location;
- reviewer/test approach;
- exception/remediation path;
- change/reassessment trigger;
- explicit boundary between management readiness work and independent CPA judgment.

## Migration completion rule

Migration is complete only when all 32 target chapters exist in the controlled English master, the source-state/copyright boundaries remain intact, and no required controlled topic depends solely on an unreviewed legacy artifact. Localization and rendered publication work must derive from the exact controlled candidate, not from the legacy bilingual package.

This mapping is deterministic build evidence only. It does not assert human semantic, legal, editorial, accessibility/visual or practitioner review and does not change publication status.
