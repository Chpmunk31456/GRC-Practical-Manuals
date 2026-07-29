# Chapter 85 — Threat Modelling

## Purpose

This chapter establishes a repeatable threat-modelling process for AI systems, their data, models, prompts, tools, interfaces, infrastructure, users, vendors, and affected persons.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Threat modelling should begin during design, be updated before deployment, and be repeated after material changes, incidents, major vulnerabilities, or changes in intended use.

The process should address confidentiality, integrity, availability, safety, privacy, fundamental rights, misuse, fraud, manipulation, and operational resilience.

## Plain-language explanation

A threat model asks what the system is, what must be protected, who or what could cause harm, how harm could occur, which controls reduce the risk, and who decides whether the remaining risk is acceptable.

## Scope and system boundaries

Document:

- intended purpose and prohibited uses;
- users, affected persons, administrators, reviewers, and third parties;
- models, prompts, datasets, vector stores, tools, APIs, plugins, and agents;
- trust boundaries and data flows;
- external providers and subprocessors;
- deployment environments;
- decision points and human oversight;
- logging, monitoring, fallback, and shutdown mechanisms.

## Assets to protect

Assets may include:

- personal and special-category data;
- proprietary datasets and prompts;
- model weights and fine-tuning artefacts;
- credentials, secrets, and API keys;
- business rules and fare logic;
- audit evidence and logs;
- traveller safety and accessibility information;
- system availability and integrity;
- organizational reputation and legal compliance.

## Threat actors and sources

Consider:

- external attackers;
- malicious or careless insiders;
- customers or users attempting misuse;
- compromised vendors or dependencies;
- poisoned public content;
- automated bots;
- organized fraud groups;
- accidental configuration errors;
- model or data drift;
- natural events and infrastructure failure.

## AI-specific threat scenarios

Threat modelling should consider:

- direct and indirect prompt injection;
- jailbreaks and policy bypass;
- malicious tool invocation;
- excessive agency;
- insecure output handling;
- retrieval poisoning;
- training-data poisoning;
- model extraction or inversion;
- membership inference;
- sensitive-data disclosure;
- adversarial examples;
- hallucinated instructions;
- automation bias;
- compromised model or library supply chains;
- logging gaps and evidence tampering;
- denial of service and resource exhaustion.

## Method

A practical threat model should:

1. define the system and business context;
2. diagram components, data flows, and trust boundaries;
3. identify assets and harm scenarios;
4. identify threat actors and attack paths;
5. rate likelihood, impact, detectability, and exposure;
6. map preventive, detective, responsive, and recovery controls;
7. assign owners and target dates;
8. document residual risk and approval;
9. validate controls through testing;
10. update the model when conditions change.

## Abuse and misuse cases

Document realistic misuse stories, including attempts to:

- obtain confidential traveller information;
- force unauthorised rebooking or refunds;
- manipulate rankings or eligibility decisions;
- bypass human review;
- trigger harmful or discriminatory outputs;
- cause the system to call unauthorised tools;
- poison operational knowledge sources;
- conceal activity from monitoring.

## Human oversight

The threat model must identify where human review can prevent, detect, or contain harm. It should also consider risks created by rushed review, automation bias, poor interfaces, insufficient authority, or lack of training.

## Risk treatment

Each material threat should have:

- control owner;
- treatment decision;
- implementation evidence;
- validation test;
- residual-risk rating;
- accountable approver;
- review date;
- stop or escalation threshold.

## GlobalWay Travel Services example

GlobalWay threat-models an AI rebooking assistant connected to airline inventory, customer profiles, payment services, and an internal knowledge base.

The team identifies an indirect prompt-injection path through malicious text in a supplier advisory. The injected text could instruct the assistant to reveal customer data or call a refund tool.

Controls include content isolation, instruction hierarchy, tool allowlists, transaction limits, confirmation prompts, human approval, output filtering, anomaly detection, and complete logging. The system cannot issue refunds or disclose sensitive records without a human agent’s explicit approval.

## Control activities

- Maintain a threat-modelling standard and template.
- Require diagrams and abuse cases.
- Include privacy, safety, rights, and resilience impacts.
- Validate controls through adversarial testing.
- Link threats to vulnerabilities, incidents, and change management.
- Reassess material changes and new dependencies.

## Evidence

- architecture and data-flow diagrams;
- trust-boundary map;
- asset register;
- threat and abuse-case register;
- risk ratings;
- treatment plans;
- test results;
- approvals and exceptions;
- change-trigger records;
- incident lessons learned.

## Audit tests

1. Select AI systems and verify current threat models exist.
2. Compare diagrams to production architecture.
3. Confirm AI-specific threats and human-oversight failures were considered.
4. Trace high-risk threats to implemented and tested controls.
5. Verify residual risks have accountable approval.
6. Confirm material changes triggered updates.
7. Review whether incidents and vulnerability intelligence feed back into the model.

## Metrics

- systems with current threat models;
- high-risk threats without validated controls;
- overdue treatments;
- material changes without reassessment;
- time from new threat identification to mitigation;
- threat-model findings discovered later in production;
- tested abuse cases by risk tier.

## Management checklist

- Are system boundaries and dependencies accurate?
- Are data, models, prompts, tools, and human decisions included?
- Are realistic misuse and attack paths documented?
- Are controls validated rather than assumed?
- Are residual risks explicitly approved?
- Does the threat model change when the system changes?

## Figure specification — AI Threat-Modelling Flow

Create a formal process diagram showing system context, assets, actors, attack paths, harm scenarios, controls, validation, residual-risk approval, and continuous update. Highlight trust boundaries and human decision points.

**Alt text:** AI threat-modelling flow from system context and assets through attack paths, controls, testing, residual-risk approval, and continuous update, with trust boundaries and human decision points highlighted.
