# Changelog

All notable updates to the GRC Practical Manuals collection will be recorded in this file.

This project uses version numbers such as:

- v1.0 — Initial release
- v1.1 — Minor corrections or additions
- v2.0 — Major revision or restructuring

---

## [1.7] — 1 August 2026

### Added

- Published the GRC Policy Template Toolkit.
- Added four controlled English implementation chapters, a combined English Markdown master, Microsoft Word edition, searchable PDF, source assembly records, QA reports, and SHA-256 checksums.
- Added ten controlled English policy templates and ten editable policy-template DOCX files covering information security, access control, acceptable use, incident response, business continuity and disaster recovery, third-party and vendor risk, data protection and privacy, change management, vulnerability and patch management, and logging and monitoring.
- Added a 25-field policy register, a 25-field policy exception tracker, and a 33-field policy adoption and review checklist.
- Added Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) machine-assisted publication candidates in Markdown, DOCX, and searchable PDF formats.

### Validated

- English controlled assembly, combined DOCX ZIP integrity, searchable-PDF text, ten editable DOCX templates, drafting safeguards, controlled placeholders, and all three CSV schemas passed automated validation.
- Both localized editions passed level-one and level-two heading parity, protected-token restoration, DOCX ZIP integrity, searchable-PDF, page-count, extracted-word, and checksum checks.
- Spanish package: 29 PDF pages and 7,108 extracted words.
- Brazilian Portuguese package: 29 PDF pages and 6,842 extracted words.

### Changed

- Updated the root repository catalog and the Templates and Tools index.
- Advanced the repository version from 1.6 to 1.7.
- Identified control-mapping resources as the next planned Section 08 workstream.
- Removed temporary English and localized policy-toolkit workflows after successful publication.

### Limitations

- Native-language editorial approval, organization-specific legal or regulatory review, privacy and labor review, standards certification, assistive-technology testing, and full page-by-page human visual review are not represented as completed.

---

## [1.6] — 1 August 2026

### Added

- Published the Audit Readiness and Remediation Management Practical Manual.
- Added six controlled English chapters, an English Markdown master, Microsoft Word edition, searchable PDF, source assembly records, QA reports, and SHA-256 checksums.
- Added a 42-field audit-readiness assessment tracker, a 35-field finding and root-cause register, a 34-field remediation action-plan tracker, and a 29-field closure-validation record.
- Added Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) machine-assisted publication candidates in Markdown, DOCX, and searchable PDF formats.

### Validated

- English assembly, DOCX integrity, searchable-PDF, and template-schema validation completed successfully.
- Both localized editions passed heading parity, protected-token restoration, DOCX ZIP integrity, searchable-PDF, page-count, extracted-word, metadata, and checksum checks.
- Spanish package: 20 PDF pages and 4,829 extracted words.
- Brazilian Portuguese package: 19 PDF pages and 4,705 extracted words.

### Changed

- Updated the root repository catalog and the Templates and Tools roadmap.
- Retained the Policy Template Toolkit as the next planned Section 08 resource.
- Removed temporary English and localized audit-readiness workflows after successful publication.

### Limitations

- Native-language editorial approval, legal or regulatory review, standards certification, formal audit opinion, assistive-technology testing, and full page-by-page human visual review are not represented as completed.

---

## [1.5] — 1 August 2026

### Added

- Published the Evidence Collection and Audit Support Practical Manual.
- Added an English controlled Markdown master, Microsoft Word edition, searchable PDF, source assembly records, QA reports, and SHA-256 checksums.
- Added a 38-field evidence request tracker, a 36-field evidence quality review checklist, a 21-field audit request and response log, and a 32-field corrective-action tracker.
- Added Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) machine-assisted publication candidates in Markdown, DOCX, and searchable PDF formats.

### Validated

- English assembly and package validation completed successfully.
- Spanish and Brazilian Portuguese editions passed heading parity, protected-token restoration, DOCX ZIP integrity, searchable-PDF, page-count, extracted-word, metadata, and checksum checks.
- Spanish package: 16 PDF pages and 3,927 extracted words.
- Brazilian Portuguese package: 16 PDF pages and 3,879 extracted words.

### Updated

- Adopted ISO 19011:2026 as the current management-system audit guidance baseline; the 2018 edition is withdrawn.
- Used NIST SP 800-53A Rev. 5 Release 5.2.0, NIST SP 800-53 Rev. 5 Release 5.2.0, the 2025 GAO Green Book, and the IIA Global Internal Audit Standards as current primary references.

### Changed

- Updated the root repository catalog and the Templates and Tools roadmap.
- Identified the Policy Template Toolkit as the next planned Section 08 resource.
- Removed temporary English and localized evidence-manual workflows after successful publication.

### Limitations

- Native-language editorial approval, legal or regulatory review, standards certification, formal audit opinion, assistive-technology testing, and full page-by-page human visual review are not represented as completed.

---

## [1.4] — 1 August 2026

### Added

