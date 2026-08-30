# Manual 14 — Legacy Source to Controlled 32-Chapter Reconciliation Map

**State:** active build aid / not publication evidence  
**Prepared:** 2026-08-30

## Purpose

Map the existing 25-chapter PCI DSS v4.0.1 practical manual into the controlled Manual 14 architecture without silently relabeling legacy content or losing provenance. The legacy source remains an input asset; every migrated section must be revalidated against the current PCI SSC source state and Manual 14 evidence model.

## Legacy source reviewed

`04-regulatory-compliance/PCI_DSS_v4.0.1/English_Source_PCI_DSS_v4.0.1_Practical_Manager_and_Junior_Analyst_Manual_v1.0.md`

Observed legacy structure: foundations, account data, scope/segmentation, validation roles, defined/customized/compensating approaches, twelve PCI DSS requirement chapters, evidence/testing, open-source tools, manager playbook, analyst development, fictional laboratory, learning plan, interview preparation, templates/glossary/index.

## Controlled chapter mapping

| Controlled chapter | Controlled topic | Principal legacy inputs | Required controlled-build treatment |
|---|---|---|---|
| 01 | Governance and PCI DSS operating model | Preface; Ch. 1; Ch. 20 | add owner/accountability, cadence, evidence and escalation model |
| 02 | Applicability and entity/validation boundaries | Ch. 1; Ch. 4 | separate PCI DSS applicability from acquirer/payment-brand/legal obligations |
| 03 | Account data and protection boundaries | Ch. 2 | retain PAN/SAD distinctions; revalidate terminology and storage rules |
| 04 | Scoping and CDE boundaries | Ch. 3 | add repeatable scope procedure, evidence objects and reassessment triggers |
| 05 | Data flows and segmentation | Ch. 3; labs | separate data-flow evidence from segmentation assumptions and testing |
| 06 | Roles, validation and assurance pathways | Ch. 4 | distinguish SAQ/ROC/AOC, assessor roles and compliance-accepting entities |
| 07 | Defined/customized/compensating approaches | Ch. 5 | preserve current applicability boundaries and evidence requirements |
| 08 | Evidence architecture and implementation paths | Ch. 18; Ch. 20 | normalize Essential/Structured/Enhanced paths and evidence schema |
| 09 | Network security controls | Legacy Requirement 1 / Ch. 6 | convert to objective-owner-procedure-frequency-evidence-test format |
| 10 | Secure configurations | Legacy Requirement 2 / Ch. 7 | add baseline/change/evidence lifecycle |
| 11 | Stored account-data protection | Legacy Requirement 3 / Ch. 8 | revalidate retention, masking, truncation and cryptographic boundaries |
| 12 | Transmission cryptography | Legacy Requirement 4 / Ch. 9 | add protocol/configuration evidence and reassessment triggers |
| 13 | Malware defenses | Legacy Requirement 5 / Ch. 10 | add applicability decisions, monitoring evidence and exception logic |
| 14 | Secure systems and software | Legacy Requirement 6 / Ch. 11 | expand secure development, change and e-commerce dependencies |
| 15 | Vulnerability management | Ch. 11; Ch. 19 | separate vulnerability workflow from tool-specific examples |
| 16 | Change control and configuration assurance | Ch. 11; Ch. 18 | add change approval, evidence, regression and reassessment controls |
| 17 | Access-control model | Legacy Requirement 7 / Ch. 12 | formalize business-need, role and entitlement evidence |
| 18 | Identity, authentication and MFA | Legacy Requirement 8 / Ch. 13 | isolate identity lifecycle and MFA evidence/testing |
| 19 | Physical access | Legacy Requirement 9 / Ch. 14 | preserve facility/media boundaries and evidence |
| 20 | Logging and monitoring | Legacy Requirement 10 / Ch. 15 | add source, retention, review, alert and evidence-location model |
| 21 | Security testing | Legacy Requirement 11 / Ch. 16 | separate internal/external testing, evidence and retest expectations |
| 22 | External scans and ASV boundaries | Ch. 16; Ch. 19 | explicitly prevent open-source-tool equivalence claims |
| 23 | Penetration testing and segmentation validation | Ch. 16; labs | separate objective, scope, independence, evidence and remediation |
| 24 | Service-provider and third-party evidence | Legacy Requirement 12 / Ch. 17 | expand responsibility matrices, written agreements and monitoring evidence |
| 25 | Incident response | Ch. 17; lab incident scenario | normalize response ownership, testing, evidence and reassessment triggers |
| 26 | Exceptions and compensating controls | Ch. 5; Ch. 18 | formalize approval, rationale, evidence, expiration and reassessment |
| 27 | Validation-path operations | Ch. 4; Ch. 18 | operationalize SAQ/ROC/AOC preparation without assessor substitution |
| 28 | Continuous compliance and control monitoring | Ch. 18; Ch. 20 | add recurring evidence schedules, ownership and metrics |
| 29 | Remediation and retesting | Ch. 18; Ch. 20; labs | formalize finding-owner-date-evidence-retest lifecycle |
| 30 | Management assurance and reporting | Ch. 20 | add executive reporting, risk acceptance and escalation evidence |
| 31 | Maturity and capability progression | Ch. 21; Ch. 23 | convert learning progression into controlled operating maturity paths |
| 32 | Scenario-based implementation and failure modes | Ch. 22; Ch. 24; Ch. 25 | preserve labs/interview learning as scenario validation, not compliance proof |

## Material requiring special handling

- **Open-source tools (legacy Ch. 19):** retain only as bounded implementation/testing examples. Every tool entry must state what evidence it can support and what official/qualified validation it cannot replace.
- **Career/interview material (legacy Ch. 21, 23, 24):** move to scenario/maturity or companion learning material where it supports implementation competence; do not let career content dilute the controlled manual's compliance workflow.
- **Templates/glossary/index (legacy Ch. 25):** reconcile into controlled evidence templates, glossary and end matter after terminology and localization architecture are stable.
- **Legacy DOCX/PDF and localized assets:** source material only. They cannot become Manual 14 publication artifacts unless regenerated from the exact controlled candidate and pass current rendered/provenance gates.

## Migration acceptance criteria

For each controlled chapter, migration is complete only when the content has a current source boundary, applicability statement, objective, owner, procedure, frequency where applicable, evidence artifact, evidence location, reviewer/test method, exception/remediation path, reassessment trigger, and localization-ready controlled terminology.

This map reduces build ambiguity but does not satisfy final source verification, semantic/legal review where required, localization review, exact-head QA, rendered accessibility/visual QA, durable artifact staging, provenance, or publication reconciliation.
