# Manual 42 — Canada Privacy Authoritative Source State

**Series order:** 42  
**State:** authoritative-source verification / controlled architecture preparation; not controlled-English master and not publication authorization  
**Verification date:** 2026-08-31

## Source decision

Manual 42 must not present “Canada privacy” as one uniform private-sector statute. The controlled source model is layered by jurisdiction and organizational context.

### Federal private sector — PIPEDA

The federal Personal Information Protection and Electronic Documents Act (PIPEDA), S.C. 2000, c. 5, remains the controlling federal private-sector baseline for personal information handled in the course of commercial activities where PIPEDA applies. The Justice Laws site states that PIPEDA is current to 2026-06-21 and was last amended on 2025-03-04.

Official source: https://laws-lois.justice.gc.ca/eng/acts/P-8.6/

For breach handling, section 10.1 requires an organization to report a breach of security safeguards involving personal information under its control to the Privacy Commissioner of Canada where it is reasonable in the circumstances to believe the breach creates a real risk of significant harm to an individual. The report must be made as soon as feasible after the organization determines that the breach occurred.

Official section 10.1 source: https://laws-lois.justice.gc.ca/eng/acts/P-8.6/section-10.1.html

Operational guidance and enforcement material from the Office of the Privacy Commissioner of Canada (OPC) may be used as guidance and current regulator context, but must not be represented as statutory text.

Official regulator: https://www.priv.gc.ca/

### Federal public sector — separate boundary

The federal Privacy Act governs federal government institutions and is a separate legal regime from PIPEDA. Manual 42 must not merge federal public-sector obligations with private-sector PIPEDA obligations. Public-sector breach and privacy-management requirements should be treated as a separate overlay when included.

Official source: https://laws-lois.justice.gc.ca/eng/acts/P-21/

### Provincial private-sector laws

PIPEDA applicability must be assessed together with provincial private-sector privacy laws and the federal “substantially similar” framework. Provincial rules must not be collapsed into a single Canada-wide control statement.

#### Québec

For Québec private-sector organizations, use the Act respecting the protection of personal information in the private sector and current Commission d’accès à l’information (CAI) materials as the controlling provincial source set. Law 25 amendments and phased effective dates must be handled through the current consolidated law and regulator guidance rather than by treating “Law 25” as a standalone perpetual rule text.

Official consolidated legislation: https://www.legisquebec.gouv.qc.ca/en/document/cs/P-39.1

Official regulator: https://www.cai.gouv.qc.ca/

#### Alberta

For Alberta private-sector organizations, use Alberta’s Personal Information Protection Act (PIPA) and its regulations as the provincial private-sector baseline. Alberta government guidance explicitly distinguishes PIPA from public-sector privacy law and directs users to official statutes and regulations for interpretation.

Official government PIPA portal: https://www.alberta.ca/personal-information-protection-act

Official Alberta King’s Printer legislation should control where guidance and statutory text differ.

#### British Columbia

For British Columbia private-sector organizations, use British Columbia’s Personal Information Protection Act and current Office of the Information and Privacy Commissioner for British Columbia guidance as the provincial source set.

Official legislation: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/03063_01

Official regulator: https://www.oipc.bc.ca/

### Transfers and cross-border processing

Manual 42 must not state that Canadian privacy law generally requires data localization. Cross-border transfers, service-provider processing, accountability, transparency, contractual safeguards, and sector-specific restrictions must be assessed under the applicable federal/provincial regime and any sector overlay. A transfer must not be represented as automatically prohibited merely because processing occurs outside Canada.

### Consent and lawful handling

Consent requirements, permitted handling without consent, purpose limitation, reasonable-purpose tests, access/correction rights, retention, safeguarding, transparency, complaint rights, and accountability must be mapped separately to the applicable statute. Any summary must preserve jurisdiction-specific differences.

### Sector overlays

Health, financial-services, telecommunications, employment, consumer, public-sector, and other sector-specific privacy or confidentiality regimes may add or displace requirements. Manual 42 must identify such overlays as applicability questions rather than silently treating the general private-sector framework as exhaustive.

## Current-state evidence

As of this source-state verification:

- PIPEDA remains in force on the federal Justice Laws site and includes mandatory breach reporting under section 10.1 for breaches creating a real risk of significant harm.
- OPC materials remain the current federal regulator guidance/enforcement source for PIPEDA.
- Québec, Alberta, and British Columbia continue to maintain distinct private-sector privacy regimes that must be analyzed separately from federal PIPEDA.
- Alberta’s public-sector privacy framework changed in 2025: the Protection of Privacy Act came into force on June 11, 2025, replacing the former FOIP privacy framework for Alberta public bodies. This change must not be confused with Alberta private-sector PIPA.

## Controlled architecture requirements

The later 32-chapter Manual 42 architecture must, at minimum, separate:

1. Canadian privacy-law jurisdiction map;
2. organization and activity applicability analysis;
3. federal PIPEDA baseline;
4. federal public-sector Privacy Act boundary;
5. Québec private-sector requirements;
6. Alberta private-sector requirements;
7. British Columbia private-sector requirements;
8. provincial/federal interaction and substantially-similar analysis;
9. personal-information inventory and classification;
10. accountability and privacy-management governance;
11. purposes and collection limitation;
12. consent and permitted exceptions;
13. notice and transparency;
14. access and correction rights;
15. use and disclosure controls;
16. service providers and processors;
17. cross-border transfers and transparency;
18. security safeguards;
19. breach triage and real-risk-of-significant-harm analysis;
20. regulator and individual notification workflows;
21. breach records and evidence;
22. retention and disposal;
23. children, vulnerable individuals, and high-risk contexts;
24. employee and workforce information;
25. automated decision/AI privacy interfaces;
26. privacy impact and risk assessment;
27. vendor and third-party governance;
28. complaints, investigations, and regulator engagement;
29. sector overlays and legal-conflict handling;
30. evidence architecture and audit readiness;
31. legal/regulatory change watch and reassessment;
32. localization, provenance, accessibility, artifact QA, and release controls.

## Fail-closed controls

Before controlled-English freeze:

- reverify PIPEDA, Privacy Act, Québec, Alberta, and British Columbia authoritative statutory/regulatory state;
- verify any substantially-similar designation relied upon in applicability analysis;
- distinguish binding law from regulator guidance and enforcement interpretation;
- avoid unsupported national generalizations where provincial law differs;
- verify breach-reporting thresholds, timing, recordkeeping, and notification requirements separately by jurisdiction;
- verify current cross-border-transfer guidance before describing notice, consent, contractual, or accountability expectations;
- preserve original explanatory language and do not reproduce protected source text beyond permitted quotation limits;
- identify any genuine-human legal/semantic review competency before candidate generation under the project’s canonical review-preflight control.

## Publication boundary

This file advances Manual 42 only to authoritative-source-state / controlled architecture preparation. It does not authorize controlled-English freeze, localization, candidate generation, staging, catalog promotion, or publication. Sequential predecessor and all normal release controls remain in force.