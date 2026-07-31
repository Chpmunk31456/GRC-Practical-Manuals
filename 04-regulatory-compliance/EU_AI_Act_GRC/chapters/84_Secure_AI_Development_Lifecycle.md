# Chapter 84 — Secure AI Development Lifecycle

## Purpose

This chapter establishes a secure AI development lifecycle (SAIDL) that integrates legal, governance, privacy, security, resilience, accessibility, and human-oversight controls from initial concept through retirement.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should operate a documented lifecycle that prevents AI systems from moving into testing, deployment, material change, or retirement without appropriate risk assessment, control evidence, accountable approval, and traceability.

The lifecycle should align applicable EU AI Act obligations with data protection, cybersecurity, product assurance, records management, procurement, incident response, and business continuity requirements.

## Plain-language explanation

Security and compliance cannot be added only at the end. Each stage must have clear entry criteria, required controls, evidence, named decision-makers, and stop conditions.

## Lifecycle stages

1. **Concept and intake** — define purpose, affected persons, prohibited uses, business owner, and preliminary legal classification.
2. **Requirements and design** — document functional, security, privacy, transparency, accessibility, oversight, and resilience requirements.
3. **Data and component acquisition** — approve datasets, models, libraries, APIs, infrastructure, licences, and vendors.
4. **Build and configuration** — apply secure coding, access control, secrets management, environment separation, and configuration baselines.
5. **Verification and validation** — test accuracy, robustness, security, bias, privacy, accessibility, explainability, and human-oversight effectiveness.
6. **Pre-deployment approval** — confirm evidence completeness, residual risk acceptance, operating procedures, training, and rollback readiness.
7. **Deployment and change control** — use authorised releases, versioning, monitoring, segregation of duties, and controlled promotion.
8. **Operations and monitoring** — detect drift, abuse, incidents, vulnerabilities, control degradation, and changes in legal or business context.
9. **Retirement and disposal** — revoke access, preserve required evidence, delete or return data, remove integrations, and verify shutdown.

## Governance gates

Each stage should have documented gate criteria. A system must not proceed when required evidence is missing, risk is outside tolerance, testing has failed, human oversight is ineffective, or an accountable approver has not signed off.

Minimum gates should include:

- use-case acceptance;
- legal and role classification;
- data and privacy approval;
- architecture and threat-model approval;
- testing completion;
- deployment authorisation;
- material-change approval;
- suspension and restoration approval;
- retirement confirmation.

## Roles and accountability

The lifecycle should identify, at minimum:

- executive sponsor;
- business owner;
- product or system owner;
- AI risk owner;
- security owner;
- privacy or data-protection reviewer;
- legal or compliance reviewer;
- model or engineering lead;
- human-oversight owner;
- incident commander;
- independent approver where required.

No role assignment should obscure the organization’s own accountability.

## Secure engineering controls

Controls should include:

- approved repositories and protected branches;
- peer review and segregation of duties;
- dependency and licence scanning;
- software and model bills of materials;
- secrets and key management;
- hardened build and deployment pipelines;
- signed or otherwise verifiable artefacts;
- environment separation;
- least privilege;
- secure defaults;
- reproducible builds where feasible;
- model, prompt, configuration, and dataset versioning;
- rollback and kill-switch capability;
- tamper-evident logs;
- secure test-data handling.

## AI-specific controls

The lifecycle should address:

- prompt injection and indirect prompt injection;
- model manipulation and jailbreaks;
- unsafe tool use and excessive agency;
- retrieval and vector-store poisoning;
- training-data poisoning;
- model extraction and theft;
- sensitive-data leakage;
- insecure output handling;
- hallucination and unsupported claims;
- automation bias;
- model and data drift;
- adversarial examples;
- supply-chain compromise.

## Testing and assurance

Testing should be risk-based and repeatable. It should cover normal, boundary, misuse, adversarial, failure, and recovery conditions.

Evidence should identify:

