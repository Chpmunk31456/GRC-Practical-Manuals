# Chapter 117 — Bias, Oversight, and Transparency Testing

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 117 draft language.

## Requirement

Organizations must test bias, human oversight, and transparency to the extent required by their legal role, the AI system’s classification, intended purpose, affected persons, and applicable law. Providers of high-risk AI systems must address data-governance, risk-management, accuracy, human-oversight, transparency, and technical-documentation duties. Deployers must operate systems according to instructions, assign competent human oversight, monitor use, retain relevant logs where applicable, and meet any transparency, fundamental-rights, employment, equality, accessibility, consumer-protection, and data-protection obligations that apply to the use case.

## Plain-English explanation

The EU AI Act does not create a single universal “bias test” for every AI system. It requires different controls depending on actor and risk. A system can appear accurate overall while performing poorly for particular groups or contexts. Human review may exist on paper but fail because reviewers lack time, authority, information, competence, or practical ability to intervene. Transparency can also fail if notices are inaccurate, late, inaccessible, or inconsistent with actual system behaviour.

## Testing requirements

Test, as applicable:

1. the actor, classification, intended purpose, population, and legal trigger;
2. relevance, representativeness, completeness, and suitability of data and test populations;
3. overall and subgroup performance, error distribution, and context-specific failure;
4. proxy variables, indirect discrimination, accessibility barriers, and foreseeable disparate impact;
5. reviewer competence, workload, information, authority, automation bias, and conflicts;
6. override, escalation, stop, appeal, contestability, and safe-fallback mechanisms;
7. disclosure timing, wording, language, accessibility, and delivery channel;
8. consistency between notices, instructions for use, technical documentation, actual operation, and logs;
9. material limitations, foreseeable misuse, and unsupported uses;
10. remediation, retesting, residual-risk treatment, and release or continued-use decisions.

## GlobalWay example

GlobalWay tests a recruitment-screening system across job families, languages, age ranges, disability-related accommodations, and relevant applicant groups. It also observes whether recruiters understand the system’s limitations, challenge recommendations when appropriate, use the override and escalation routes, and provide applicants with legally appropriate information and a practical review process. GlobalWay separately evaluates whether GDPR, equality, employment, and accessibility requirements apply.

## Control activity

Providers and deployers must perform the testing and monitoring necessary for their respective obligations. GlobalWay requires documented bias, oversight, and transparency testing before release or deployment of systems with material human or fundamental-rights impact and after significant changes to data, model, purpose, population, workflow, instructions, or notice design. A failed test must trigger containment, corrective action, reassessment, and retesting before release or continued use unless an authorized and legally supportable interim measure is documented.

## Evidence

- legal-role, classification, and use-case assessment;
- test plan and population rationale;
- data-quality and representativeness evidence;
- overall, subgroup, and outcome metrics;
- oversight simulations and operating observations;
- notice, instruction, accessibility, and comprehension tests;
- limitations, exceptions, and complaints;
- remediation and retest results;
- approval, escalation, and residual-risk records.

## Audit test

Select systems with material human or fundamental-rights impact. Confirm that testing matched the actor and legal trigger, used relevant populations and scenarios, assessed operating effectiveness rather than design alone, documented disparities and oversight failures, tested legally required transparency and accessibility, and verified remediation before release or continued use.

## Primary legal references

- Regulation (EU) 2024/1689, as amended, including Articles 4, 9, 10, 13–15, 26, 27, 50, 72, and 86, as applicable.
- Regulation (EU) 2016/679, including Articles 5, 12–15, 21, 22, 25, and 35–36, where personal data, profiling, or automated decision-making is involved.
- Applicable equality, employment, accessibility, consumer-protection, and sector-specific law.
- Regulation (EU) 2026/1744, where its amendments affect the relevant AI Act obligations or application dates.
- Testing methods in this chapter are operational assurance practices and must not be misrepresented as one universal statutory testing formula.
- Current consolidated official texts control over older summaries and drafts.
