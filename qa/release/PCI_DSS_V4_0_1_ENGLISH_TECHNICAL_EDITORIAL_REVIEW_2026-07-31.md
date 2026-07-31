# PCI DSS v4.0.1 English Master — Technical and Editorial Review

## Candidate

- Repository: `Chpmunk31456/GRC-Practical-Manuals`
- Branch: `production/multilingual-grc-editions`
- Candidate SHA reviewed: `bf70721c734673d3a516d01ba5f131a656e0c6eb`
- Source: `04-regulatory-compliance/PCI_DSS_v4.0.1/English_Source_PCI_DSS_v4.0.1_Practical_Manager_and_Junior_Analyst_Manual_v1.0.md`
- Pull request: `#3` — remains draft and unmerged
- Review date: 2026-07-31

## Review result

**PASS**

The English Markdown master is technically and editorially suitable to proceed to generated-document and localization QA. No source correction was required in this review.

## Current-version verification

The following points were checked against current official PCI Security Standards Council materials:

- PCI DSS v4.0.1 was published in June 2024 as a limited revision to v4.0.
- The limited revision added no requirements and deleted none.
- PCI DSS v4.0 retired on December 31, 2024.
- PCI DSS v4.0.1 is the current active supported version.
- The v4.x future-dated requirements became effective on March 31, 2025.
- After the effective date, applicable future-dated requirements must be considered as part of an assessment.
- Requirements superseded on March 31, 2025 are reported as not applicable after their replacement requirements became effective.
- Compliance-program and reporting decisions remain with compliance-accepting entities such as payment brands and acquirers.

## Verified technical and editorial points

- The manual covers all 12 PCI DSS requirements and the six control goals.
- Cardholder data, sensitive authentication data, PAN, and the cardholder data environment are treated as distinct scoping concepts.
- The source correctly states that entities whose systems can affect CDE security may be in scope.
- Scoping, connected-to systems, security-impacting systems, segmentation, and annual scope validation are presented as evidence-based processes rather than assumptions.
- The manual distinguishes the defined approach, customized approach, compensating controls, and targeted risk analysis.
- SAQs, Reports on Compliance, Attestations of Compliance, Qualified Security Assessors, and Approved Scanning Vendors are not treated as interchangeable.
- Open-source vulnerability scanning is not presented as a substitute for required ASV scanning.
- The source correctly states that PCI DSS v4.0.1 added no requirements and removed none.
- The source correctly states that the 51 future-dated requirements became effective March 31, 2025.
- E-commerce security, payment-page script controls, change detection, authentication, logging, vulnerability management, and penetration testing are included without overstating tool output as compliance proof.
- Service-provider evidence and shared responsibility do not remove the assessed entity’s responsibility to understand and validate applicable duties.
- Technical tools are limited to specifically authorized environments using synthetic payment data.
- The publication notice clearly states that the manual is not a PCI SSC publication, ROC, AOC, SAQ, or guarantee of compliance.

## Baseline evidence

The automated English-master audit recorded PASS after one bounded correction to the Word table-of-contents label, with:

- all expected numbered sections present exactly once;
- all 12 PCI DSS requirement headings present;
- no configured structural or placeholder defects; and
- all required version, retirement-date, and future-dated requirement markers present.

## No correction required

No verified factual, standards-currentness, structural, or material editorial defect requiring a change to the English Markdown source was found in this review.

## Remaining gates

- Human PCI assessor or payment-compliance specialist review: not completed.
- Human Spanish terminology and language review: not completed.
- Human Brazilian Portuguese terminology and language review: not completed.
- Generated DOCX/PDF page-by-page visual inspection: not completed.
- Accessibility structure, reading order, metadata, and assistive-technology review: not completed.
- Link execution and official-reference destination testing in generated formats: not completed.
- Final release-gate audit at the exact publication candidate SHA: not completed.
- PR #3 merge or publication authorization: not granted.

## Status

The PCI DSS v4.0.1 English Markdown master passes the technical/editorial source gate. This status does not constitute a PCI DSS assessment, compliance validation, legal conclusion, accessibility certification, translation approval, generated-document layout approval, or publication authorization.
