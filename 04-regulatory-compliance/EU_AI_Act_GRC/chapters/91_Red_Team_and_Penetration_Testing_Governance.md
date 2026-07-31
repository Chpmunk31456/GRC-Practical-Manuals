# Chapter 91 — Red-Team and Penetration-Testing Governance

## Purpose

This chapter establishes governance for adversarial testing of AI systems, applications, models, prompts, tools, data pipelines, integrations, infrastructure, vendors, and human-control processes.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should conduct risk-based red-team and penetration-testing activities before deployment, after material changes, and periodically during operation. Testing must be authorised, scoped, safe, independent where appropriate, evidence-based, and connected to remediation and accountable risk acceptance.

## Plain-language explanation

Red teaming tests how an AI system may fail, be misused, or cause harm under realistic adversarial pressure. Penetration testing tests whether technical weaknesses can be exploited. Both require formal rules so testing itself does not create uncontrolled legal, privacy, security, safety, or operational risk.

## Governance principles

Testing should be:

- formally authorised;
- proportionate to system risk;
- independent from the builder where consequence warrants;
- based on realistic threat and misuse scenarios;
- performed in controlled environments where feasible;
- designed to protect personal, confidential, and special-category data;
- traceable from finding through validated closure;
- repeated after material remediation or change.

## Scope

Testing may cover:

- prompt injection and jailbreaks;
- malicious or manipulated retrieval content;
- insecure tool use and excessive agency;
- privilege escalation and access control;
- model extraction, inversion, and membership inference;
- data leakage and cross-tenant exposure;
- training and retrieval poisoning;
- adversarial examples;
- unsafe output handling;
- dependency and supply-chain compromise;
- logging and monitoring evasion;
- denial of service and resource exhaustion;
- human-oversight bypass and automation bias;
- fallback, rollback, and kill-switch failure;
- privacy, fairness, accessibility, and fundamental-rights harm.

## Rules of engagement

Document:

- business and technical scope;
- authorised testers;
- systems, environments, accounts, and data;
- permitted and prohibited techniques;
- testing window;
- rate and transaction limits;
- safety and privacy constraints;
- evidence-handling rules;
- monitoring and coordination contacts;
- stop conditions;
- incident escalation;
- restoration and cleanup responsibilities.

## Test data and environments

Use synthetic or minimised data where possible. Production testing requires explicit approval and additional safeguards. Test accounts, tools, payloads, artefacts, logs, and copied data must be inventoried and securely removed or retained under approved evidence rules.

## Independence and competence

Testers should have appropriate AI, application-security, privacy, domain, and adversarial-testing competence. Independence should increase with system criticality, novelty, potential rights impact, and consequence of failure.

Vendor testing does not automatically replace the deployer’s own assurance.

## Finding management

Each finding should record:

- affected system and version;
- test method;
- evidence and reproducibility;
- exploitability and preconditions;
- technical, privacy, safety, and rights impacts;
- severity and priority;
- control owner;
- remediation target;
- compensating controls;
- retest result;
- residual-risk decision;
- accountable approver.

## Human oversight testing

Testing should determine whether human reviewers:

- receive sufficient information;
- can recognise manipulated or unreliable output;
- have time and authority to intervene;
- can override or stop the system;
- avoid blind reliance on AI recommendations;
- follow escalation and incident procedures.

## Stop conditions

Testing must stop or escalate when:

- personal or confidential data is unexpectedly exposed;
- production stability or safety is threatened;
- actions may affect real customers or transactions;
- testing exceeds authorised scope;
- logs or monitoring fail;
- third-party systems may be affected;
- evidence indicates an active compromise;
- the agreed emergency contact cannot be reached.

## GlobalWay Travel Services example

GlobalWay commissions an independent red team to test its AI disruption assistant. The team attempts indirect prompt injection through supplier advisories, unauthorised refund-tool calls, traveller-data extraction, accessibility-priority manipulation, and human-review bypass.

A critical finding shows that crafted retrieved text can influence a proposed refund action. Production deployment is blocked. GlobalWay isolates retrieved instructions, restricts the tool gateway, adds transaction validation and mandatory human approval, and requires a successful independent retest before release.

## Control activities

- Maintain a testing policy and risk-based schedule.
- Approve scope and rules of engagement.
- Protect data, systems, and evidence.
- Include AI-specific, technical, human, privacy, and rights scenarios.
- Track findings to validated closure.
- Require accountable approval for residual risk.
- feed lessons into threat models, lifecycle gates, monitoring, training, and vendor management.

## Evidence

- testing policy and schedule;
- authorisation and scope;
- rules of engagement;
- tester qualifications and independence assessment;
- test plans and cases;
- raw and summarised results;
- finding register;
- remediation and retest evidence;
- residual-risk approvals;
- cleanup confirmation;
- lessons-learned records.

## Audit tests

1. Select systems by risk tier and verify testing frequency and scope.
2. Confirm testing was authorised and followed rules of engagement.
3. Review whether AI-specific, human-oversight, privacy, and rights risks were tested.
4. Trace critical findings to remediation and independent retest.
5. Verify production deployment was blocked when required.
6. Review residual-risk approvals and overdue findings.
7. Confirm test artefacts, accounts, and data were cleaned up or securely retained.

## Metrics

- systems tested by risk tier;
- critical and high findings;
- average remediation and retest time;
- repeat findings;
- deployments blocked by testing;
- overdue findings and expired exceptions;
- human-oversight failures identified;
- findings originating from vendor-controlled components;
- test coverage of defined threat scenarios.

## Management checklist

- Is adversarial testing required before high-risk deployment?
- Are scope, authority, safety, and privacy rules clear?
- Are testers sufficiently independent and competent?
- Are human oversight and affected-person harms tested?
- Are findings validated through retesting?
- Can critical findings block deployment or trigger suspension?
- Are lessons incorporated into governance and engineering?

## Figure specification — Adversarial Assurance Governance Cycle

Create a formal cycle showing risk scoping, authorisation, rules of engagement, adversarial execution, evidence capture, severity assessment, remediation, independent retest, residual-risk approval, and feedback into threat modelling and lifecycle governance. Show an emergency stop path throughout testing.

**Alt text:** Adversarial assurance governance cycle from risk scoping and authorisation through testing, remediation, independent retest, residual-risk approval, and governance feedback, with an emergency stop path.
