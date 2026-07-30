# Chapter 52 — Change Management and Substantial Modification

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 52 draft language.

## Requirement

Changes to a high-risk AI system must be assessed before implementation to determine whether they affect intended purpose, regulatory classification, conformity, risk controls, performance, data, human oversight, cybersecurity, documentation, or actor roles. A substantial modification can transfer provider obligations to the modifying actor and may require renewed conformity assessment and related compliance actions.

## Plain-English explanation

Not every patch is a substantial modification, but no material change should be assumed harmless. The legal question is whether the change was foreseen and assessed by the original provider and whether it affects compliance or intended purpose. Technical, business, contractual, data, and operational changes can all matter.

## Change-assessment criteria

Assess at minimum:

1. change to intended purpose, users, affected population, jurisdiction, or decision consequence;
2. retraining, fine-tuning, model replacement, parameter changes, or new retrieval sources;
3. material dataset, feature, threshold, interface, or workflow changes;
4. new integrations, autonomous functions, or downstream uses;
5. changes to accuracy, robustness, cybersecurity, bias, safety, or fundamental-rights risk;
6. changes to human oversight, logging, instructions, or transparency;
7. changes to provider branding, contractual allocation, or operational control;
8. whether the change was foreseen in the original conformity assessment and technical documentation;
9. whether renewed conformity assessment, registration, declaration, marking, notification, or provider-role reassessment is required.

## GlobalWay example

GlobalWay fine-tunes a vendor recruitment model using its own historical applicant data, changes ranking thresholds, and deploys the result under its own brand. The change board does not treat this as routine configuration. It performs a substantial-modification and provider-role assessment, updates the risk and data-governance files, and blocks release until legal and conformity decisions are documented.

## Control activity

Every production change must pass a documented AI change assessment before approval. High-impact changes require legal, compliance, privacy, security, model-risk, and business-owner review. Release tooling must prevent deployment where substantial-modification, role-transfer, conformity, or registration questions remain unresolved.

## Evidence

- change request and technical description;
- before-and-after intended-purpose analysis;
- substantial-modification assessment;
- provider-role reassessment;
- updated risk, data, oversight, and cybersecurity evidence;
- regression, subgroup, and safety testing;
- conformity and registration decisions;
- updated technical documentation and instructions;
- release approval and rollback plan;
- post-change monitoring results.

## Audit test

Select a sample of significant changes. Confirm that the organization assessed intended purpose, foreseeability, compliance impact, role transfer, and conformity consequences before release; verify that testing and documentation match the deployed version; and confirm that post-change monitoring was performed.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: Article 3 definition of substantial modification, Article 25, and applicable conformity, registration, technical-documentation, and post-market provisions.
- Current consolidated EUR-Lex text controls over older summaries.
- Commission guidance on substantial modification must be identified as non-binding unless and until formally adopted with binding effect.
