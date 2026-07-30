# EU AI Act GRC Manual — Canonical Source Consolidation Register

**Branch:** `manual/eu-ai-act-grc-compliance`  
**Status:** Active consolidation control  
**Purpose:** Establish one verified canonical English source for every chapter and appendix before publication assembly.

## Control rules

1. No source file is deleted until its content has been compared with the proposed canonical file.
2. Useful content must be preserved before any archive or deletion action.
3. A `_CORRECTED_MASTER.md` file controls over an earlier draft only after verification that it is complete, legally reviewed, and correctly numbered.
4. Zero-content, incomplete, alternate-title, and duplicate-number files remain unresolved until specifically reviewed.
5. This register records the canonical decision, superseded material, action, verification result, and commit evidence.

## Verified canonical decisions

| Item | Canonical source | Superseded or competing files | Action | Verification result | Commit evidence |
|---|---|---|---|---|---|
| Chapter 71 | `chapters/71_AI_Vendor_Due_Diligence_CORRECTED_MASTER.md` | `71_AI_Vendor_Due_Diligence.md`; `71_AI_Vendor_Due_Diligence_and_Contractual_Assurance.md` | Preserve pending archive review | Canonical topic confirmed by approved Chapter 71–79 map | Canonical map commit `4fc812089c5c04122f8015d332da739eb2b0bafa` |
| Chapter 72 | `chapters/72_Contract_Clauses_CORRECTED_MASTER.md` | `72_AI_Contract_Clauses_and_Allocation_of_Responsibilities.md`; `72_AI_Contracting_and_Compliance_Clauses_CORRECTED_MASTER.md` | Preserve pending content comparison | Canonical topic confirmed as Contract Clauses | Canonical map commit `4fc812089c5c04122f8015d332da739eb2b0bafa` |
| Chapter 73 | `chapters/73_Provider_Documentation_Review_CORRECTED_MASTER.md` | `73_Provider_Documentation_Review.md`; `73_Ongoing_Supplier_Oversight_CORRECTED_MASTER.md` | Preserve pending content comparison | Canonical topic confirmed as Provider Documentation Review | Canonical map commit `4fc812089c5c04122f8015d332da739eb2b0bafa` |
| Chapter 74 | `chapters/74_Model_Cards_System_Cards_and_Limitations_CORRECTED_MASTER.md` | `74_Model_Cards_System_Cards_and_Limitations.md`; `74_Audit_Assurance_and_Evidence_Access_CORRECTED_MASTER.md` | Preserve pending content comparison | Canonical topic confirmed as Model Cards, System Cards, and Limitations | Canonical map commit `4fc812089c5c04122f8015d332da739eb2b0bafa` |
| Chapter 75 | `chapters/75_Audit_Rights_and_Incident_Notification_CORRECTED_MASTER.md` | `75_Audit_Rights_and_Incident_Notification.md`; `75_AI_Supplier_Exit_and_Continuity_CORRECTED_MASTER.md` | Preserve pending content comparison | Canonical topic confirmed as Audit Rights and Incident Notification | Canonical map commit `4fc812089c5c04122f8015d332da739eb2b0bafa` |
| Chapter 76 | `chapters/76_Cloud_API_and_Model_Dependency_Risk_CORRECTED_MASTER.md` | `76_Cloud_API_and_Model_Dependency_Risk.md`; `76_Supplier_Change_Notification_and_Reassessment_CORRECTED_MASTER.md` | Preserve pending archive review | Canonical corrected master created and mapped | Commit `010dc2c58174cab23a859fb707084c83bf89bead`; map `4fc812089c5c04122f8015d332da739eb2b0bafa` |
| Chapter 77 | `chapters/77_Open_Source_and_Component_Governance_CORRECTED_MASTER.md` | `77_Open_Source_and_Component_Governance.md` | Preserve pending archive review | Canonical topic and corrected master confirmed | Canonical map commit `4fc812089c5c04122f8015d332da739eb2b0bafa` |
| Chapter 78 | `chapters/78_Ongoing_Vendor_Monitoring_CORRECTED_MASTER.md` | `78_Ongoing_Vendor_Monitoring.md` | Preserve pending archive review | Canonical topic and corrected master confirmed | Canonical map commit `4fc812089c5c04122f8015d332da739eb2b0bafa` |
| Chapter 79 | `chapters/79_Exit_Portability_and_Continuity_Planning_CORRECTED_MASTER.md` | `79_Exit_Portability_and_Continuity_Planning.md` | Preserve pending archive review | Canonical topic and corrected master confirmed | Canonical map commit `4fc812089c5c04122f8015d332da739eb2b0bafa` |
| Chapters 115–138 | Corresponding `*_CORRECTED_MASTER.md` files | Earlier numbered draft files | Preserve pending archive review | Corrected-master legal pass completed through Chapter 138 | Audit commit `a8dbf8ad282bd3a81a3b5ed90e2e63a0d249ecef` |
| Appendix C | `appendices/Appendix_C_Applicability_Assessment_CORRECTED_MASTER.md` | `Appendix_C_Applicability_Assessment.md` | Preserve pending archive review | Corrected master exists; appendix legal audit still required | Commit `a8fc2f947582678a625e7d8c590e100f7bbb8f66` |
| Appendix F | `appendices/Appendix_F_Role_Assessment_Worksheet_CORRECTED_MASTER.md` | `Appendix_F_Role_Assessment_Worksheet.md` | Preserve pending archive review | Corrected master exists; appendix legal audit still required | Commit `6e8850a7893c459d4bdf718db54c92cb0b494817` |
| Foundation legal timeline | `quality/FOUNDATION_TIMELINE_AND_SOURCE_REGISTER_CORRECTION.md` plus controlling README references | Older timeline statements in `EU_AI_Act_GRC_Manual_Foundation.md` | Direct integration still required | Correction package created; source foundation not yet replaced | Commit `f630fff19cb432d6b60d2d9cbb202093829ba566` |

## Known unresolved consolidation items

1. Compare all alternate Chapter 71–76 supplier-governance files against the canonical files and preserve any nonduplicative content in the proper chapter or appendix.
2. Review every original chapter file against its corrected master before archive or deletion.
3. Identify all zero-content and truncated chapter files, including legacy corrected files reported with zero additions.
4. Reconcile overlapping legal-audit reports, especially the overlapping Chapter 77–91 audit and the separate Batch 05 record.
5. Repair and verify the Chapter 92–103 legal-audit record if incomplete.
6. Integrate the foundation legal correction directly into the foundation document after a complete replacement review.
7. Review Appendices A–Z and establish one canonical file for each appendix.
8. Create an archive manifest before any deletion batch.

## Deletion gate

No deletion is authorized merely by inclusion in this register. Deletion or archival movement requires:

- source comparison completed;
- useful content preserved;
- legal and editorial verification completed;
- canonical path confirmed;
- commit SHA recorded;
- no broken links or references introduced.
