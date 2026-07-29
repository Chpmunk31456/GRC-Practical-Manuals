# Chapter 116 — Technical Validation

## Purpose

This chapter explains how to plan, perform, and evaluate technical validation of AI systems as part of governance, compliance, and assurance work.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Organizations should validate that AI systems perform as intended within defined operating conditions and that accuracy, robustness, cybersecurity, resilience, data quality, human-oversight interfaces, and failure behavior are consistent with documented requirements and risk decisions.

## Plain-language explanation

Policies and approvals cannot prove that a system works safely. Technical validation tests the actual system, model, data, interfaces, controls, and operating conditions. It should determine not only whether average performance is acceptable, but also whether the system fails predictably, exposes affected groups to unequal harm, or behaves differently after change.

## Validation scope

Define:

- system and model versions;
- environments and configurations;
- intended purpose and prohibited uses;
- user groups and affected populations;
- input and output boundaries;
- data sources and preprocessing;
- external tools, APIs, and retrieval sources;
- performance and safety requirements;
- human-review and escalation paths;
- known limitations;
- deployment conditions and jurisdictions.

## Validation domains

Assess proportionately:

- functional correctness;
- accuracy and error rates;
- robustness to noisy, incomplete, or adversarial inputs;
- bias and subgroup performance;
- explainability and transparency outputs;
- human-oversight usability;
- cybersecurity and abuse resistance;
- privacy and data leakage;
- resilience and graceful degradation;
- logging and traceability;
- latency, capacity, and availability;
- change and regression behavior.

## Test design

Validation should include:

- representative normal cases;
- boundary and edge cases;
- rare but high-impact scenarios;
- known failure modes;
- out-of-distribution inputs;
- malicious or manipulative inputs;
- incomplete and conflicting data;
- low-confidence outputs;
- fallback and suspension conditions;
- multilingual and accessibility scenarios where relevant;
- materially affected groups;
- vendor and infrastructure failure scenarios.

## Performance criteria

Define approved criteria before testing, including:

- minimum acceptable performance;
- subgroup thresholds;
- maximum error or harm rates;
- confidence and abstention thresholds;
- escalation triggers;
- safe-stop conditions;
- tolerance for drift;
- required recovery behavior;
- criteria for production approval or rejection.

Avoid selecting thresholds after seeing results solely to justify deployment.

## Independent challenge

Use qualified reviewers who are sufficiently independent from development and business pressure. Independence may be achieved through a separate validation team, internal audit specialists, external assessors, or documented peer challenge, depending on risk and organizational size.

## Reproducibility and environment integrity

Preserve:

- model and code versions;
- prompts, system instructions, and tool configurations;
- datasets and sampling logic;
- test scripts;
- hardware and software environment;
- parameter settings;
- random seeds where applicable;
- vendor version information;
- raw results and analysis notebooks;
- approvals and limitations.

## Change and regression testing

Repeat or target validation after:

- model replacement or update;
- prompt or policy change;
- new retrieval source;
- data-pipeline change;
- infrastructure migration;
- new user group or jurisdiction;
- material vendor change;
- incident, complaint, or drift signal;
- new tool or agent capability;
- substantial modification.

## GlobalWay Travel Services example

GlobalWay validates an AI disruption assistant using routine itinerary questions, severe-weather scenarios, stale airline feeds, conflicting fare rules, low-confidence cases, prompt-injection attempts, multilingual requests, and accessibility tests. Average accuracy meets target, but the assistant fails to abstain when one supplier feed is stale.

GlobalWay blocks deployment until freshness checks, confidence thresholds, and human escalation are implemented and successfully retested.

## Control activities

- Approve a risk-based validation plan.
- Freeze and identify the system version under test.
- Define criteria before execution.
- Use representative, edge, failure, and adversarial scenarios.
- Evaluate subgroup and high-impact performance.
- Preserve reproducible technical evidence.
- Require independent challenge.
- block or restrict deployment when criteria are not met.
- Retest after remediation and material change.

## Evidence

- validation plan;
- requirements and acceptance criteria;
- system and model version records;
- dataset documentation;
- test cases and scripts;
- raw and summarized results;
- subgroup analyses;
- security and resilience test results;
- failure and abstention tests;
- reviewer challenge records;
- approvals, restrictions, and remediation;
- regression-test evidence.

## Audit tests

1. Confirm the validated version matches the version approved for deployment.
2. Verify acceptance criteria were defined before results were evaluated.
3. Review whether tests cover normal, edge, failure, adversarial, and subgroup scenarios.
4. Reperform selected tests or inspect reproducibility evidence.
5. Evaluate reviewer competence and independence.
6. Trace failed criteria to deployment restrictions and remediation.
7. Confirm material changes trigger regression testing.

## Metrics

- systems with current technical validation;
- validation criteria failed;
- subgroup performance gaps;
- unresolved high-severity defects;
- deployments blocked or restricted;
- time from remediation to retest;
- changes deployed without regression testing;
- reproducibility failures;
- incidents linked to untested scenarios.

## Management checklist

- Are we testing the exact system that will operate in production?
- Were criteria approved before testing?
- Do tests cover realistic failure and abuse scenarios?
- Are affected groups and high-impact cases represented?
- Can results be reproduced independently?
- Are failed criteria able to block deployment?
- Will material changes trigger revalidation?

## Figure specification — AI Technical Validation Matrix

Create a matrix connecting validation domains with test conditions: normal, boundary, subgroup, failure, adversarial, degraded, and recovery. Show acceptance criteria, independent challenge, remediation, retesting, and release decision as governance gates.

**Alt text:** AI technical-validation matrix connecting performance, fairness, security, resilience, privacy, oversight, and traceability domains to normal, edge, failure, adversarial, degraded, and recovery tests, followed by remediation and release decisions.