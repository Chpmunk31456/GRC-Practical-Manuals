# Chapter 97 — Cybersecurity Risk

> **Legal status:** Corrected English master for consolidation. This file controls over conflicting earlier Chapter 97 draft language.

## Requirement

Organizations must identify, assess, mitigate, test, and monitor cybersecurity risks affecting AI systems, models, data, interfaces, infrastructure, users, and dependent services throughout the lifecycle. Controls must address both conventional security threats and AI-specific attack paths.

## Plain-English explanation

AI systems expand the attack surface. Attackers may manipulate prompts, poison data, evade detection, extract models, steal credentials, exploit APIs, compromise dependencies, or induce unsafe tool actions. Security therefore requires coordinated controls across software, models, data, identity, infrastructure, vendors, and operations.

## Assessment requirements

Assess at minimum:

1. assets, trust boundaries, users, privileges, and data flows;
2. prompt injection, indirect prompt injection, jailbreaks, and unsafe tool use;
3. training-data poisoning, retrieval-source manipulation, and feedback-loop abuse;
4. adversarial examples, evasion, model extraction, inversion, and membership inference;
5. secrets, credentials, APIs, plugins, agents, and privileged integrations;
6. confidentiality, integrity, availability, authenticity, and resilience;
7. model, library, container, cloud, and supplier vulnerabilities;
8. logging, detection, incident response, rollback, and evidence preservation;
9. denial of service, capacity exhaustion, and dependency failure;
10. secure development, change control, patching, and vulnerability disclosure;
11. data leakage, model memorisation, output filtering, and access control;
12. material-change and post-incident reassessment triggers.

## GlobalWay example

GlobalWay threat-models a travel-assistance agent that can read itineraries and initiate booking changes. It identifies indirect prompt injection through external content, overprivileged service accounts, sensitive-data leakage, malicious plugins, and model-provider outages. Release is blocked until privilege reduction, content isolation, transaction confirmation, monitoring, and fallback controls are validated.

## Control activity

Material AI systems must pass risk-based security architecture review, threat modelling, secure development, adversarial testing, vulnerability management, and incident-readiness checks before production and after significant change. Critical unresolved findings require documented executive escalation and release prohibition unless a lawful, time-limited exception is approved.

## Evidence

- threat model and attack-surface inventory;
- security architecture and data-flow diagrams;
- secure-development and code-review records;
- vulnerability scans and dependency inventories;
- adversarial and penetration-test results;
- identity, access, and secrets-management evidence;
- monitoring and incident-response procedures;
- remediation, retest, and closure records.

## Audit test

Select material AI systems and verify that threat models cover AI-specific and conventional attacks, controls match actual architecture and privileges, critical findings were remediated and retested, monitoring detects relevant events, and material changes triggered reassessment.

## Primary legal references

- Regulation (EU) 2024/1689, as amended: applicable risk-management, data-governance, accuracy, robustness, cybersecurity, monitoring, incident, and GPAI provisions.
- Applicable Union and Member State cybersecurity and sector requirements.
- Current consolidated official texts control over older summaries.
