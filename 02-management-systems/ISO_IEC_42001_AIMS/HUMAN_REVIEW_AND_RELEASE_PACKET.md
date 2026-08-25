# Manual 02 — Human Review and Release Decision Packet

**Manual:** ISO/IEC 42001 AI Management System Implementation

**Pull request:** `#89`

**Candidate branch:** `build/iso-iec-42001-manual-02-2026`

**Candidate commit:** `5a598ea999f0d2e9d86625da84db2634443d9185`

**Controlled source commit:** `647c88fa905a16cba4e3ec162a32aad56f48c58b`

**Languages:** English, neutral Latin American Spanish (`es-419`), Brazilian Portuguese (`pt-BR`)

**Current status:** Gates 1–5 passed; Gate 6 human reviews open; Gate 7 blocked.

This packet is the controlled entry point for the remaining human decisions. Automated QA, AI-assisted review, repository checks and a standing instruction to publish when ready do not substitute for a competent reviewer’s decision on the actual evidence.

## 1. Fail-closed release rule

Manual 02 must remain a draft and must not be merged, tagged, described as final or published as a release if any mandatory review is:

- missing;
- incomplete;
- rejected;
- awaiting remediation;
- based on a different candidate commit without a documented impact assessment; or
- invalidated by a material source, translation, graphic, document or control change.

Every completed review must record reviewer, competence, date, decision, evidence, findings and remediation. Final Human Release Approval occurs only after all prerequisite reviews are approved and their evidence is assembled.

## 2. Candidate evidence inventory

| Evidence | Location | Status at candidate commit |
|---|---|---|
| English controlled master | `English/ISO_IEC_42001_2023_Practical_AIMS_Manual_English_v1.0.md` | Controlled source |
| Spanish controlled draft | `translations/es-419/source/Manual_02_ISO_IEC_42001_AI_Management_System_ES-419.md` | Human review required |
| Portuguese controlled draft | `translations/pt-BR/source/Manual_02_ISO_IEC_42001_AI_Management_System_PT-BR.md` | Human review required |
| Licensed-source queue | `SOURCE_VERIFICATION_REPORT_01.md` | Public-source review passed; licensed verification open |
| AI-assisted localization review | `translations/CONTROLLED_TRANSLATION_REVIEW_03.md` | Ready for human review |
| Human language checklist | `translations/HUMAN_SEMANTIC_REVIEW_CHECKLIST.md` | Open |
| Editorial QA | `EDITORIAL_QA_REVIEW_01.md` | Completed automated/advisory review |
| Visual QA | `VISUAL_QA_REVIEW_01.md` | Completed automated/visual candidate review |
| Publication artifacts | `publication/qa-candidate/` | QA candidates only |
| Document-processing report | `../../qa/manual02-document-processing/ISO_IEC_42001_MANUAL_02_DOCUMENT_PROCESSING_REPORT.md` | Gates 1–5 pass |
| Page-level review | `../../qa/manual02-document-processing/ISO_IEC_42001_MANUAL_02_PAGE_QA.csv` | 136 pages checked |
| Candidate checksums | `../../qa/manual02-document-processing/ISO_IEC_42001_MANUAL_02_SHA256SUMS.txt` | Present |

Repository-relative note: the three `qa/manual02-document-processing` links above resolve from the repository root; reviewers may use the literal paths shown in the file names if their Markdown client does not resolve relative links.

## 3. Gate 6A — Licensed ISO source, citation and copyright-boundary review

### Required reviewer competence

A human reviewer with authorized access to the relevant ISO publications and sufficient ISO/IEC 42001 management-system or conformity-assessment competence to evaluate clause/Annex characterization, normative strength, certification-stage statements and licensed-text similarity.

### Required review scope

- Clause 4–10 and Annex A–D descriptions against an authorized copy of ISO/IEC 42001:2023.
- Annex A control count and group count.
- Relationship among risk treatment, additional controls, Annex A selection/exclusion and the Statement of Applicability.
- Annex A.4, A.7 and A.8 implementation wording.
- Informative/normative characterization of Annexes B–D.
- Stage 1, Stage 2 and certification-cycle descriptions against authorized ISO/IEC 17021-1:2015, ISO/IEC 42006:2025, applicable accreditation requirements and the intended certification scheme.
- Normative-language cues identified in `SOURCE_VERIFICATION_REPORT_01.md`.
- Licensed-text similarity and copyright boundary across the English master and localized editions.

### Decision record

| Field | Reviewer entry |
|---|---|
| Reviewer name | Pending |
| Organization/role | Pending |
| Review date | Pending |
| Authorized-source access confirmed | Pending |
| Relevant competence | Pending |
| Conflict/independence note | Pending |
| Candidate commit reviewed | Pending |
| Evidence reviewed | Pending |
| Decision: `APPROVED`, `APPROVED WITH CONDITIONS`, `REJECTED`, or `INCOMPLETE` | Pending |
| Findings reference | Pending |
| Remediation verified | Pending |
| Signature/attestation method | Pending |

## 4. Gate 6B — Spanish (`es-419`) human semantic and terminology review

### Required reviewer competence

A competent human reader/editor of neutral professional Latin American Spanish who can evaluate ISO, AI governance, GRC, audit, risk, supplier, corrective-action and management-system meaning.

### Required review scope

- All 32 localized chapters against the English controlled master.
- Chapter order, headings, tables, evidence relationships and external references.
- Controlled terminology and locale-natural professional usage.
- Distinction between AI risk assessment and AI system impact assessment.
- Statement of Applicability, certification, internal-audit, supplier-accountability and corrective-action boundaries.
- Ten localized graphics, captions, visible labels, alternative text and accessible explanations.
- Loanword policy and the review items identified in `CONTROLLED_TRANSLATION_REVIEW_03.md`.

