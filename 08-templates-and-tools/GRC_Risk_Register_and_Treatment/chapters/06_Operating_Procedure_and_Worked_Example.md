# 6. Operating Procedure and Worked Example

## End-to-end procedure

### Step 1 — Establish scope

Define the objective, process, service, project, business unit, asset group, vendor population, or decision being assessed. Confirm the assessment period, methodology, rating criteria, and decision authority.

### Step 2 — Gather evidence

Collect current documents, system reports, incidents, test results, metrics, contracts, architecture information, and specialist input. Record evidence dates and gaps.

### Step 3 — Write scenarios

Describe cause, event, affected objective, and consequence. Separate materially different scenarios rather than combining unrelated exposures.

### Step 4 — Assign ownership

Name one accountable risk owner. Identify control and action owners separately.

### Step 5 — Assess inherent exposure

Apply the approved likelihood and impact criteria using the stated inherent-risk assumption.

### Step 6 — Evaluate controls

Document relevant controls and assess design and operating effectiveness using evidence.

### Step 7 — Assess residual exposure

Estimate the remaining likelihood and impact. Record confidence, assumptions, and uncertainty.

### Step 8 — Compare with appetite and tolerance

Determine whether exposure is within approved limits and whether escalation is required.

### Step 9 — Select response and treatment

Choose avoid, mitigate, transfer/share, accept, or pursue/enhance. Define measurable actions and target exposure.

### Step 10 — Approve and monitor

Obtain the required decision, monitor indicators and actions, reassess after change, and preserve evidence.

## Worked example

### Objective

Maintain continuous access to the customer-support platform during business-critical periods.

### Scenario

Because the platform depends on a single cloud region and recovery testing has not demonstrated restoration within the business requirement, a regional service disruption may make the platform unavailable, delaying customer support and causing contractual, financial, and reputational harm.

### Evidence

- Current architecture diagram
- Business impact analysis
- Recovery test report
- Cloud-provider service documentation
- Customer contract availability commitments

### Inherent assessment

- Likelihood: 3 — Possible
- Impact: 5 — Severe
- Score: 15 — High under the example matrix

### Existing controls

- Provider-native backups
- Infrastructure configuration stored in version control
- Incident-response procedures
- Status-page monitoring

### Control assessment

Design is partially effective because backups and configuration support recovery, but no secondary-region capability exists. Operating effectiveness is partially effective because backup jobs are monitored, while full restoration has not met the required recovery time.

### Residual assessment

- Likelihood: 3 — Possible
- Impact: 4 — Major
- Score: 12 — High
- Confidence: Medium
- Appetite status: Outside tolerance

### Response

Mitigate.

### Treatment actions

1. Design and approve secondary-region architecture.
2. Implement replicated data and tested deployment automation.
3. Conduct a full recovery exercise.
4. Update procedures and customer communications.
5. Validate recovery time and recovery point objectives.

### Target assessment

- Target likelihood: 2 — Unlikely
- Target impact: 3 — Moderate
- Target score: 6 — Moderate

### Monitoring

Track recovery-test results, unresolved replication failures, architecture milestones, and overdue treatment tasks. Escalate missed milestones or any outage exceeding the approved tolerance.

## Common implementation failures

- Treating the score as the risk rather than the scenario
- Assigning groups instead of accountable owners
- Recording controls without testing evidence
- Accepting risk indefinitely
- Closing actions without reassessing exposure
- Using stale evidence
- Combining many unrelated risks into one record
- Reporting only counts instead of decisions and concentration
