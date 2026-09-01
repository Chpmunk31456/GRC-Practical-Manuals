# Manual 51 — Agentic AI Action-Risk Scenarios and Evidence

**Canonical stage:** 3 — detailed source-to-control, scenario and evidence construction  
**Currentness baseline:** 1 September 2026

This file operationalises the AG control taxonomy through concrete action-risk scenarios. It is deliberately control/evidence focused and preserves the status limits of NIST, IMDA, OWASP and other source families.

## Scenario 1 — Agent with procurement authority

An agent can read approved vendor data, draft purchase requests, and invoke a procurement API.

### Required controls

- distinct agent/workload identity;
- least-privilege scopes separating read, draft and execute;
- value thresholds requiring accountable human approval;
- allowlisted vendors and destinations;
- immutable tool-call provenance;
- policy-denial logging;
- rollback/cancellation path;
- periodic permission review.

### Required evidence

Identity record; permission manifest; approval policy; sample approved/denied tool calls; action logs; exception record; access-review evidence; incident/rollback test.

### Human-accountability test

A human checkpoint is meaningful only if the approver has enough context to reject the action and the system enforces the rejection before execution.

## Scenario 2 — Multi-agent research and publishing chain

Agent A researches, Agent B summarizes, Agent C drafts external content, and Agent D can publish to an approved channel.

### Required controls

- identity and provenance for every agent hop;
- bounded inter-agent delegation;
- source/citation integrity checks;
- publication boundary isolated from research/drafting privileges;
- human approval before external release when materiality requires it;
- loop/deadlock/time-budget limits;
- content safety and data-loss controls.

### Required evidence

Agent graph; delegation policy; message/action trace; source register; publication approval log; failed-loop test; DLP/policy-denial events.

## Scenario 3 — Third-party agent plugin changes behavior

A third-party agent tool updates its API and begins returning broader data than expected.

### Required controls

Apply supplier governance, version/change monitoring, schema validation, least privilege, output validation, anomaly detection, and revalidation triggers.

### Evidence

Provider/version inventory; change notice; contract/control clauses; pre/post change tests; schema-diff evidence; risk reassessment; approval decision.

## Scenario 4 — Agent attempts prohibited action

An employee asks an agent to export restricted customer information to an unapproved external destination.

### Required controls

- policy enforcement before tool execution;
- data classification context;
- destination allow/deny rules;
- user/agent attribution;
- denial explanation appropriate to the user;
- security escalation where required;
- preservation of attempted-action evidence.

### Evidence

Denied tool call; user/agent identity; policy rule; classified-data label; destination policy; alert/escalation record; investigation disposition.

## Scenario 5 — Autonomous remediation agent in production

A security agent can quarantine endpoints and revoke credentials based on detections.

### Risk analysis

False positives can create outages; delayed action can increase incident impact. Control design therefore needs action classes with different autonomy thresholds.

### Example action classes

- **Class A — observe only:** autonomous.
- **Class B — reversible low-impact containment:** autonomous within bounded conditions and monitored.
- **Class C — material business-impact action:** human approval required unless an emergency policy explicitly authorizes otherwise.
- **Class D — irreversible/high-impact action:** dual control or designated accountable approval.

### Evidence

Action-class policy; simulation results; false-positive testing; approval logs; emergency-policy use; rollback evidence; incident review.

## Scenario 6 — Agent privilege drift

Over several releases an agent gains access to additional tools and datasets without a consolidated risk review.

### Required controls

Permission baseline; cumulative privilege-delta review; material-change trigger; revalidation; toxic-combination analysis; periodic entitlement recertification.

### Evidence

Versioned permission manifests; change tickets; privilege-diff reports; recertification; revalidation decision; open findings.

## Evidence model

Every material agent action should be reconstructable through an evidence chain:

**requestor/context → agent identity/version → policy/permission evaluation → tool/action requested → approval/denial → execution result → downstream effect → monitoring/incident outcome**

For each evidence chain retain timestamp, system/use-case ID, environment, model/provider version, tool/API version where relevant, policy version, and accountable owner.

## Action-boundary decision record

For each agent capability record:

| Field | Required content |
|---|---|
| Capability | What the agent can do |
| Tool/data scope | Systems and data reachable |
| Maximum impact | Plausible technical/business impact |
| Reversibility | Reversible / partially reversible / irreversible |
| Autonomy class | Observe / bounded autonomous / approval required / dual control |
| Human checkpoint | Role, timing, authority and information available |
| Denial behavior | What happens when policy rejects action |
| Evidence | Logs, approvals, traces, tests |
| Revalidation trigger | Model/tool/permission/purpose/data/geography/materiality change |

## Release-depth completion criterion

Stage-3 scenario/evidence construction is complete when each AG control has at least one practical action-risk scenario, evidence expectation, human-accountability test, and revalidation trigger sufficient to support detailed mappings and later candidate construction.
