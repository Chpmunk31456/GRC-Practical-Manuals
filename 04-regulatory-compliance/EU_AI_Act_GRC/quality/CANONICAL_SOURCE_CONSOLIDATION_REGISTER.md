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
| Chapter 71 | `chapters/71_AI_Vendor_Due_Diligence_CORRECTED_MASTER.md` | `71_AI_Vendor_Due_Diligence.md`; `71_AI_Vendor_Due_Diligence_and_Contractual_Assurance.md` | Preserve detailed drafts until mapped operational content is integrated into Chapters 71–79 and Appendices O/P | Full source comparison completed; canonical identity confirmed; combined draft overlaps Chapters 72–79 | Comparison `d8e6927ab1624acf6e939c9f66801ef559b4a50d` |
| Chapter 72 | `chapters/72_Contract_Clauses_CORRECTED_MASTER.md` | `72_AI_Contract_Clauses_and_Allocation_of_Responsibilities.md`; `72_AI_Contracting_and_Compliance_Clauses_CORRECTED_MASTER.md` | Preserve until useful material is integrated | Full source comparison completed; canonical identity and legal modality confirmed | Comparison `4055dfe809c20b6d6b9fba11d22ce80d424cf7f7` |
| Chapter 73 | `chapters/73_Provider_Documentation_Review_CORRECTED_MASTER.md` | `73_Provider_Documentation_Review.md`; `73_Ongoing_Supplier_Oversight_CORRECTED_MASTER.md` | Preserve detailed draft; remap supplier oversight to Chapter 78 review | Canonical identity confirmed | Comparison `c567e72cac3e2442cd0645da909363ae38e280a2` |
| Chapter 74 | `chapters/74_Model_Cards_System_Cards_and_Limitations_CORRECTED_MASTER.md` | `74_Model_Cards_System_Cards_and_Limitations.md`; `74_Audit_Assurance_and_Evidence_Access_CORRECTED_MASTER.md` | Preserve detailed draft; compare assurance alternate against Chapter 75/assurance chapters | Canonical identity confirmed | Comparison `c567e72cac3e2442cd0645da909363ae38e280a2` |
| Chapters 75–84 | Corresponding `*_CORRECTED_MASTER.md` files | Earlier numbered and alternate drafts | Preserve pending archive and migration review | Canonical batch verified | `4ffec5a66d67e54ef2edfefceb9174b1652b7e7d` |
| Chapters 85–94 | Corresponding `*_CORRECTED_MASTER.md` files | Earlier numbered drafts | Preserve pending archive review | Canonical batch verified | `775c31a02feb9f5fabc2d8988db5644fa26aaca3` |
| Chapters 95–104 | Corresponding `*_CORRECTED_MASTER.md` files | Earlier numbered drafts | Preserve pending archive review | Canonical batch verified | `66e2d1b92c4693ebc8194748e4223ef02723f4a0` |
| Chapters 105–114 | Corresponding `*_CORRECTED_MASTER.md` files | Earlier numbered drafts | Preserve pending archive review | Canonical batch verified | `55c7cec2409bf32d23c8077ece167ef843da9ab8` |
| Chapters 115–124 | Corresponding `*_CORRECTED_MASTER.md` files | Earlier numbered drafts | Preserve pending archive review | Canonical batch verified | `d2feb572caa757f7f9035ef484f6f79becd1c7dc` |
| Chapters 125–134 | Corresponding `*_CORRECTED_MASTER.md` files | Earlier numbered drafts | Preserve pending archive review | Canonical batch verified | `7685b35fd1a17a3ee1961611568ab96c02514e21` |
| Chapters 135–138 | Corresponding `*_CORRECTED_MASTER.md` files | Earlier numbered drafts | Preserve pending archive review | Canonical batch verified | `e7b17ddf3ea7e80f1138fa7f7e2680283fbf9e17` |
| Appendices A–Z | Corresponding `Appendix_*_CORRECTED_MASTER.md` files | Earlier appendix drafts | Preserve pending draft comparison, archive manifest, and link validation | First-pass legal audit and corrected-master creation completed for all 26 appendices | Audit index `67c981275458e5b6028681b6dc6dd1772e4f6aaf`; audits `faf10f91759e994547a5aa4068d36b591f473a03`, `4d0c09e33390f50d8c07b5b5d1a79adda3fb79c2`, `869eb66ceef1f8efa80a6b41dfffd70fb97cb991` |
| Foundation legal timeline | `quality/FOUNDATION_TIMELINE_AND_SOURCE_REGISTER_CORRECTION.md` plus controlling README references | Older timeline statements in `EU_AI_Act_GRC_Manual_Foundation.md` | Direct integration still required | Correction package created; source foundation not yet replaced | `f630fff19cb432d6b60d2d9cbb202093829ba566` |

## Known unresolved consolidation items

1. Compare Chapter 75–79 supplier-governance alternates and originals against canonical files and preserve nonduplicative content.
2. Migrate and verify useful operational content identified in the Chapter 71–74 comparison records.
3. Review every remaining original chapter and appendix file against its corrected master before archive or deletion.
4. Identify and resolve all zero-content and truncated legacy files.
5. Reconcile overlapping legal-audit reports, including Chapter 77–91 and Chapter 92–103 records.
6. Integrate the foundation legal correction directly into `EU_AI_Act_GRC_Manual_Foundation.md` after complete replacement review.
7. Validate chapter-to-appendix and appendix-to-chapter cross-references using corrected paths.
8. Create an archive manifest before any deletion or archival movement.
9. Conduct whole-English editorial, terminology, graphics, accessibility, and publication-layout review.

## Deletion gate

No deletion is authorized merely by inclusion in this register. Deletion or archival movement requires:

- source comparison completed;
- useful content preserved;
- legal and editorial verification completed;
- canonical path confirmed;
- commit SHA recorded;
- no broken links or references introduced.
