# ISO/IEC 27001 and 27002 English Master — Technical and Editorial Review

## Candidate

- Repository: `Chpmunk31456/GRC-Practical-Manuals`
- Branch: `production/multilingual-grc-editions`
- Candidate branch SHA reviewed: `6c4974380200d7636a9a84671a4dad5c488d8409`
- Source: `02-management-systems/ISO_IEC_27001_27002/English_Source_ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_v1.0.md`
- Source blob SHA: `77568a9e61d6769d6eb3dbbed6b131a58d60e1f1`
- Pull request: `#3` — remains draft and unmerged
- Review date: 2026-07-31

## Review result

**PASS FOR ENGLISH MARKDOWN GATE**

No verified technical or editorial defect requiring a source correction was found in this review.

## Verified standards-currentness points

The following claims were checked against current official ISO sources:

- The current base editions used by this manual are ISO/IEC 27001:2022 and ISO/IEC 27002:2022.
- ISO/IEC 27001:2022 is the requirements standard for an information security management system.
- ISO/IEC 27002:2022 provides information-security control guidance and is not itself the management-system certification standard.
- ISO/IEC 27001:2022/Amd 1:2024 is published and applies to ISO/IEC 27001:2022.
- Amendment 1 adds climate-change consideration to organizational context and interested-party requirements; the manual appropriately describes this as a relevance determination rather than an automatic requirement to create a separate climate program.
- ISO develops standards but does not certify organizations or issue ISO certificates. Certification is performed by external certification bodies and is optional unless another obligation makes it necessary.

## Verified technical and editorial points

- The manual distinguishes normative ISO/IEC 27001 requirements from ISO/IEC 27002 implementation guidance.
- Clauses 4–10 are presented as the management-system requirements structure.
- Annex A is represented as 93 reference controls organized into four themes: 37 organizational, 8 people, 14 physical, and 34 technological controls.
- The manual correctly avoids treating Annex A as a universal checklist requiring every control in every implementation.
- Risk assessment, risk treatment, control selection, and the Statement of Applicability are presented as connected but distinct activities.
- The Statement of Applicability is described as recording necessary controls, justification, implementation status, and justified exclusions.
- Internal audit, management review, nonconformity, corrective action, evidence quality, certification readiness, and continual improvement are separated appropriately.
- The publication notice clearly states that the manual is independent educational material, not an ISO publication, certification decision, legal opinion, or substitute for licensed standards.
- The manual correctly instructs readers to use licensed ISO standards for exact requirements and guidance.
- The statement that ISO does not certify organizations is accurate and appropriately directs certification reliance toward scope, accreditation, locations, version, and certificate status.
- The corrected Word table-of-contents instruction is clear and no malformed `True Word contents` label remains.
- The automated baseline confirms all expected Chapters 1–28 appear exactly once and all configured ISO facts are present.

## Review boundary

This record is a source-level technical and editorial review of the English Markdown master. It does not certify conformity with ISO/IEC 27001, interpret copyrighted standard text, provide legal advice, validate a certification body, or replace use of licensed standards.

The review also does not constitute:

- full link execution testing;
- page-by-page DOCX or PDF visual inspection;
- assistive-technology or reading-order validation;
- independent standards-law or certification-scheme legal review;
- Spanish or Brazilian Portuguese language and terminology approval.

## Remaining gates

- Propagate approved English corrections already made during baseline review to localized Markdown where applicable.
- Complete documented Spanish terminology and language review.
- Complete documented Brazilian Portuguese terminology and language review.
- Rebuild localized DOCX and PDF outputs from settled sources.
- Inspect generated headings, tables, graphics, links, page breaks, headers, footers, searchable text, metadata, and accessibility structure.
- Run the final repository-wide release gate at the exact candidate production SHA.
- Obtain owner authorization before changing PR `#3` from draft or merging it.

## Status

The ISO/IEC 27001 and 27002 English Markdown master is technically and editorially suitable to proceed to localization synchronization and generated-document QA, subject to the remaining documented release gates.
