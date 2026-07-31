# Chapter 113 — Design-Effectiveness Testing

## Purpose

This chapter explains how to determine whether AI governance and compliance controls are suitably designed to achieve their stated objectives before relying on operating-effectiveness results.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should evaluate whether each material AI control, if performed as designed by competent personnel using reliable information, would prevent, detect, or correct the relevant risk or compliance failure in a timely manner.

## Plain-language explanation

A control may be performed consistently and still be ineffective because its design is weak. For example, a quarterly review cannot prevent an unapproved high-risk AI system from entering production if deployment can occur at any time without a release gate. Design-effectiveness testing asks whether the control is capable of working before asking whether it actually operated.

## Design attributes

For each control, assess:

- objective and risk addressed;
- legal or policy requirement mapped;
- scope and population;
- owner and performer competence;
- frequency or trigger;
- preventive, detective, corrective, or directive nature;
- manual, automated, or hybrid operation;
- information used by the control;
- precision and thresholds;
- evidence produced;
- escalation and exception handling;
- dependency on other controls;
- segregation of duties;
- timeliness relative to the risk.

## Testing methods

Use proportionate methods such as:

- document inspection;
- process walkthrough;
- inquiry and corroboration;
- observation;
- configuration review;
- control-to-risk traceability analysis;
- scenario testing;
- review of forms, checklists, approvals, and workflow gates;
- evaluation of system-generated evidence;
- assessment of override and bypass paths.

Inquiry alone is insufficient for key controls.

## Design questions

Determine whether:

- the control addresses the correct risk;
- the control occurs early enough;
- the control covers the complete population;
- decision thresholds are specific and proportionate;
- required evidence is reliable and retained;
- failures are blocked, escalated, or corrected;
- no individual can approve their own high-risk decision without appropriate challenge;
- dependencies are identified and tested;
- the control remains effective after system, vendor, legal, or process change.

## Common design deficiencies

Examples include:

- vague control statements;
- unclear ownership;
- frequency too low for the risk;
- incomplete scope;
- no defined evidence;
- reliance on self-attestation;
- no escalation path;
- no control over model or vendor changes;
- thresholds that are not measurable;
- human oversight without authority or competence;
- monitoring that cannot trigger suspension;
- duplicate controls with inconsistent requirements.

## GlobalWay Travel Services example

GlobalWay requires an AI classification review before production deployment. The walkthrough shows that the review form is complete, but the deployment pipeline does not require evidence of approval. A product team could therefore deploy without classification.

The control is operating as documented, but its design is ineffective. GlobalWay adds a mandatory release gate that verifies approved classification, privacy, security, and human-oversight records before deployment can proceed.

## Control activities

- Define design criteria for key AI controls.
- Trace each control to risks and requirements.
- Perform walkthroughs with owners and performers.
- Evaluate population, timing, thresholds, evidence, and escalation.
- Test override and bypass paths.
- Document dependencies and complementary controls.
- Conclude effective, partially effective, or ineffective.
- Require remediation before relying on operating-effectiveness testing.

## Evidence

- control descriptions;
- requirement and risk mappings;
- process maps;
- walkthrough records;
- system configurations;
- workflow and release-gate screenshots;
- role and authority matrices;
- evidence specifications;
- design-test workpapers;
- deficiency and remediation records.

## Audit tests

1. Select key AI controls and trace them to stated risks and requirements.
2. Walk through each control from trigger to evidence and escalation.
3. Confirm the control covers the complete relevant population.
4. Evaluate whether frequency and precision match the risk.
5. Inspect override, exception, and bypass paths.
6. Confirm information used by the control is complete and reliable.
7. Determine whether the control could achieve its objective if operated as designed.

## Metrics

- key controls with effective design;
- design deficiencies by severity;
- controls with incomplete population coverage;
- controls without reliable evidence;
- controls vulnerable to override;
- average time to remediate design deficiencies;
- repeat design failures.

## Management checklist

- Would this control prevent or detect the intended failure in time?
- Does it cover every relevant system and transaction?
- Are thresholds, evidence, and escalation explicit?
- Can the control be bypassed?
- Are performers competent and independent?
- Are dependencies and complementary controls understood?

## Figure specification — Design-Effectiveness Decision Path

Create a decision path from risk and requirement through control objective, design attributes, walkthrough, population coverage, timing, evidence reliability, escalation, override testing, and conclusion. Branch to effective, partially effective, or ineffective design.

**Alt text:** Design-effectiveness testing path from risk and requirement mapping through walkthrough, scope, timing, evidence, escalation, override testing, and the final design conclusion.