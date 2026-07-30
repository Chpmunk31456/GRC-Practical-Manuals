# Chapter 81 — Privacy by Design and Data Minimisation

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 81 draft language.

## Requirement

AI systems that process personal data must embed privacy and data-protection principles into design, development, configuration, deployment, monitoring, and retirement. Personal data must be adequate, relevant, and limited to what is necessary for the documented purpose, while AI Act data-governance, accuracy, risk-management, and evidence requirements are met.

## Plain-English explanation

More data is not automatically better or lawful. Teams must justify why each data element, feature, prompt field, log, annotation, and retention period is needed. Privacy-enhancing design must be considered before collection and before model or workflow changes, not added only after deployment.

## Design controls

The organization should implement:

1. documented purpose and necessity tests for each personal-data element;
2. feature and proxy-variable review;
3. collection and retention limits;
4. role-based access and least privilege;
5. pseudonymisation, aggregation, masking, or synthetic data where appropriate;
6. separation of training, validation, testing, and production data;
7. privacy-preserving logging and monitoring;
8. controls against unintended memorisation, disclosure, or re-identification;
9. deletion, correction, restriction, and portability workflows where applicable;
10. reassessment after new data sources, features, model updates, integrations, or purposes.

## GlobalWay example

GlobalWay's travel-assistance system does not retain passport numbers, payment-card data, or health information in prompts merely because those fields exist in upstream systems. The design review confirms which attributes are necessary, masks sensitive values, limits log content, and sets retention periods aligned with legal and operational needs.

## Control activity

Privacy Engineering and AI Governance must approve a privacy-by-design review before production release and after material changes. The review must document necessity, proportionality, minimisation decisions, technical safeguards, residual risks, and unresolved trade-offs.

## Evidence

- data inventory and flow map;
- purpose and necessity assessment;
- feature-selection rationale;
- retention schedule;
- access-control design;
- pseudonymisation or masking evidence;
- privacy test results;
- deletion and rights-handling procedures;
- design-review approvals and change history.

## Audit test

Select a sample of AI data elements, features, prompts, and logs. Confirm that necessity was documented, excessive or stale data was removed, safeguards operate as designed, and material changes triggered renewed review.

## Primary legal references

- Regulation (EU) 2016/679: Articles 5(1)(c), 25, and 32, with other provisions as applicable.
- Regulation (EU) 2024/1689, as amended: Articles 9, 10, 12, 15, 26, and Annex IV as applicable.
- Current consolidated EUR-Lex texts control over summaries and earlier drafts.