### Decision record

| Field | Reviewer entry |
|---|---|
| Reviewer name | Pending |
| Organization/role | Pending |
| Review date | Pending |
| Language competence | Pending |
| ISO/AI/GRC domain competence | Pending |
| Conflict/independence note | Pending |
| Candidate commit reviewed | Pending |
| Evidence reviewed | Pending |
| Decision: `APPROVED`, `APPROVED WITH CONDITIONS`, `REJECTED`, or `INCOMPLETE` | Pending |
| Critical findings open | Pending |
| Major findings open | Pending |
| Findings reference | Pending |
| Remediation verified | Pending |
| Signature/attestation method | Pending |

## 5. Gate 6C — Brazilian Portuguese (`pt-BR`) human semantic and terminology review

### Required reviewer competence

A competent human reader/editor of professional Brazilian Portuguese who can evaluate ISO, AI governance, GRC, audit, risk, supplier, corrective-action and management-system meaning.

### Required review scope

- All 32 localized chapters against the English controlled master.
- Chapter order, headings, tables, evidence relationships and external references.
- Controlled terminology and natural Brazilian professional usage.
- Distinction between AI risk assessment and AI system impact assessment.
- Statement of Applicability, certification, internal-audit, supplier-accountability and corrective-action boundaries.
- Ten localized graphics, captions, visible labels, alternative text and accessible explanations.
- Loanword policy and the review items identified in `CONTROLLED_TRANSLATION_REVIEW_03.md`, including `asseguração`, `constatação`, `subprocessador` and `auditoria de supervisão`.

### Decision record

| Field | Reviewer entry |
|---|---|
| Reviewer name | Pending |
| Organization/role | Pending |
| Review date | Pending |
| Language competence | Pending |
| ISO/AI/GRC domain competence | Pending |
| Conflict/independence note | Pending |
| Candidate commit reviewed | Pending |
| Evidence reviewed | Pending |
| Decision: `APPROVED`, `APPROVED WITH CONDITIONS`, `REJECTED`, or `INCOMPLETE` | Pending |
| Critical findings open | Pending |
| Major findings open | Pending |
| Findings reference | Pending |
| Remediation verified | Pending |
| Signature/attestation method | Pending |

## 6. Consolidated findings and remediation log

| ID | Gate | Location | Severity | Finding | Owner | Remediation | Retest/review evidence | Status |
|---|---|---|---|---|---|---|---|---|
| HR-001 | Pending | Pending | Pending | Pending | Pending | Pending | Pending | Pending |

Severity:

- **Critical:** changes an obligation, assurance/certification meaning, authority, safety boundary, source identity or copyright boundary.
- **Major:** materially changes a control, risk, impact, evidence, lifecycle, audit, supplier, accessibility or corrective-action concept.
- **Minor:** terminology, readability, punctuation, layout or style with no material meaning change.

All Critical and Major findings must be closed or explicitly accepted by an authorized person within a documented boundary before final release approval.

## 7. Material-change impact assessment

After any reviewer approval, compare the approved candidate with the proposed release commit.

| Field | Entry |
|---|---|
| Approved candidate commit | Pending |
| Proposed release commit | Pending |
| Changed files | Pending |
| Source meaning affected? | Pending |
| Localization meaning affected? | Pending |
| Graphics/accessibility affected? | Pending |
| DOCX/PDF layout affected? | Pending |
| Security/reproducibility affected? | Pending |
| Re-review gates reopened | Pending |
| Assessor and date | Pending |

Editorial metadata-only changes may be accepted through documented impact analysis. Any material change reopens the affected gate and requires new reviewer evidence against the release commit.

## 8. Gate 7 — Final Human Release Approval

The release approver reviews the complete package only after Gates 6A, 6B and 6C are approved and all blocking findings are resolved. Conditional standing authorization to publish when ready permits execution of an approved release; it does not attest that this evidence was reviewed.

### Final decision record

| Field | Release approver entry |
|---|---|
| Release approver | Pending |
| Authority/role | Pending |
| Decision date | Pending |
| Exact release commit | Pending |
| Gate 6A approval evidence | Pending |
| Gate 6B approval evidence | Pending |
| Gate 6C approval evidence | Pending |
| Automated QA/workflow evidence | Pending |
| Security/accessibility/visual evidence | Pending |
| Open Critical findings | Pending |
| Open Major findings | Pending |
| Accepted conditions/known limitations | Pending |
| Decision: `APPROVED FOR RELEASE` or `REJECTED / REMEDIATION REQUIRED` | Pending |
| Signature/attestation method | Pending |

## 9. Release execution checklist

Release execution may begin only after the final record states `APPROVED FOR RELEASE` for the exact release commit.

- [ ] Confirm the proposed release commit matches the approved commit.
- [ ] Confirm all required workflows pass at that commit.
- [ ] Confirm the reproducibility diff is empty.
- [ ] Confirm checksums match committed artifacts.
- [ ] Confirm candidate labels are replaced only through the controlled release change.
- [ ] Confirm localized editions retain the non-ISO-authorized-translation disclaimer.
- [ ] Confirm release notes state the exact source/version boundary and known limitations.
- [ ] Create the release/tag/package without modifying protected `main` outside the approved merge workflow.
- [ ] Record the release URL, tag, commit, date and actor as an action receipt.
- [ ] Keep rollback/withdrawal instructions available if post-release evidence invalidates the approval.

## 10. Current disposition

`AWAITING QUALIFIED HUMAN REVIEW — DO NOT RELEASE`

The package is technically ready for the three Gate 6 reviews. Publication remains fail-closed until their completed records and the subsequent Gate 7 decision are committed or otherwise linked as durable evidence.
