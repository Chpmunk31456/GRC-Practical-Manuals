# Manual 48 — Practical Scenarios

## Scenario 1 — Customer-service GenAI with confidential data risk

A customer-service team deploys a GenAI assistant using retrieval over policy documents and selected customer records. The team proposes sending every conversation to the model provider for quality improvement.

### Learner tasks
1. identify data-governance and confidentiality risks;
2. define permitted retrieval sources and data classes;
3. establish input/output filtering and retention controls;
4. create an evaluation plan for hallucination, leakage and harmful responses;
5. define the evidence needed for assurance.

### Expected control outcome
Use data minimisation, source allowlisting, contractual/provider controls, logging, evaluation, human escalation and incident response. Do not infer that use of AI Verify alone proves the system safe or legally compliant.

## Scenario 2 — Finance agent with payment authority

An agent receives invoices, matches them to purchase orders and can initiate payment instructions up to a configurable threshold.

### Learner tasks
- determine whether the use case is suitable for agentic automation;
- bound the agent's powers;
- define significant human checkpoints;
- specify identity, credential and tool-access controls;
- design action provenance and a kill switch.

### Minimum safeguards
- separate agent identity;
- least privilege;
- payment/value limits;
- allowlisted counterparties or payment rails;
- mandatory approval for exceptions/high-value transactions;
- complete transaction/action log;
- independent reconciliation;
- rapid disablement capability.

## Scenario 3 — HR recruiting agent and automation bias

A recruiting agent ranks candidates, drafts screening recommendations and schedules interviews. Recruiters rarely override its ranking.

### Learner tasks
- identify where automation bias may occur;
- decide what human review is meaningful;
- design monitoring that detects excessive deference;
- define candidate-facing transparency and escalation where appropriate;
- document limitations and prohibited uses.

### Evidence
- reviewer guidance;
- sampled override/disagreement data;
- fairness/performance testing where applicable;
- decision rationale;
- issue-remediation log.

## Scenario 4 — Third-party coding agent

A software team connects a third-party coding agent to source repositories, issue trackers, CI/CD and cloud development environments.

### Learner tasks
1. inventory tools and credentials;
2. classify permitted and prohibited actions;
3. determine whether production deployment or privileged changes require human approval;
4. design sandboxing, branch protection and secrets controls;
5. define provider-change and incident-response requirements.

### Expected control outcome
Separate identities, short-lived/scoped credentials, protected branches, code review, CI security checks, restricted production access, immutable logs and revocation/containment procedures.

## Scenario 5 — Multi-agent travel operations

A travel platform uses one agent to interpret customer intent, another to search inventory, another to create bookings, and another to handle disruption rebooking.

### Learner tasks
- map delegation paths;
- define which agent can instruct which other agent;
- prevent confused-deputy and privilege-escalation patterns;
- define user confirmation requirements for irreversible or costly actions;
- preserve end-to-end action provenance.

### Evidence
- inter-agent trust-boundary diagram;
- permissions matrix;
- delegation/event logs;
- replayable transaction trail;
- exception and rollback record.

## Scenario 6 — Public-facing advisory chatbot

An organisation deploys a chatbot that explains eligibility criteria and suggests next steps but is not authorised to make formal eligibility decisions.

### Learner tasks
- communicate the agent's actual authority;
- prevent the system from presenting guidance as a binding determination;
- establish escalation to human staff;
- test for hallucinated policy claims;
- maintain source/version control.

## Scenario 7 — AI Verify assurance exercise

A project team says, 'The system passed AI Verify, therefore it is compliant and safe.'

### Learner task
Rewrite the conclusion into an evidence-based assurance statement.

### Expected answer pattern
State which claims, process checks and technical tests were assessed; identify the test conditions, results, limitations and residual risk; explicitly avoid certification/compliance claims not supported by the evidence.

## Scenario 8 — Agent capability expansion after vendor update

A provider update adds web browsing, file upload and autonomous tool selection to a previously bounded agent.

### Learner tasks
- identify the change as a revalidation trigger;
- reassess blast radius and data/tool access;
- update human checkpoints;
- re-run relevant safety/security tests;
- decide whether deployment should remain suspended until controls are updated.

## Scenario 9 — Executive governance review

A governance committee receives a dashboard showing 30 AI systems, five GenAI systems and three agents. Two agents have not completed current access reviews, one has no tested kill switch, and one vendor changed models without prior notice.

### Learner tasks
Prioritise findings, assign owners, define remediation deadlines and specify which systems should be conditionally restricted or suspended.

## Scenario 10 — Cross-framework mapping challenge

A business asks whether implementing Singapore's Agentic AI framework means the organisation 'complies with the EU AI Act and ISO/IEC 42001.'

### Required learner response
Reject automatic equivalence. Produce a mapping that identifies supporting overlaps, partial relationships, differences in legal/standards status and additional evidence or obligations required by each target regime.