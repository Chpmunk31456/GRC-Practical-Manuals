# Manuals 14–45 — Anti-Halt Parallel Preflight Matrix

**Status:** ACTIVE PARALLEL PREFLIGHT / RESEARCH-ARCHITECTURE / NOT RELEASE AUTHORIZATION  
**Preflight date:** 2026-08-29; live-state reconciliation: 2026-08-30  
**Base:** current `main` after Manual 13 publication reconciliation through PR #194 and rolling downstream advancement through PR #201. **Manual 13 is published. Manual 14 is front-of-line.**  

This matrix exists to eliminate idle cycle time while preserving sequential publication and fail-closed substantive controls. It does not claim that any downstream manual is release-ready. Each manual must later receive current authoritative-source verification, controlled build, exact-head QA, durable artifacts, provenance, workflow-security checks, localization, substantive review where explicitly required, changed-scope reconciliation, and sequential predecessor clearance.

## Shared preflight requirements for every downstream manual

1. Identify authoritative primary sources and classify each as law/regulation, regulator guidance, standard/framework, audit criteria, or professional-practice reference.
2. Record source-state watch items: effective dates, amendments, pending replacement standards, proposed rules, jurisdiction transitions, and publication-version dependencies.
3. Define legal/standards boundaries so guidance is not represented as binding law and crosswalks are not represented as equivalence or certification.
4. Define controlled English architecture, evidence model, Essential / Structured / Enhanced implementation paths, assessment procedures, failure modes, and scenario training.
5. Pre-stage es-419 and pt-BR terminology architecture without claiming semantic approval.
6. Pre-stage accessible graphics requirements, text equivalents, captions, figure references, tables, links, metadata, language tags, bookmarks, reading order, and rendered-page QA criteria.
7. Pre-stage publication package, manifest, SHA-256 checksums, provenance, exact-head checks, repository/workflow-security checks, and durable-artifact requirements.
8. Retain genuine-human legal/editorial/technical, localization-semantic, accessibility/visual, and changed-scope gates wherever the repository control explicitly requires human judgment.
9. Publication order remains sequential; research/build work may proceed in parallel.

## Parallel queue and source-target preflight

