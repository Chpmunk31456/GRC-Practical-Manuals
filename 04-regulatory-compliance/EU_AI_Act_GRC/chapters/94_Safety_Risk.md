# Chapter 94 — Safety Risk

## Purpose

This chapter provides a practical method for identifying, evaluating, controlling, monitoring, and evidencing safety risks arising from AI systems throughout their lifecycle.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should assess whether an AI system could cause or contribute to physical, psychological, operational, environmental, or public-safety harm. Safety risk must be considered before deployment, after material change, and continuously during operation.

For high-risk AI systems, safety-related controls should be integrated with the risk-management system, data governance, technical documentation, human oversight, accuracy, robustness, cybersecurity, post-market monitoring, incident reporting, and corrective-action processes.

## Plain-language explanation

An AI system can be technically functional and still be unsafe. It may provide a plausible but incorrect recommendation, fail under unusual conditions, encourage an unsafe action, delay emergency escalation, or create a chain of operational errors.

Safety assessment therefore asks more than whether the model works. It asks what could go wrong, who could be harmed, how severe the harm could be, how quickly it could develop, whether a person can intervene, and whether the organization can detect and contain the failure.

## Safety-risk categories

Assess at least the following:

- physical injury or health harm;
- psychological distress or behavioral harm;
- unsafe operational decisions;
- delayed or blocked emergency response;
- transportation, infrastructure, or workplace hazards;
- environmental damage;
- misleading or overconfident advice;
- unsafe automation or excessive system autonomy;
- cascading failures across integrated systems;
- harm caused by degraded, unavailable, or manipulated data;
- harm caused by model drift or changed operating conditions;
- foreseeable misuse, abuse, or circumvention;
- harm to children, older persons, persons with disabilities, or other vulnerable groups.

## Safety-risk assessment method

### 1. Define the safety context

Document:

- intended purpose;
- reasonably foreseeable misuse;
- users and affected persons;
- operating environment;
- critical dependencies;
- safety-sensitive decisions or actions;
- expected human involvement;
- emergency and fallback conditions.

### 2. Identify hazardous scenarios

Use structured techniques such as:

- hazard analysis;
- failure-mode and effects analysis;
- fault-tree analysis;
- misuse-case analysis;
- scenario workshops;
- incident and near-miss review;
- red-team and adversarial testing;
- human-factors analysis.

Each scenario should describe the initiating event, system behavior, human response, consequence, detection opportunity, and control path.

### 3. Assess severity and likelihood

Rate:

- severity of potential harm;
- likelihood under normal use;
- likelihood under foreseeable misuse;
- detectability before harm;
- speed of onset;
- reversibility;
- number and vulnerability of people affected;
- dependency on human intervention;
- uncertainty in the assessment.

Avoid treating low historical frequency as proof of low risk when the system is new, data are limited, or consequences are severe.

### 4. Select controls

Use layered controls, including:

- safe design constraints;
- approved-use boundaries;
- input and output validation;
- confidence thresholds;
- prohibited-action rules;
- human review and dual approval;
- accessible escalation paths;
- fail-safe defaults;
- rate, transaction, or authority limits;
- emergency stop, rollback, and isolation;
- monitoring and alerting;
- resilience and continuity measures;
- user warnings and instructions;
- training and competency controls;
- vendor and dependency assurance.

### 5. Validate control effectiveness

Validation should include:

- normal-operation testing;
- edge and stress conditions;
- degraded-data scenarios;
- unavailable-dependency scenarios;
- adversarial and misuse scenarios;
- human-oversight exercises;
- emergency-stop and rollback tests;
- accessibility and usability testing;
- independent review for higher-consequence systems.

### 6. Determine residual safety risk

Residual risk must be explicitly documented, approved by an accountable authority, and supported by evidence. A system should not proceed when residual safety risk exceeds approved tolerance or when critical uncertainty remains unresolved.

## Human factors and automation bias

Safety depends on whether people can understand, challenge, and override the system. Assess whether users:

