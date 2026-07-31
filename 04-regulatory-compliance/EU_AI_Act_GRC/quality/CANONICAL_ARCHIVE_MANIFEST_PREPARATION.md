# EU AI Act GRC Manual — Canonical Archive Manifest Preparation

**Branch:** `manual/eu-ai-act-grc-compliance`  
**Status:** Archive preparation only; no deletion or movement authorized

## Purpose

This register identifies superseded, competing, incomplete, alternate-title, and legacy files that may be archived only after content preservation, legal review, cross-reference validation, and owner-authorized archive execution.

## Archive control rules

1. No file may be deleted merely because a corrected master exists.
2. Every candidate must be compared against the canonical source.
3. Nonduplicative controls, examples, evidence lists, audit tests, clause language, tables, and citations must be migrated before archival.
4. Internal links and references must be tested after any path change.
5. Zero-content or apparently incomplete files must be retained until repository history confirms that no content was lost.
6. Archive execution requires a separate commit and explicit owner authorization where deletion or movement could affect information access.

## Confirmed canonical families

| Scope | Canonical source | Preserved competing material | Current action |
|---|---|---|---|
| Chapters 71–79 | Canonical paths identified in `quality/CANONICAL_SOURCE_CONSOLIDATION_REGISTER.md` | Alternate titles, detailed drafts, and supplier-governance overlaps | Preserve and migrate useful content before archive |
| Chapters 80–114 | Corresponding `*_CORRECTED_MASTER.md` files | Earlier long-form numbered drafts | Preserve pending full source comparison |
| Chapters 115–138 | Corresponding `*_CORRECTED_MASTER.md` files | Earlier numbered drafts, including files previously reported as empty or incomplete | Preserve pending archive verification |
| Appendix C | `appendices/Appendix_C_Applicability_Assessment_CORRECTED_MASTER.md` | `appendices/Appendix_C_Applicability_Assessment.md` | Preserve pending content-delta and link validation |
| Appendix F | `appendices/Appendix_F_Role_Assessment_Worksheet_CORRECTED_MASTER.md` | `appendices/Appendix_F_Role_Assessment_Worksheet.md` | Preserve pending content-delta and link validation |
| Appendices A–Z | Corresponding corrected English masters recorded in the appendix audit index | Original appendix files | Preserve until publication-source map and links are verified |

## Priority archive candidates requiring detailed migration review

### Supplier-governance overlap

- `chapters/71_AI_Vendor_Due_Diligence.md`
- `chapters/71_AI_Vendor_Due_Diligence_and_Contractual_Assurance.md`
- `chapters/72_AI_Contract_Clauses_and_Allocation_of_Responsibilities.md`
- `chapters/72_AI_Contracting_and_Compliance_Clauses_CORRECTED_MASTER.md`
- `chapters/73_Provider_Documentation_Review.md`
- `chapters/73_Ongoing_Supplier_Oversight_CORRECTED_MASTER.md`
- `chapters/74_Model_Cards_System_Cards_and_Limitations.md`
- `chapters/74_Audit_Assurance_and_Evidence_Access_CORRECTED_MASTER.md`
- `chapters/75_Audit_Rights_and_Incident_Notification.md`
- `chapters/75_AI_Supplier_Exit_and_Continuity_CORRECTED_MASTER.md`
- `chapters/76_Cloud_API_and_Model_Dependency_Risk.md`
- `chapters/76_Supplier_Change_Notification_and_Reassessment_CORRECTED_MASTER.md`
- `chapters/77_Open_Source_and_Component_Governance.md`
- `chapters/78_Ongoing_Vendor_Monitoring.md`
- `chapters/79_Exit_Portability_and_Continuity_Planning.md`

### Known alternate-title families

- Chapter 42 human-oversight alternate
- Chapters 64–70 transparency alternate titles
- Chapters 133–138 original and corrected-master pairs
- Any chapter family where both a long-form original and a shorter corrected master remain

### Audit-document overlap

- Overlapping Chapter 77–91 audit records
- Separate Batch 05 audit record
- Chapter 92–103 legal-audit record requiring completeness verification
- Earlier timeline and legal-source reports superseded by the 30 July 2026 correction

## Verification fields required before archive action

| Candidate file | Canonical replacement | Full comparison completed | Useful content migrated | Legal review complete | Cross-references tested | Archive decision | Commit SHA |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Zero-content and incomplete-file control

Files reported by GitHub comparison with zero additions are not automatically empty. Before classification, fetch the current blob and inspect repository history. Record one of:

- valid non-empty file;
- Git LFS or binary artifact;
- placeholder intentionally retained;
- genuinely empty draft superseded by verified content;
- corrupted or inaccessible file requiring owner notification.

## Archive destination

No archive directory is created by this register. A future archive batch should use a controlled path such as:

`04-regulatory-compliance/EU_AI_Act_GRC/archive/superseded-source/<category>/`

The archive must include a README explaining that archived files are noncanonical and retained for provenance only.

## Current decision

No deletion, movement, or archival execution is authorized at this stage. Canonical publication assembly must reference only the verified canonical source map.