| Manual | Topic | Primary authoritative-source targets to verify at build/release time | Principal preflight risk/watch item |
|---|---|---|---|
| 14 | PCI DSS 4.x | PCI Security Standards Council current PCI DSS standard, document library, FAQs and program guidance | exact current PCI DSS revision/effective dates; distinguish standard from SAQ/program guidance |
| 15 | SOC 2 | AICPA Trust Services Criteria and SOC reporting guidance | copyrighted criteria; distinguish readiness guidance from CPA attestation requirements |
| 16 | ISO/IEC 27001 & 27002 | ISO official standard records and applicable ISO/IEC guidance; accreditation/certification references only when authoritative | edition/amendment status; copyright boundaries; certification vs implementation distinction |
| 17 | NIST Privacy Framework | NIST Privacy Framework official publication and NIST implementation resources | framework-version currency and any transition to newer NIST privacy guidance |
| 18 | GLBA / FTC Safeguards Rule | U.S. Code / official statutory text, FTC Safeguards Rule, FTC official guidance | institution scope, regulator overlap, amendment/effective-date state |
| 19 | FedRAMP / FISMA | FedRAMP official authorization requirements, NIST RMF/SP 800-53 sources, OMB/CISA/Federal policy as applicable | FedRAMP revision/version migration; agency-policy vs statutory distinction |
| 20 | CIS Controls | Center for Internet Security current CIS Controls publication and official implementation resources | current control version; safeguard mapping drift |
| 21 | OT/ICS Security | NIST SP 800-82 current revision; ISA/IEC 62443 official standard records and permitted references | industrial-safety boundary; copyrighted IEC text; sector-specific overlays |
| 22 | Cloud Security | Cloud Security Alliance CCM official current release and authoritative cloud-control references | CCM version drift; provider-specific mappings are implementation aids only |
| 23 | DORA | EUR-Lex Regulation (EU) 2022/2554, delegated/implementing acts, ESA official materials | regulatory technical standards and implementing acts continue to evolve |
| 24 | NIS2 | EUR-Lex Directive (EU) 2022/2555 plus official national transposition sources when jurisdiction-specific | directive vs national transposition; member-state divergence |
| 25 | ISO 22301 | ISO official ISO 22301 record and related authorized references | edition/amendment status and copyright boundaries |
| 26 | Incident Response & Cyber Crisis Management | NIST incident-response guidance, CISA resources, applicable regulator requirements by context | avoid treating voluntary guidance as universally mandatory |
| 27 | Data Governance & Privacy Engineering | NIST privacy engineering/risk resources, applicable regulator/privacy-authority sources, recognized governance references | separate governance practice from jurisdiction-specific legal obligations |
| 28 | AI Privacy & Automated Decision Governance | EU AI Act/EUR-Lex, privacy regulators, NIST AI RMF/GenAI Profile, jurisdictional automated-decision rules | rapidly changing ADMT/AI rules; exact-date jurisdiction verification mandatory |
| 29 | Software / AI Supply Chain and Component Assurance | NIST SSDF, CISA secure-by-design/supply-chain resources, NTIA/SBOM sources, applicable AI supply-chain guidance | SBOM/AI-BOM terminology and evolving federal guidance |
| 30 | Enterprise GRC Integration & Crosswalks | source manuals and original authoritative frameworks referenced by each crosswalk | crosswalks must never imply legal equivalence, certification, or full control equivalence |
| 31 | NYDFS 23 NYCRR Part 500 | New York DFS official Part 500 regulation and cybersecurity resources | phased amendment dates and covered-entity/class A distinctions |
| 32 | FFIEC | FFIEC official handbooks/catalog, federal banking regulator materials | handbook replacement/state changes; regulator-specific applicability |
| 33 | SEC Cybersecurity Governance and Disclosure | SEC final rules, official adopting releases, forms and interpretive materials | disclosure-rule amendments/litigation/status; issuer vs investment-adviser regimes |
| 34 | ISO/IEC 27701 | ISO official standard record and related authorized references | edition transition and alignment to ISO/IEC 27001:2022; copyright boundaries |
| 35 | HITRUST CSF | HITRUST official CSF and assurance-program materials | licensing/copyright; certification/assessment program versioning |
| 36 | Brazil LGPD | Planalto statutory text, ANPD regulations/guidance and official government sources | ANPD rule updates; legal bases, DPO and international-transfer developments |
| 37 | Colombia Data Protection / Habeas Data | Colombian statutes/decrees, SIC official regulations/guidance and authoritative government sources | law/decree/SIC guidance hierarchy; sector overlays |
| 38 | FERPA | U.S. Code/CFR and U.S. Department of Education official FERPA resources | education-record scope, school-official exceptions and state-law overlays |
| 39 | COPPA | 15 U.S.C. statutory basis, FTC COPPA Rule and FTC official guidance | rule amendments/effective dates and age/scope changes |
| 40 | CJIS Security Policy | FBI CJIS official current Security Policy and companion resources | policy-version currency; agency implementation overlays |
| 41 | UK GDPR / Data Protection Act | legislation.gov.uk, ICO official guidance, retained/UK GDPR sources | UK data-law reform status and effective-date transitions |
| 42 | Canada Privacy | Justice Laws PIPEDA text, OPC official guidance, successor federal legislation if enacted | legislative replacement risk; federal/provincial split |
| 43 | ISO/IEC 27017 & 27018 | ISO official standard records and authorized references | edition status; cloud provider/customer role distinction; copyright boundaries |
| 44 | NIST SSDF / SP 800-218 | NIST SP 800-218 and official NIST secure-software resources | revision/version state; federal procurement overlays must be separately sourced |
| 45 | Enterprise Compliance Training Capstone | authoritative sources already verified for Manuals 01–44 | no new legal equivalence claims; scenarios must preserve each source manual’s scope and jurisdiction boundaries |

## Parallelization depth targets — reconciled 2026-08-30

- **Manual 14:** front-of-line controlled build/release lane — PCI DSS source-state verification is active; complete controlled English source, localization, exact-head QA, rendered candidates, durable artifacts, provenance, and release reconciliation.
- **Manual 15:** active QA lane behind Manual 14; no publication bypass.
- **Manual 16:** active QA lane behind Manual 15; no publication bypass.
- **Manual 17:** active controlled-build lane; no publication bypass.
- **Manual 18:** next pre-stage lane — GLBA / FTC Safeguards Rule source inventory, regulator-overlap boundaries, amendment/effective-date watch, localization architecture, evidence model, and publication-preflight controls.
- **Manuals 19–20:** early preflight lane — source inventory, version-watch, dependency mapping, shared tooling requirements.
- **Manuals 21–30:** architecture/research lane — primary-source targets, jurisdiction/standard boundaries, graphics and evidence-model reuse.
- **Manuals 31–45:** research/intake lane — regulatory/standards source targets, currency watch, localization/legal-risk notes and dependency lineage.

## Promotion rule

A downstream manual may advance to deeper build stages whenever safe capacity exists, but no manual may be represented as reviewed, release-ready, or published without its own exact evidence. A blocked front manual never freezes downstream research/build work, and a downstream manual never bypasses sequential publication.
