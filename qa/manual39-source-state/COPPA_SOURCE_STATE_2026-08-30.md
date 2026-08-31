# Manual 39 — COPPA Authoritative Source State

**Manual:** 39 — Children's Online Privacy Protection Act / Rule Controlled Implementation  
**State:** downstream authoritative-source gate only; publication state unchanged  
**Verified:** 2026-08-30/31 UTC against current FTC COPPA rule and 2026 policy materials

## Controlled baseline

The current federal baseline is the **Children's Online Privacy Protection Act (COPPA)** and the FTC's **Children's Online Privacy Protection Rule, 16 CFR Part 312**, as amended by the FTC's final rule published **April 22, 2025**. As of this verification date, the amended rule's general 365-day compliance period has elapsed, so the revised rule is the operative compliance baseline for provisions without earlier special dates.

Manual 39 must preserve the distinction among the statute, 16 CFR Part 312, the 2025 final-rule amendments and Statement of Basis and Purpose, FTC business guidance/FAQs, Safe Harbor program requirements, enforcement matters, policy statements, state children's/privacy laws, and organization-specific implementation practices.

## Scope and applicability boundaries

COPPA applies to covered operators of commercial websites and online services directed to children under 13 and to other covered operators with actual knowledge that they collect personal information from a child under 13. The manual must not generalize COPPA to every service used by minors, every educational technology provider, or every processor of youth data without a supported applicability analysis.

The controlled implementation must distinguish child-directed, mixed-audience and general-audience contexts, actual-knowledge triggers, operator/service-provider roles, and any school/education context without conflating COPPA with FERPA or state student-privacy law.

## 2025 amendment boundary

The April 22, 2025 final rule materially updated the COPPA baseline. The controlled manual must account for, where applicable:

- separate verifiable parental consent for certain disclosures to third parties, including targeted-advertising-related disclosures;
- revised and expanded definitions, including additional identifiers within personal information;
- strengthened data-retention limitations tied to the specific purpose of collection;
- security and integrity requirements for children's personal information;
- increased transparency and reporting obligations for FTC-approved Safe Harbor programs;
- revised notice, parental-choice and consent mechanics reflected in the final rule.

The manual must not preserve superseded pre-2025 assumptions where the amended rule now controls.

## 2026 age-verification policy boundary

In February 2026, the FTC issued a COPPA policy statement describing enforcement discretion for certain age-verification activities when specified safeguards are satisfied. This is an **enforcement-policy statement**, not a replacement for the rule text. The manual must treat it as a dated, change-controlled enforcement position and must not generalize the policy beyond its stated conditions or treat it as a new statutory exception.

The FTC also indicated an intent to review the COPPA Rule regarding age-verification mechanisms. Any later proposed or final amendments must remain change-watch material unless formally adopted and effective.

## Source-layer boundaries

Manual 39 must separately identify:

1. COPPA statutory requirements;
2. binding requirements in 16 CFR Part 312;
3. the 2025 final-rule amendments and effective/compliance dates;
4. FTC guidance, FAQs and small-entity compliance materials;
5. FTC Safe Harbor requirements and approved-program materials;
6. FTC enforcement matters and policy statements, including the 2026 age-verification statement;
7. applicable state children's/privacy laws and education/privacy overlays;
8. organization-specific policies, product decisions, contracts, technical controls and evidence.

Guidance, policy statements and enforcement matters must not be presented as if they were the regulation itself.

## Core implementation boundaries

The controlled manual must correctly scope at least the following areas:

- child-directed and actual-knowledge applicability analysis;
- privacy notice and direct notice to parents;
- verifiable parental consent and separate consent where required;
- parental review, deletion and choice rights;
- collection limitation and data minimization;
- use/disclosure restrictions;
- targeted advertising and third-party disclosure controls;
- retention and deletion requirements;
- reasonable security, confidentiality and integrity safeguards;
- service-provider/third-party due diligence and contractual safeguards where required;
- Safe Harbor participation requirements where applicable;
- records/evidence supporting consent, notice, disclosure, retention and security decisions;
- age-verification controls and any reliance on enforcement-policy conditions.

No blanket claim may be made that every user under 18 is a COPPA child, that all third-party disclosures are prohibited, that all age-verification collection is exempt, or that state youth-privacy requirements are identical to COPPA.

## Primary official sources used for this gate

- FTC — 16 CFR Part 312: COPPA Final Rule Amendments, April 22, 2025: https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-312-coppa-final-rule-amendments
- FTC — COPPA final-rule announcement and amendment summary: https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-changes-childrens-privacy-rule-limiting-companies-ability-monetize-kids-data
- FTC — COPPA compliance FAQs, noting the Rule was amended April 22, 2025: https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions
- FTC — Children's Online Privacy Protection Rule overview: https://www.ftc.gov/legal-library/browse/rules/childrens-online-privacy-protection-rule-coppa
- FTC — February 2026 age-verification enforcement policy statement: https://www.ftc.gov/news-events/news/press-releases/2026/02/ftc-issues-coppa-policy-statement-incentivize-use-age-verification-technologies-protect-children

## Release controls

This source gate is not legal advice, an FTC compliance determination, certification, or audit opinion. Before controlled-candidate freeze and again before release, reverify the current text of 16 CFR Part 312, effective FTC amendments, current FTC FAQs and Safe Harbor materials, the continued status of the 2026 age-verification policy statement, any later COPPA rulemaking, and applicable state-law overlays.

Controlled architecture, full controlled English master, exact English freeze, es-419 and pt-BR localization, deterministic six-binary generation, accessibility/visual QA, provenance/checksums, workflow security, exact-hash substantive human review where required, durable staging, predecessor publication, and catalog/release-registry reconciliation remain fail-closed.

Publication remains strictly sequential behind Manuals 18–38.
