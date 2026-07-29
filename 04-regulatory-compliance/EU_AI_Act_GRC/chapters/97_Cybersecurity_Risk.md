# Chapter 97 — Cybersecurity Risk

## Purpose

This chapter defines a practical method for identifying, assessing, treating, monitoring, and evidencing cybersecurity risk across the AI lifecycle.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should assess cybersecurity risk for AI systems in proportion to their purpose, architecture, data, connectivity, autonomy, exposure, affected persons, and consequence of failure. The assessment should cover the model, application, prompts, retrieval sources, tools, interfaces, identities, infrastructure, vendors, operational processes, and human oversight.

## Plain-language explanation

An AI system can be secure at the model layer and still be unsafe because of weak access control, exposed data, insecure plugins, poisoned retrieval content, over-privileged tools, missing logs, or ineffective human review. Cybersecurity risk assessment must therefore examine the complete system rather than treating the model as an isolated component.

## Risk objectives

The assessment should determine whether the organization can:

- prevent unauthorized access, use, modification, disclosure, or destruction;
- protect model, prompt, data, configuration, and system integrity;
- maintain confidentiality of personal, confidential, and proprietary information;
- sustain availability and safe operation under attack or failure;
- detect anomalous, malicious, or unauthorized behavior;
- contain and recover from incidents;
- preserve evidence for investigation and regulatory response;
- prevent security weaknesses from undermining human oversight, fairness, safety, or legal compliance.

## Scope of assessment

Assess the following layers:

1. **Business process** — purpose, decision consequence, manual alternatives, dependency, and criticality.
2. **Model** — source, version, hosting, known limitations, safeguards, evaluation, and update process.
3. **Data** — training, tuning, retrieval, input, output, logs, labels, lineage, quality, and access.
4. **Application** — prompts, orchestration, agents, memory, output handling, APIs, and user interface.
5. **Tools and actions** — transactions, search, code execution, messaging, refunds, bookings, and privileged operations.
6. **Identity and access** — authentication, authorization, segregation of duties, service accounts, secrets, and privileged access.
7. **Infrastructure** — endpoints, networks, cloud services, containers, storage, monitoring, backup, and recovery.
8. **Third parties** — providers, hosting platforms, data sources, open-source components, and support services.
9. **People and governance** — administrators, reviewers, operators, incident responders, approvers, and affected users.

## Threat scenarios

Consider at minimum:

- direct and indirect prompt injection;
- jailbreaks and safeguard bypass;
- malicious retrieval or context content;
- data poisoning and label manipulation;
- model extraction, inversion, and membership inference;
- sensitive-data leakage through outputs, logs, or integrations;
- unauthorized model, prompt, policy, or configuration changes;
- compromised credentials, API keys, service accounts, or secrets;
- insecure tool use and excessive agency;
- privilege escalation and cross-tenant exposure;
- supply-chain compromise;
- vulnerable open-source components;
- denial of service and resource exhaustion;
- monitoring evasion and log manipulation;
- unsafe fallback, rollback, or recovery behavior;
- insider misuse;
- fraudulent or deceptive output designed to influence users or reviewers.

## Assessment factors

Rate risk using documented criteria such as:

- threat likelihood;
- attack surface and internet exposure;
- ease of exploitation;
- attacker capability and access required;
- data sensitivity;
- transaction or action authority;
- scale and number of affected persons;
- safety and fundamental-rights consequence;
- detectability;
- recoverability;
- vendor dependency;
- maturity of preventive, detective, and corrective controls.

## Control expectations

Controls may include:

- secure architecture and threat modelling;
- least privilege and strong authentication;
- secrets management;
- input, retrieval, and output validation;
- tool allow-lists and transaction limits;
- sandboxing and environment separation;
- data minimisation and encryption;
- model and component provenance;
- signed or controlled releases;
- vulnerability and patch management;
- adversarial testing;
- continuous logging and anomaly detection;
- human approval for consequential actions;
- kill switches, rollback, and manual fallback;
- incident response and evidence preservation;
- independent assurance for high-consequence systems.