- know the system’s limitations;
- can recognize uncertain or abnormal output;
- have enough time to intervene;
- have authority to stop or override;
- receive actionable alerts rather than excessive noise;
- are protected from fatigue and automation bias;
- can reach a qualified human decision-maker;
- understand emergency and fallback procedures.

Human oversight should be tested as an operational control, not assumed from a policy statement.

## Change and drift

Reassess safety risk when there is:

- a model, prompt, tool, or data-source change;
- a new user population or geography;
- a new use case or decision consequence;
- a supplier or infrastructure change;
- evidence of model drift;
- a significant incident or near miss;
- changed legal, technical, or operating conditions;
- a substantial modification.

## GlobalWay Travel Services example

GlobalWay uses an AI travel-disruption assistant to recommend rebooking options during severe weather. A safety review identifies a scenario in which the assistant recommends a route through an airport that has issued a security evacuation notice.

GlobalWay introduces authoritative disruption-data validation, blocks recommendations involving closed or evacuated facilities, requires human approval for safety-critical rerouting, displays the source and time of each alert, and automatically escalates conflicting information to the travel-risk team. The system is tested under stale-data, unavailable-feed, high-volume, and contradictory-alert scenarios before deployment.

## Control activities

- Maintain a documented AI safety-risk methodology.
- Identify foreseeable hazardous scenarios before deployment.
- Define risk criteria, tolerances, and accountable approval levels.
- Implement layered preventive, detective, responsive, and recovery controls.
- Test human oversight, fail-safe behavior, rollback, and emergency stop.
- Track incidents, near misses, unsafe outputs, and control failures.
- Reassess risk after material changes and emerging evidence.
- Block or suspend deployment when safety criteria are not met.

## Evidence

- safety-risk assessment;
- hazard and misuse-scenario register;
- severity and likelihood ratings;
- assumptions and uncertainty log;
- safety requirements and acceptance criteria;
- test plans, results, and defect records;
- human-factors and usability results;
- emergency-stop and rollback evidence;
- residual-risk approvals;
- incident and near-miss records;
- monitoring reports;
- corrective-action and retest evidence;
- change and reassessment records.

## Audit tests

1. Select AI systems with material safety consequences and inspect their safety assessments.
2. Verify that intended use and foreseeable misuse were considered.
3. Trace identified hazardous scenarios to implemented controls and test evidence.
4. Confirm that human oversight, emergency stop, fallback, and recovery were tested.
5. Review whether vulnerable groups and accessibility were considered.
6. Inspect residual-risk approvals and confirm they were made by authorized personnel.
7. Trace incidents and near misses to corrective action and reassessment.
8. Verify that material changes triggered renewed safety review.

## Metrics

- systems with completed safety assessments;
- open high or critical safety risks;
- safety-control test pass rate;
- unsafe-output and near-miss rate;
- time to detect and contain safety events;
- emergency-stop and rollback test success rate;
- overdue safety remediation;
- repeat safety findings;
- human-oversight failures;
- systems operating under temporary safety exceptions.

## Management checklist

- What harm could this AI system cause or amplify?
- Who could be affected, including vulnerable groups?
- Are hazardous scenarios documented and tested?
- Can people recognize, challenge, override, and stop the system?
- Are fail-safe, rollback, and emergency procedures effective?
- Is residual safety risk within approved tolerance?
- Are incidents, near misses, drift, and changes feeding continuous reassessment?

## Figure specification — AI Safety-Risk Control Loop

Create a circular control-loop graphic showing: define safety context, identify hazards, assess severity and likelihood, select layered controls, validate under normal and abnormal conditions, approve residual risk, monitor incidents and near misses, and reassess after change. Include a visible stop-deployment path when risk exceeds tolerance.

**Alt text:** AI safety-risk control loop from context and hazard identification through control validation, residual-risk approval, monitoring, and reassessment, with a stop-deployment path for unacceptable risk.
