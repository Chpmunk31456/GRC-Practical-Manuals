# Issue #4 Multilingual QA Change Report

## Status

The Spanish and Brazilian Portuguese editions remain machine-assisted drafts. This work does not mark any edition publication-ready.

## Spanish (Latin America)

- **NIST CSF 2.0:** replaced the defective draft with the repository's reviewed chapter blocks; preserved NIST identifiers, official Function labels, localized graphic paths, captions, alt text, and draft status. Added the two missing localized workflow graphics referenced by chapters 19 and 24, bringing each localized edition to eight embedded figures.
- **CIS Controls v8.1, NIST RMF/SP 800-53, ISO/IEC 27001/27002, GDPR, HIPAA, PCI DSS, Incident Response/BCDR, Cloud Security and Compliance, and Third-Party Risk:** localized recurring English table labels and quick-start headings; removed extraction artifacts; repaired mechanically detectable table boundaries.
- **SOC 2 Audit Readiness:** audited; no listed mechanical defect required a source change.

## Brazilian Portuguese

- **NIST CSF 2.0:** replaced the defective draft with the repository's reviewed chapter blocks; preserved NIST identifiers, official Function labels, localized graphic paths, captions, alt text, and draft status. Added the two missing localized workflow graphics referenced by chapters 19 and 24, bringing each localized edition to eight embedded figures.
- **CIS Controls v8.1, NIST RMF/SP 800-53, ISO/IEC 27001/27002, GDPR, HIPAA, PCI DSS, and Third-Party Risk:** corrected recurring English or malformed labels and known machine-translation artifacts.
- **SOC 2 Audit Readiness, Incident Response/BCDR, and Cloud Security and Compliance:** audited; no listed mechanical defect required a source change.

## Automated checks

- Multilingual inventory: all 11 manuals have English, Spanish, and Brazilian Portuguese DOCX/PDF package pairs.
- Batch Markdown QA: 22 localized Markdown files scanned; 11 passed all implemented mechanical checks and 11 were explicitly classified for review because they contain legacy malformed or unresolved image references. The checker now detects malformed image tags and missing local image targets instead of silently treating them as passing.
- NIST integration validation: all 24 chapters are present once in each localized edition and forbidden terminology is absent.
- NIST package validation: both rebuilt DOCX files are valid ZIP/XML packages with eight embedded localized graphics each; both rebuilt PDFs contain searchable text.
- Affected-package rebuild: all 18 localized editions changed by the Issue #4 Markdown corrections were rebuilt locally; DOCX ZIP integrity and searchable PDF content were checked.
- Focused image-tag follow-up: repaired the two unambiguous malformed tags in the Spanish CIS Controls and GDPR editions, rebuilt only those two editions, and confirmed that malformed image-tag counts are now zero. Their unresolved targets (`media/image3.png` and `media/image5.png`) remain explicitly reported as missing; no replacement files or paths were invented.

Automated checks do not constitute human language, legal, technical, accessibility, visual, factual, or publication approval.

## Unresolved human-review items

- **Native-speaker review:** every Spanish and Brazilian Portuguese edition still requires full line-by-line review for idiom, register, regional usage, residual mixed-language prose, and terminology outside the automated marker list.
- **Legal/regulatory review:** GDPR, HIPAA, PCI DSS, ISO/IEC, SOC 2, and related legal or standards descriptions require qualified review against authoritative licensed/current texts.
- **Technical/factual review:** version references, tooling examples, commands, mappings, control interpretations, and operational recommendations require subject-matter validation.
- **Accessibility review:** reading order, heading semantics, table header associations, link purpose, captions, alt-text quality, and color/contrast require human assistive-technology review.
- **Visual publication review:** rebuilt DOCX/PDF files require page-by-page inspection for wrapping, clipping, glyphs, tables, figures, headers, footers, and page breaks.
- **Legacy non-NIST image sources:** 11 localized Markdown files still contain unresolved image references inherited from their machine-generated drafts. The two unambiguous malformed tags were corrected, but their missing targets and the other unresolved references remain listed in the automated report. Those files remain review-gated; this PR does not invent localized artwork or claim the missing source figures are synchronized.

These items are publication gates, not evidence that any edition is final.