- Published the GRC Risk Register and Risk Treatment Practical Manual.
- Added an English controlled Markdown master, Microsoft Word edition, searchable PDF, source assembly records, QA reports, and SHA-256 checksums.
- Added a 41-field risk-register template, a 27-field risk-treatment plan template, and a formal risk-acceptance record.
- Added Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) machine-assisted publication candidates in Markdown, DOCX, and searchable PDF formats.

### Validated

- English assembly and package validation completed successfully.
- Spanish and Brazilian Portuguese editions passed heading parity, protected-token restoration, DOCX ZIP integrity, searchable-PDF, page-count, extracted-word, metadata, and checksum checks.
- Spanish package: 17 PDF pages and 4,051 extracted words.
- Brazilian Portuguese package: 17 PDF pages and 3,964 extracted words.

### Changed

- Updated the root repository catalog and the Templates and Tools roadmap.
- Identified the Evidence Collection and Audit Support Practical Manual as the next planned Section 08 resource.
- Removed temporary risk-register build and localization workflows after successful publication.

### Limitations

- Native-language editorial approval, legal or regulatory review, standards certification, assistive-technology testing, and full page-by-page human visual review are not represented as completed.

---

## [1.3] — 31 July 2026

### Added

- Published the EU AI Act GRC Compliance Manual on the default branch in English, Latin American Spanish (`es-419`), and Brazilian Portuguese (`pt-BR`).
- Added 138 chapters and Appendices A–Z per language, controlled Markdown masters, DOCX and PDF editions, manifests, automated QA reports, PDF metadata, and SHA-256 checksums.
- Added maintainable English and Spanish/Portuguese EU AI Act publication workflows.

### Verified

- Spanish and Brazilian Portuguese automated QA reports have `PASS` status with zero failures.
- Both localized build manifests record 138 chapters, 26 appendices, and 164 source records.

---

## [1.3] — 30 July 2026

### Added

- Published the EU AI Act GRC Compliance Manual in Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`).
- Added controlled Markdown masters, DOCX editions, PDF editions, manifests, automated QA reports, PDF metadata, and SHA-256 checksums for both localized editions.
- Added complete localized source sets covering Chapters 1–138 and Appendices A–Z.

### Validated

- Confirmed structural counts, localized chapter and appendix headings, tables of contents, Figure 12-1, Portuguese Appendix Q, automated QA results, and checksum integrity.
- Merged the validated localized publication packages through pull request #35 into `production/multilingual-grc-editions`.

### Changed

- Updated the root catalog, regulatory-compliance index, EU AI Act manual status, and translation workstream documentation to reflect the published multilingual state.

---

## [Unreleased]

### Changed

- Rebuilt the root README as a concise, clickable catalog.
- Corrected the duplicated cloud and technology risk directory.
- Added section indexes for management systems, assurance and audit, cloud and technology risk, and third-party risk.

### Corrected

- Corrected broken incident-response Word and PDF download links.
- Corrected cloud manual navigation and download links.

### Added

- Added an accessibility statement and document-review workflow.

Planned or in-progress improvements may include:

- Additional GRC manuals
- New templates and checklists
- Updated framework guidance
- Regulatory updates
- Accessibility improvements
- New diagrams and practical examples
- Link corrections
- Formatting improvements

---

## [1.0] — July 2026

### Added

- Master repository structure
- Root README
- Repository license
- Contribution guidelines
- Changelog
- Section-level README files
- Manual-level README files

### Manual Collections Added

#### Foundations

- NIST Cybersecurity Framework 2.0
- CIS Critical Security Controls v8.1
- NIST Risk Management Framework
- NIST SP 800-53

#### Management Systems

- ISO/IEC 27001
- ISO/IEC 27002

#### Assurance and Audit

- SOC 2

#### Regulatory Compliance

- GDPR
- HIPAA
- PCI DSS v4.0.1

#### Operational Resilience

- Incident Response
- Business Continuity
- Disaster Recovery

#### Cloud and Technology Risk

- Cloud Security and Compliance

#### Third-Party Risk

- Third-Party Risk Management
- Cyber Supply Chain Security

### Formats Added

- Microsoft Word editions
- PDF editions
- GitHub README guidance
- Practical manager guidance
- Junior analyst guidance

### Repository Improvements

- Organized manuals by GRC domain
- Added navigation links
- Added educational mission
- Added licensing information
- Added contribution instructions
- Added disclaimers and usage notices

---

## Change Categories

Future updates may use the following categories:

### Added

New manuals, sections, diagrams, tools, templates, or resources.

### Changed

Major revisions to structure, explanations, terminology, or implementation guidance.

### Corrected

Spelling, grammar, formatting, links, citations, or technical corrections.

### Updated

Framework, regulatory, standards, or version updates.

### Removed

Outdated, duplicated, unsupported, or incorrect material.

### Security

Corrections involving security, privacy, ethical use, or risk-management guidance.

---

## Reporting Corrections

Please use GitHub Issues and include:

- Manual name
- Version number
- Page or section
- Description of the issue
- Recommended correction
- Supporting source when available

---

## Author

**Alberto “Al” Leiva**