- tested version;
- environment;
- datasets and test cases;
- expected and actual results;
- defects and severity;
- remediation;
- residual limitations;
- approver;
- date and validity period.

Independent review should be used where consequence, complexity, novelty, or regulatory exposure warrants it.

## Material change

A material-change review should be triggered by changes to purpose, users, affected persons, model, provider, dataset, prompts, tools, integrations, decision authority, geography, legal classification, or risk profile.

A change must not be treated as routine merely because it is technically small.

## Human oversight

For each use case, document:

- what AI may do;
- what decision remains human;
- what information the reviewer receives;
- required competence and authority;
- time available for review;
- override and correction mechanisms;
- stop and escalation criteria;
- accountable owner.

## Stop and escalation conditions

Suspend progression or operation when:

- required evidence is missing;
- prohibited use is identified;
- security testing fails;
- privacy or rights impacts are unresolved;
- monitoring is unavailable;
- human review is ineffective;
- critical vulnerabilities remain open;
- material drift is detected;
- rollback cannot be performed safely;
- accountable approval is absent.

## GlobalWay Travel Services example

GlobalWay develops an AI assistant that recommends alternative itineraries during major disruptions.

The assistant may analyse schedules, fare rules, traveller preferences, accessibility requests, and operational constraints. It may rank options and draft a proposed itinerary.

A trained human agent must approve any rebooking that changes destination, creates material additional cost, affects accessibility support, or conflicts with the traveller’s stated preferences. The agent can reject, revise, or escalate the recommendation.

Before deployment, GlobalWay requires threat modelling, privacy review, accessibility testing, prompt-injection testing, rollback validation, vendor evidence, and human-oversight testing. Deployment is blocked until the accountable business and security owners approve the residual risk.

## Control activities

- Maintain a lifecycle standard and gate checklist.
- Assign accountable owners.
- Maintain version-controlled artefacts and evidence.
- Require security, privacy, rights, accessibility, and resilience reviews.
- Test human oversight and recovery.
- Monitor deployed systems and re-assess material changes.
- Retire systems through a controlled process.

## Evidence

- approved use-case record;
- legal and risk classification;
- architecture diagrams;
- threat model;
- privacy and rights assessments;
- data and model documentation;
- bills of materials;
- test plans and results;
- approval records;
- deployment and rollback records;
- monitoring reports;
- incident records;
- retirement certificate.

## Audit tests

1. Select deployed AI systems and trace each through every required lifecycle gate.
2. Verify that versions in production match approved artefacts.
3. Confirm that failed tests or unresolved risks blocked progression where required.
4. Test whether material changes triggered re-assessment.
5. Verify that human oversight was tested, not merely documented.
6. Confirm rollback and retirement procedures are operational.
7. Review whether evidence is complete, current, attributable, and tamper-resistant.

## Metrics

- percentage of systems with complete lifecycle evidence;
- gate exceptions by severity;
- unresolved critical findings at deployment;
- average time to remediate security defects;
- percentage of material changes reassessed before release;
- rollback-test success rate;
- percentage of systems with tested human oversight;
- retired systems with verified data and access closure.

## Management checklist

- Is every AI system governed by the lifecycle?
- Are gates mandatory and enforceable?
- Are owners and approvers named?
- Are AI-specific threats tested?
- Is human oversight effective?
- Are material changes reassessed?
- Can the system be suspended, rolled back, and retired safely?
- Is the evidence sufficient for audit and regulatory review?

## Figure specification — Secure AI Development Lifecycle

Create a formal circular lifecycle diagram with nine stages: intake, design, acquisition, build, validation, approval, deployment, monitoring, and retirement. Place governance gates between stages. Show continuous human accountability, risk management, security, privacy, accessibility, evidence, and incident feedback around the lifecycle.

**Alt text:** Circular secure AI lifecycle showing governance gates from concept through retirement, with continuous human accountability, risk management, security, privacy, accessibility, evidence, and incident feedback.