## Inherent and residual risk

Assess inherent risk before considering controls. Then evaluate control design and operation to determine residual risk. Residual risk decisions should identify:

- risk owner;
- treatment decision;
- control gaps;
- compensating controls;
- target completion date;
- exception expiry;
- accountable approver;
- conditions requiring reassessment.

## Reassessment triggers

Reassess cybersecurity risk after:

- model or provider changes;
- new tools, integrations, data sources, or users;
- material prompt or orchestration changes;
- newly discovered vulnerabilities or attack techniques;
- incidents, near misses, or control failures;
- expansion into new jurisdictions or business processes;
- changes to autonomy or transaction authority;
- significant volume or sensitivity increases;
- changes to fallback, recovery, or oversight arrangements.

## GlobalWay Travel Services example

GlobalWay deploys an AI disruption assistant that reads airline alerts, proposes itinerary changes, and can prepare refund requests. The cybersecurity assessment identifies indirect prompt injection through supplier advisories, over-privileged refund APIs, traveler-data leakage in logs, and weak separation between test and production credentials.

GlobalWay restricts retrieved content to data-only treatment, isolates instructions, reduces API permissions, requires human approval for refunds, tokenizes traveler identifiers in logs, separates environments, and adds prompt-injection monitoring. Residual risk remains elevated until an independent adversarial retest confirms the controls are operating effectively.

## Control activities

- Maintain an AI cybersecurity risk methodology.
- Assess the complete system, not only the model.
- Link threat scenarios to controls and test evidence.
- Record inherent and residual risk separately.
- Require accountable approval for exceptions and residual risk.
- Reassess after material change, incident, or emerging threat.
- Integrate results with lifecycle gates, vendor management, monitoring, and incident response.

## Evidence

- cybersecurity risk assessment;
- architecture and data-flow diagrams;
- threat model;
- asset and dependency inventory;
- access-control matrix;
- vulnerability and patch records;
- adversarial and penetration-test reports;
- logging and monitoring evidence;
- incident and near-miss records;
- remediation plans;
- residual-risk approvals;
- reassessment history.

## Audit tests

1. Select AI systems by risk tier and confirm cybersecurity assessments are complete and current.
2. Verify the assessment covers the model, application, data, tools, infrastructure, vendors, and human processes.
3. Trace priority threat scenarios to implemented controls and test evidence.
4. Review whether privileged actions require appropriate authorization and human approval.
5. Confirm vulnerabilities, incidents, and material changes trigger reassessment.
6. Review residual-risk approvals, exception expiry, and overdue remediation.
7. Test whether logs are sufficient to reconstruct significant security events.

## Metrics

- systems with current cybersecurity assessments;
- critical and high residual risks;
- overdue remediation actions;
- vulnerabilities by severity and age;
- incidents and near misses;
- mean time to detect, contain, and recover;
- adversarial-test coverage;
- privileged AI actions requiring human approval;
- vendor-controlled risks without independent assurance;
- reassessments completed after material change.

## Management checklist

- Does the assessment cover the complete AI system?
- Are AI-specific attack methods included?
- Are data, tools, identities, and vendors assessed?
- Are inherent and residual risk clearly separated?
- Can critical findings block deployment?
- Are high-consequence actions constrained and reviewable?
- Are changes, incidents, and new threats triggering reassessment?

## Figure specification — AI Cybersecurity Risk Assessment Map

Create a layered diagram showing business process, model, data, application, tools, identity, infrastructure, third parties, and people. Overlay major threat paths and show the flow from inherent risk through controls, validation, residual risk, approval, monitoring, and reassessment.

**Alt text:** Layered AI cybersecurity risk assessment map covering business process, model, data, application, tools, identity, infrastructure, third parties, and people, with threat paths and the progression from inherent to residual risk.