# Chapter 90 — Business Continuity and Disaster Recovery

## Purpose

This chapter establishes business continuity and disaster recovery requirements for AI systems, supporting infrastructure, data, models, vendors, human-review processes, and essential services.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should identify critical AI-supported services, define acceptable disruption and data-loss tolerances, maintain tested fallback and recovery arrangements, and ensure that restoration does not reintroduce unsafe, unlawful, insecure, or unapproved system states.

## Plain-language explanation

Continuity keeps essential work operating during disruption. Disaster recovery restores technology and data after serious failure. AI continuity must include not only servers and backups, but also models, prompts, configurations, vendors, monitoring, human reviewers, decision authority, and safe manual alternatives.

## Business impact analysis

For each AI-supported process, document:

- business service and accountable owner;
- affected persons and potential harm;
- critical dependencies;
- maximum tolerable downtime;
- recovery time objective;
- recovery point objective;
- minimum acceptable service level;
- manual or alternate process;
- legal and contractual obligations;
- priority for restoration.

## Failure scenarios

Plan for:

- model or API outage;
- cloud or network failure;
- corrupted model, prompt, dataset, or configuration;
- cyberattack or ransomware;
- loss of credentials or keys;
- vendor insolvency or service withdrawal;
- unavailable monitoring or logging;
- data-centre or regional outage;
- unavailable trained reviewers;
- unsafe model update;
- widespread incorrect output;
- compromised retrieval or tool integration.

## Continuity strategies

Strategies may include:

- manual processing;
- reduced-function safe mode;
- alternate approved provider;
- prior validated model version;
- static decision rules;
- read-only operation;
- queueing for later human review;
- geographic or infrastructure redundancy;
- offline procedures;
- pre-authorised emergency roles.

Fallback must not silently lower legal, privacy, security, accessibility, or human-oversight standards.

## Recovery controls

Recovery should include:

- protected and tested backups;
- model, prompt, configuration, and dataset versioning;
- infrastructure-as-code or documented rebuild procedures;
- key and credential restoration;
- dependency verification;
- integrity and malware checks;
- validation before service restoration;
- monitoring and logging confirmation;
- human-oversight readiness;
- accountable approval and communication.

## Recovery decision gate

Before restoration, confirm:

- the root cause is understood sufficiently;
- affected artefacts are identified;
- restored versions are approved and intact;
- privacy and security controls operate;
- known critical vulnerabilities are addressed or formally accepted;
- monitoring and rollback are available;
- human reviewers are trained and authorised;
- affected stakeholders receive required communication.

## Exercises

Conduct risk-based exercises covering technical recovery and operational continuity. Include tabletop, failover, backup restoration, vendor outage, corrupted model, unsafe output, manual fallback, communications, and return-to-normal scenarios.

Document objectives, participants, results, deficiencies, owners, deadlines, retests, and management approval.

## Human oversight

During disruption, humans decide whether to suspend, degrade, switch providers, invoke manual processing, restore service, or return to normal operation. Emergency pressure must not allow unreviewed AI decisions to become final.

## GlobalWay Travel Services example

During a major weather event, GlobalWay’s external AI provider becomes unavailable. The company activates a reduced-function mode using verified schedule data and static prioritisation rules.

The system may assemble options, but trained agents approve all itinerary changes. Accessibility and medical-assistance cases are routed to specialists. Recovery to the AI provider occurs only after integrity, monitoring, privacy, and human-oversight tests pass.

## Stop and escalation conditions

Do not restore when:

- backup or artefact integrity is uncertain;
- monitoring and logging are unavailable;
- the cause of compromise remains active;
- an unapproved model or configuration would be used;
- human oversight cannot operate;
- required privacy or security controls are absent;
- rollback is unavailable;
- vendor assurance is materially incomplete.

## Evidence

- business impact analysis;
- continuity and recovery plans;
- dependency map;
- backup inventories and test results;
- recovery procedures;
- fallback operating guides;
- emergency-role assignments;
- exercise records;
- restoration approvals;
- incident communications;
- improvement plans.

## Audit tests

1. Select critical AI services and review impact analyses and recovery objectives.
2. Verify backups include required models, prompts, configurations, data, and evidence.
3. Observe or reperform selected restoration tests.
4. Confirm fallback preserves human review and key controls.
5. Review exercises and overdue improvements.
6. Verify vendor failure and exit scenarios are included.
7. Confirm restoration requires accountable approval and validation.

## Metrics

- critical services with current plans;
- backup and restoration success rate;
- recovery objective achievement;
- exercises completed by risk tier;
- overdue continuity findings;
- time operating in degraded mode;
- restorations completed without full validation;
- vendor dependencies without tested alternatives.

## Management checklist

- Which AI-supported services are critical?
- Can they operate safely without the AI?
- Are backups complete and tested?
- Are people, vendors, models, and data included?
- Is restoration independently validated?
- Can service be rolled back again if recovery fails?

## Figure specification — AI Continuity and Recovery Cycle

Create a formal cycle showing prepare, detect, contain, invoke fallback, recover, validate, approve restoration, monitor, and improve. Show human decision gates before fallback activation and service restoration.

**Alt text:** AI continuity and recovery cycle from preparation and detection through fallback, recovery, validation, human-approved restoration, monitoring, and improvement.
