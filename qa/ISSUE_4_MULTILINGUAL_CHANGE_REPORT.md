# Issue #4 Multilingual QA Change Report

## Status

The Spanish and Brazilian Portuguese editions remain machine-assisted drafts. This work does not mark any edition publication-ready.

## Spanish (Latin America)

- **NIST CSF 2.0:** replaced the defective draft with the repository's reviewed chapter blocks; preserved NIST identifiers, official Function labels, localized graphic paths, captions, alt text, and draft status.
- **CIS Controls v8.1, NIST RMF/SP 800-53, ISO/IEC 27001/27002, GDPR, HIPAA, PCI DSS, Incident Response/BCDR, Cloud Security and Compliance, and Third-Party Risk:** localized recurring English table labels and quick-start headings; removed extraction artifacts; repaired mechanically detectable table boundaries.
- **SOC 2 Audit Readiness:** audited; no listed mechanical defect required a source change.

## Brazilian Portuguese

- **NIST CSF 2.0:** replaced the defective draft with the repository's reviewed chapter blocks; preserved NIST identifiers, official Function labels, localized graphic paths, captions, alt text, and draft status.
- **CIS Controls v8.1, NIST RMF/SP 800-53, ISO/IEC 27001/27002, GDPR, HIPAA, PCI DSS, and Third-Party Risk:** corrected recurring English or malformed labels and known machine-translation artifacts.
- **SOC 2 Audit Readiness, Incident Response/BCDR, and Cloud Security and Compliance:** audited; no listed mechanical defect required a source change.

## Automated checks

- Multilingual inventory: all 11 manuals have English, Spanish, and Brazilian Portuguese DOCX/PDF package pairs.
- Batch Markdown QA: 22 localized Markdown files scanned; 22 passed the repository's English-marker, known-defect, alt-text, and malformed-table checks.
- NIST integration validation: all 24 chapters are present once in each localized edition and forbidden terminology is absent.

Automated checks do not constitute human language, legal, technical, accessibility, visual, factual, or publication approval.

## Unresolved human-review items

- **Native-speaker review:** every Spanish and Brazilian Portuguese edition still requires full line-by-line review for idiom, register, regional usage, residual mixed-language prose, and terminology outside the automated marker list.
- **Legal/regulatory review:** GDPR, HIPAA, PCI DSS, ISO/IEC, SOC 2, and related legal or standards descriptions require qualified review against authoritative licensed/current texts.
- **Technical/factual review:** version references, tooling examples, commands, mappings, control interpretations, and operational recommendations require subject-matter validation.
- **Accessibility review:** reading order, heading semantics, table header associations, link purpose, captions, alt-text quality, and color/contrast require human assistive-technology review.
- **Visual publication review:** rebuilt DOCX/PDF files require page-by-page inspection for wrapping, clipping, glyphs, tables, figures, headers, footers, and page breaks.

These items are publication gates, not evidence that any edition is final.
