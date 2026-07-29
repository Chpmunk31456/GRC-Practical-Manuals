# Chapter 100 — Operational and Resilience Risk

## Purpose

This chapter defines a practical method for assessing and controlling operational and resilience risk arising from AI systems, supporting services, people, processes, vendors, and infrastructure.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should assess whether an AI-enabled business service can continue, degrade safely, recover, and remain accountable during failure, attack, data-quality deterioration, provider outage, model change, unexpected demand, or loss of key personnel. Resilience should be assessed at the business-service level, not only at the technology-component level.

## Plain-language explanation

An AI system may be accurate during normal testing and still create serious operational harm when a supplier API fails, input data becomes stale, demand spikes, a model update changes behavior, or staff cannot switch to a manual process. Operational resilience means understanding which services matter, how much disruption is tolerable, what dependencies exist, and how the organization will continue safely when those dependencies fail.

## Critical-service analysis

For each AI-enabled service, identify:

- business purpose and owner;
- people and customers affected;
- maximum tolerable disruption;
- minimum acceptable service level;
- recovery-time and recovery-point objectives where applicable;
- manual or alternative processing capability;
- critical data, models, prompts, tools, vendors, infrastructure, and personnel;
- safety, privacy, legal, financial, and rights consequences of failure;
- internal and external communications requirements.

## Failure scenarios

Assess at minimum:

- model or application outage;
- cloud, API, network, or identity-provider outage;
- supplier or data-feed failure;
- stale, incomplete, corrupted, or delayed data;
- unexpected model behavior after change;
- loss of logs or monitoring;
- capacity exhaustion and traffic spikes;
- cyberattack or malicious manipulation;
- human-review capacity failure;
- unavailable fallback procedures;
- key-person dependency;
- regional or jurisdictional service disruption;
- backup or restore failure;
- vendor insolvency, suspension, or abrupt service termination.

## Resilience design principles

Resilience controls should support:

- graceful degradation;
- safe failure rather than uncontrolled continuation;
- separation of critical and noncritical functions;
- redundancy where proportionate;
- manual fallback;
- clear stop and restart authority;
- recovery from known-good configurations;
- preserved evidence and logs;
- tested communications and escalation;
- vendor exit and portability;
- post-incident learning.

## Dependency mapping

Map direct and indirect dependencies, including:

- models and model providers;
- training, tuning, and retrieval data;
- cloud, hosting, storage, and network services;
- APIs, plugins, agents, and tools;
- identity and access services;
- monitoring and logging platforms;
- human reviewers and specialist support;
- suppliers and subcontractors;
- contractual rights, licenses, and data-export capabilities.

Identify single points of failure and dependencies whose recovery commitments do not meet business needs.

## Tolerance and recovery decisions

Document:

- impact tolerance;
- trigger for degraded mode;
- trigger for suspension;
- authorized decision maker;
- fallback sequence;
- customer and regulator communication thresholds;
- recovery validation criteria;
- conditions for safe restart;
- residual-risk acceptance.

## Testing expectations

Test resilience through proportionate exercises such as:

- model or API outage simulation;
- corrupted or stale data scenario;
- provider failover;
- manual fallback exercise;
- backup restoration;
- surge-capacity test;
- loss of monitoring;
- compromised credential scenario;
- key-person unavailability;
- vendor exit or data-portability exercise;
- safe shutdown and controlled restart.

Tests should include business owners, operators, technology teams, risk, communications, legal, privacy, security, and relevant vendors.

## GlobalWay Travel Services example

GlobalWay’s AI disruption assistant depends on airline feeds, a cloud model provider, traveler profiles, and a refund-processing API. During a major weather event, demand triples while one airline feed becomes stale. The system continues recommending invalid alternatives.

GlobalWay introduces data-freshness thresholds, a degraded mode that removes uncertain options, clear warnings to consultants, capacity controls, and a manual supplier-verification process. It tests cloud-model failover, restores a known-good configuration, and defines conditions under which the assistant must be suspended while human consultants continue essential service.

## Control activities

- Identify critical AI-enabled business services.
- Define disruption tolerances and minimum service levels.
- Map end-to-end dependencies and single points of failure.
- Design graceful degradation, fallback, and safe-stop controls.
- Test recovery and manual operation regularly.
- Align vendor commitments with business needs.
- Preserve logs and evidence through disruption.
- Review incidents, exercises, and material changes.

## Evidence

- critical-service inventory;
- business-impact analysis;
- dependency maps;
- impact tolerances and recovery objectives;
- continuity and disaster-recovery plans;
- degraded-mode and manual-fallback procedures;
- test plans and results;
- backup and restoration evidence;
- vendor continuity and exit assessments;
- incident records;
- communications plans;
- lessons-learned and remediation records.

## Audit tests

1. Select critical AI-enabled services and confirm impact tolerances are documented and approved.
2. Verify dependency maps include models, data, infrastructure, vendors, tools, and people.
3. Review whether fallback and safe-stop procedures are practical and current.
4. Inspect resilience test results and trace deficiencies to remediation.
5. Confirm recovery objectives align with business and customer needs.
6. Test whether data freshness, monitoring loss, and provider outage can trigger degraded mode or suspension.
7. Review vendor exit, portability, and continuity evidence.

## Metrics

- critical AI-enabled services with approved resilience plans;
- untested fallback procedures;
- recovery-time performance;
- failed or partial resilience tests;
- single points of failure;
- vendor dependencies without viable exit plans;
- incidents caused by stale or unavailable data;
- time spent in degraded mode;
- manual-capacity shortfalls;
- overdue resilience remediation.

## Management checklist

- Which AI-enabled services are operationally critical?
- How long can each service be disrupted?
- Can the service degrade or fail safely?
- Are manual alternatives realistic and tested?
- Are key dependencies and single points of failure known?
- Can the organization recover from a known-good state?
- Are vendor continuity and exit arrangements adequate?

## Figure specification — AI Operational Resilience Lifecycle

Create a lifecycle showing critical-service identification, impact tolerance, dependency mapping, resilience design, exercise, disruption, degraded operation, recovery, safe restart, and lessons learned. Show manual fallback and vendor exit as parallel resilience paths.

**Alt text:** AI operational resilience lifecycle from critical-service identification and impact tolerance through dependency mapping, testing, degraded operation, recovery, safe restart, and lessons learned, with manual fallback and vendor exit paths.