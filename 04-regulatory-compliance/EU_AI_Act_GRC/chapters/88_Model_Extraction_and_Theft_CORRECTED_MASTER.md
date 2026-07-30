# Chapter 88 — Model Extraction and Theft

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 88 draft language.

## Requirement

Organizations must implement proportionate safeguards against unauthorized model copying, extraction, inversion, weight theft, confidential-system disclosure, and abusive querying that could compromise intellectual property, security, privacy, safety, or regulatory compliance.

## Plain-English explanation

Attackers may recreate model behavior through repeated queries, steal weights or artifacts, infer sensitive training information, or exploit privileged access. Protection requires technical, contractual, monitoring, and incident controls matched to the model's value and risk.

## Control requirements

Implement as appropriate:

1. least-privilege access to weights, checkpoints, code, prompts, and configuration;
2. strong authentication, secrets management, encryption, and environment isolation;
3. query-rate, volume, pattern, and account-abuse controls;
4. anomaly detection for extraction and inversion behavior;
5. output minimisation and confidence-information controls where justified;
6. watermarking, fingerprinting, canary, or provenance techniques where effective;
7. secure distribution and supplier access controls;
8. employee and contractor monitoring consistent with applicable law;
9. evidence preservation, containment, credential rotation, and breach response;
10. legal, contractual, and regulatory escalation.

## GlobalWay example

GlobalWay operates a proprietary travel-pricing model through an API. Monitoring identifies a newly created account making systematic boundary queries at high volume. The account is rate-limited and suspended, logs are preserved, credentials and access paths are reviewed, and the incident is assessed for model theft, privacy exposure, and supplier notification.

## Control activity

Material models must have documented protection requirements before release. Security owners must monitor for extraction indicators, test privileged-access controls, and maintain an incident playbook covering stolen artifacts, exposed endpoints, and suspicious querying.

## Evidence

- model asset classification;
- access-control and privilege records;
- API and rate-limit configuration;
- anomaly-detection rules and alerts;
- extraction test results;
- incident and forensic records;
- credential rotation and containment evidence;
- contractual and legal response records.

## Audit test

Select high-value models and verify that weights and artifacts are access-controlled, endpoints are monitored for extraction behavior, abnormal activity is investigated, incident procedures are tested, and residual risk is documented.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable cybersecurity, robustness, confidentiality, risk-management, monitoring, incident, and systemic-risk provisions.
- Current consolidated EUR-Lex text controls over older summaries.