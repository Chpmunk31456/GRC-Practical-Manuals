# Chapter 91 — Red-Team and Penetration-Testing Governance

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 91 draft language.

## Requirement

Organizations must govern AI red-team, adversarial, and penetration-testing activities so that testing is authorized, proportionate, competent, evidence-based, legally compliant, and connected to remediation and release decisions.

## Plain-English explanation

Testing AI systems can reveal security, safety, bias, privacy, manipulation, misuse, and oversight failures. Poorly governed testing can itself expose data, disrupt services, create harmful content, or violate law and contract. Scope, authority, safeguards, evidence, and follow-through must therefore be explicit.

## Governance requirements

Define at minimum:

1. objectives, scope, systems, versions, environments, and prohibited actions;
2. written authorization, rules of engagement, and stop conditions;
3. tester independence, competence, conflicts, and confidentiality;
4. privacy, safety, employment, intellectual-property, and data-handling safeguards;
5. scenarios covering prompt injection, poisoning, evasion, extraction, unsafe tool use, harmful outputs, bias, and control bypass;
6. production-testing restrictions and monitoring;
7. evidence capture, severity criteria, reproducibility, and affected-version identification;
8. remediation ownership, deadlines, compensating controls, and retesting;
9. escalation of critical findings, incidents, or reportable events;
10. closure approval and lessons learned.

## GlobalWay example

GlobalWay authorizes an independent red team to test a travel-assistance agent in an isolated environment. The team evaluates indirect prompt injection, unauthorized booking changes, data leakage, privilege escalation, and safeguard bypass. Critical findings block release until remediation and independent retesting are complete.

## Control activity

Material AI systems must undergo risk-based adversarial testing before release and after significant change. Testing must be governed by approved rules of engagement and linked to vulnerability management, incident response, risk management, technical documentation, and release gates.

## Evidence

- approved test plan and authorization;
- tester qualifications and independence assessment;
- rules of engagement and stop conditions;
- scenarios, methods, and test data;
- findings and severity rationale;
- remediation and compensating controls;
- retest and closure evidence;
- executive escalation records.

## Audit test

Select a sample of red-team and penetration tests. Confirm authorization, scope, competence, safeguards, realistic AI-specific scenarios, evidence quality, timely remediation, independent retesting, and release decisions consistent with unresolved risk.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable risk-management, data-governance, human-oversight, accuracy, robustness, cybersecurity, model-evaluation, adversarial-testing, monitoring, and incident provisions.
- Current consolidated EUR-Lex text controls over older summaries.
- Security testing standards and guidance are non-binding unless incorporated through another binding requirement.