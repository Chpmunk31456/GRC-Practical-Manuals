# Chapter 59 — Cybersecurity and Incident Reporting for Systemic-Risk GPAI

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 59 draft language.

## Requirement

Providers of general-purpose AI models with systemic risk must ensure an adequate level of cybersecurity protection for the model and its physical infrastructure and must track, document, and report relevant serious incidents and possible corrective measures to the AI Office and, where appropriate, national competent authorities.

## Plain-English explanation

A systemic-risk model can create broad harm if model weights, training infrastructure, deployment systems, or safety controls are compromised. Security must cover the full model lifecycle, including development, training, evaluation, release, access, updates, incident detection, and recovery.

## Cybersecurity control areas

The provider should address:

1. secure development and training environments;
2. identity, access, privilege, and secrets management;
3. protection of model weights, datasets, code, and evaluation assets;
4. software, hardware, cloud, and supply-chain vulnerabilities;
5. adversarial machine-learning threats, including poisoning, extraction, evasion, and prompt-based abuse;
6. logging, monitoring, anomaly detection, and forensic readiness;
7. segmentation, resilience, backup, and recovery;
8. vulnerability disclosure and remediation;
9. third-party and infrastructure-provider coordination;
10. incident classification, escalation, reporting, and corrective action.

## Incident process

The process must define awareness and escalation criteria, causal and impact assessment, preservation of model and infrastructure evidence, reporting responsibilities, authority contacts, initial and supplemental reporting, corrective measures, and post-incident risk reassessment.

## GlobalWay example

GlobalWay requires its systemic-risk GPAI supplier to provide evidence of weight protection, privileged-access controls, security testing, incident notification commitments, and recovery procedures. GlobalWay separately monitors its own API keys, retrieval stores, plugins, prompts, logs, and downstream integrations.

## Control activity

The provider must operate an integrated model-security and incident-management programme with defined severity thresholds, round-the-clock escalation for critical events, protected evidence, and release or service restrictions when risk cannot be adequately controlled.

## Evidence

- cybersecurity architecture and risk assessment;
- access and privilege records;
- model-weight and data-protection controls;
- security and adversarial test results;
- vulnerability and remediation records;
- monitoring and detection evidence;
- incident reports and authority communications;
- corrective-action and recovery evidence;
- post-incident reassessment.

## Audit test

Select a systemic-risk model and a sample of security events. Confirm that controls cover the model and physical infrastructure, events were classified and escalated consistently, evidence was preserved, required reports were submitted, and corrective measures were validated.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: Article 55(1)(c) and (d).
- Current consolidated EUR-Lex text controls over older summaries.
- Applicable Commission and AI Office guidance must be identified as non-binding unless legally adopted.