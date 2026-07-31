# Chapter 95 — Bias and Discrimination Risk

## Purpose

This chapter establishes a practical method for identifying, assessing, controlling, monitoring, and evidencing bias and discrimination risks in AI systems.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should assess whether an AI system may create, reproduce, conceal, or amplify unjustified differences in treatment or outcomes. The assessment must consider data, labels, features, model behavior, workflow design, human use, accessibility, and real-world outcomes.

For systems that affect employment, education, access to services, travel assistance, pricing, fraud review, identity verification, or other consequential decisions, bias and discrimination risk should be assessed before deployment, after material change, and throughout operation.

## Plain-language explanation

Bias is not limited to an obviously prejudiced rule. It can arise when historical data reflect unequal treatment, when a proxy feature indirectly represents a protected characteristic, when one group is underrepresented, when error rates differ materially, or when people apply AI recommendations inconsistently.

A model can appear accurate overall while performing poorly for a smaller group. Organizations therefore need both technical testing and contextual review of how the system affects people.

## Sources of bias

Assess at least:

- historical and societal bias in source data;
- sampling and representation gaps;
- biased or inconsistent labels;
- measurement error;
- proxy variables;
- feature selection and transformation;
- model optimization choices;
- inappropriate thresholds;
- language and cultural bias;
- accessibility barriers;
- feedback loops;
- deployment-context mismatch;
- human interpretation and automation bias;
- unequal access to appeal or correction;
- vendor-controlled data or models that cannot be adequately evaluated.

## Assessment method

### 1. Define the decision context

Document:

- intended purpose;
- affected persons and groups;
- decision consequence;
- legal and policy constraints;
- human decision points;
- available alternatives;
- appeal and remediation paths;
- protected and vulnerable groups relevant to the context.

### 2. Examine data suitability

Review:

- provenance and collection methods;
- population coverage;
- missingness and quality;
- label consistency;
- historical inequities;
- temporal and geographic relevance;
- class imbalance;
- lawful and appropriate use of sensitive attributes;
- limitations in synthetic, inferred, or vendor data.

### 3. Test model performance by group

Where lawful, appropriate, and technically feasible, compare:

- selection or approval rates;
- false-positive and false-negative rates;
- precision and recall;
- calibration;
- error severity;
- abstention and escalation rates;
- override rates;
- time to resolution;
- appeal outcomes;
- accessibility and usability outcomes.

No single metric proves fairness. Metrics must be selected according to the use case and potential harm.

### 4. Evaluate proxies and intersections

Assess whether features such as location, language, device type, income pattern, travel history, education, or purchasing behavior may act as proxies for protected characteristics.

Where feasible, examine intersectional effects rather than relying only on broad categories. A system may perform acceptably for two groups separately but poorly for people who belong to both.

### 5. Assess workflow and human use

Determine whether:

- users understand the system's limitations;
- reviewers can challenge recommendations;
- overrides are permitted and monitored;
- instructions discourage blind reliance;
- escalation is available;
- decision explanations are meaningful;
- affected persons can contest or correct information;
- human reviewers apply consistent standards.

### 6. Select controls

Controls may include:

- improved data collection and representation;
- label-quality review;
- feature removal or transformation;
- threshold adjustment;
- constrained optimization;
- confidence-based abstention;
- mandatory human review;
- accessibility improvements;
- standardized decision criteria;
- reviewer training;
- explanation and notice controls;
- appeal, correction, and remediation procedures;
- monitoring by subgroup;
- independent validation.

### 7. Approve residual risk

Document remaining disparities, limitations, uncertainty, and the rationale for acceptance. High-impact unresolved disparities should block deployment or trigger redesign unless a lawful, evidence-based justification and adequate safeguards exist.

## GlobalWay Travel Services example

GlobalWay tests an AI fraud-screening system used to flag unusual travel bookings. Overall accuracy is high, but false-positive rates are materially higher for travelers booking from certain regions and for customers who use prepaid cards.

The review identifies geographic and payment-pattern proxies that correlate with limited banking access. GlobalWay removes one feature, adjusts thresholds, adds contextual review, requires human approval before account restriction, introduces multilingual notices, and monitors outcomes by region and payment method. The revised system must pass defined disparity thresholds before deployment.

## Control activities

- Maintain a documented bias and discrimination assessment method.
- Define relevant populations, consequences, and legal constraints.
- Review data provenance, representativeness, and labels.
- Test performance and outcomes by relevant group.
- Assess proxy and intersectional effects.
- Validate human-review and appeal controls.
- Document remediation and residual-risk decisions.
- Monitor production outcomes and investigate material disparities.
- Reassess after changes in data, model, threshold, population, or use.

## Evidence

- bias and discrimination risk assessment;
- data-provenance and representativeness analysis;
- protected-group and vulnerability analysis;
- metric-selection rationale;
- subgroup and intersectional test results;
- proxy-feature review;
- threshold and model-change records;
- human-oversight test results;
- accessibility testing;
- appeal and complaint records;
- residual-risk approvals;
- monitoring dashboards and investigation records;
- corrective-action and retest evidence.

## Audit tests

1. Select consequential AI systems and inspect their bias-risk assessments.
2. Verify that relevant groups, consequences, and deployment contexts were identified.
3. Review data representativeness, label quality, and proxy analysis.
4. Reperform or inspect subgroup performance tests.
5. Confirm that metric choices match the use case and harm model.
6. Trace material disparities to remediation and retesting.
7. Inspect human-review, override, appeal, and correction processes.
8. Verify that production monitoring identifies and escalates material changes.

## Metrics

- systems with completed bias assessments;
- systems tested by relevant subgroup;
- material disparity findings;
- unresolved high-risk disparities;
- false-positive and false-negative gaps;
- appeal and reversal rates;
- human-override rates by group;
- complaints alleging unfair treatment;
- time to investigate disparity alerts;
- repeat bias findings;
- systems operating under temporary exceptions.

## Management checklist

- Who may be disadvantaged by this system?
- Are the data representative and the labels reliable?
- Do error rates or outcomes differ materially across groups?
- Could features act as proxies for protected characteristics?
- Are intersectional effects considered?
- Can people challenge, appeal, and correct decisions?
- Are disparities monitored after deployment?
- Is residual risk justified, approved, and within tolerance?

## Figure specification — Bias and Discrimination Assurance Path

Create a left-to-right assurance path showing: define context and affected groups, inspect data and labels, test subgroup and intersectional performance, examine proxies and workflow, implement controls, validate outcomes, approve residual risk, and monitor production disparities. Include a redesign or stop-deployment branch for unresolved high-impact disparities.

**Alt text:** Bias and discrimination assurance path from context and data review through subgroup testing, control validation, residual-risk approval, and production monitoring, with a redesign path for unresolved disparities.
