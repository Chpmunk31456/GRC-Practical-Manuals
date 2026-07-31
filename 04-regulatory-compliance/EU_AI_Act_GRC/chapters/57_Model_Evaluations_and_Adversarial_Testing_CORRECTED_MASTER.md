# Chapter 57 — Model Evaluations and Adversarial Testing

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 57 draft language.

## Requirement

Providers of general-purpose AI models with systemic risk must perform model evaluations in accordance with standardised protocols and tools reflecting the state of the art, including adversarial testing where appropriate, to identify and mitigate systemic risks.

## Plain-English explanation

Evaluation is not a one-time benchmark exercise. The provider must test what the model can do, where it fails, how it can be misused, how safeguards can be bypassed, and whether new releases or fine-tuning materially change risk. Adversarial testing should include realistic attempts to defeat controls and expose dangerous or unintended capabilities.

## Evaluation programme

The provider should define:

1. evaluation objectives linked to identified systemic risks;
2. capability, safety, security, robustness, misuse, and autonomy test domains;
3. pre-release, post-release, and change-triggered evaluation points;
4. independent or functionally separated testing where proportionate;
5. representative and stress-test scenarios;
6. red-team qualifications, conflict controls, and rules of engagement;
7. severity, exploitability, reproducibility, and residual-risk criteria;
8. remediation, retesting, and release-blocking thresholds;
9. confidential handling of sensitive findings;
10. documentation sufficient for oversight and regulatory review.

## GlobalWay example

Before integrating a systemic-risk GPAI model into its travel-assistance platform, GlobalWay reviews the provider’s evaluation summary, tests prompt-injection resistance, harmful travel-document generation, sensitive-data leakage, false emergency guidance, and safeguards around prohibited content, and records downstream limitations and compensating controls.

## Control activity

The GPAI provider must maintain a documented evaluation and adversarial-testing programme tied to release governance. A release must not proceed where unresolved findings exceed approved risk thresholds or where testing does not cover material identified systemic risks.

## Evidence

- evaluation plan and test catalogue;
- benchmark and scenario rationale;
- adversarial-testing reports;
- red-team qualifications and independence records;
- findings and severity ratings;
- remediation and retest evidence;
- release decision and residual-risk approval;
- post-release evaluation results.

## Audit test

Select a systemic-risk model release. Confirm that evaluations addressed the current risk assessment, included realistic adversarial testing, used defined acceptance criteria, resulted in tracked remediation, and were completed before release approval.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: Article 55(1)(a).
- Current consolidated EUR-Lex text controls over older summaries.
- Applicable Commission and AI Office guidance must be identified as non-binding unless legally adopted.