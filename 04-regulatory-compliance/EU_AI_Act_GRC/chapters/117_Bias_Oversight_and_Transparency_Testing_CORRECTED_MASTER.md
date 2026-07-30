# Chapter 117 — Bias, Oversight, and Transparency Testing

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 117 draft language.

## Requirement

Organizations must test whether AI systems create unjustified performance disparities, whether human oversight works in practice, and whether required information and disclosures are accurate, accessible, timely, and understandable.

## Plain-English explanation

A system can appear accurate overall while performing poorly for particular groups or contexts. Human review may exist on paper but fail because reviewers lack time, authority, information, or training. Transparency notices may also fail if people cannot understand or act on them.

## Testing requirements

Test at minimum:

1. representative and relevant populations and contexts;
2. subgroup performance and error distribution;
3. proxy variables and indirect discrimination risk;
4. reviewer competence, workload, authority, and automation bias;
5. override, escalation, stop, and appeal mechanisms;
6. disclosure timing, wording, accessibility, and channel;
7. consistency between notices, instructions, actual operation, and logs;
8. material limitations and foreseeable misuse;
9. remediation and retesting after failure;
10. residual-risk and release decisions.

## GlobalWay example

GlobalWay tests a recruitment-screening system across job families, languages, age ranges, disability-related accommodations, and applicant groups. It also observes whether recruiters challenge recommendations and whether applicants receive clear notice and a practical review route.

## Control activity

Material AI systems must undergo documented bias, oversight, and transparency testing before release and after significant changes to data, model, purpose, population, workflow, or notice design.

## Evidence

- test plan and population rationale;
- subgroup and outcome metrics;
- oversight simulations and observations;
- notice and accessibility tests;
- identified limitations;
- remediation and retest results;
- approval and residual-risk records.

## Audit test

Select systems with material human or fundamental-rights impact. Confirm that testing used relevant populations and scenarios, assessed operating effectiveness rather than design alone, documented disparities and oversight failures, and verified remediation before release.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: data governance, risk management, human oversight, transparency, accuracy, monitoring, and fundamental-rights provisions.
- Applicable equality, employment, accessibility, consumer-protection, and data-protection law.