# Chapter 115 — Sampling and Evidence Evaluation

## Purpose

This chapter defines practical standards for selecting samples and evaluating whether evidence is sufficient, appropriate, reliable, relevant, and complete for AI governance and compliance assurance.

AI may support human decision-making, but it must not remove human responsibility, judgment, or accountability.

## Requirement

Assurance conclusions should be based on evidence that is sufficient in quantity and appropriate in quality. Sampling methods should be documented, risk-based, reproducible where practicable, and capable of supporting the stated conclusion without overstating assurance.

## Plain-language explanation

Auditors rarely inspect every record. They must therefore select evidence carefully and understand what the sample can and cannot prove. A convenient sample of successful approvals cannot demonstrate that all deployments were controlled if failed, cancelled, emergency, or manually overridden deployments were excluded.

## Evidence qualities

Evaluate:

- relevance to the objective;
- reliability of the source;
- completeness and accuracy;
- authenticity and integrity;
- timeliness;
- level of detail;
- consistency with other evidence;
- independence of preparation;
- reproducibility;
- retention and chain of custody.

Externally generated or independently validated evidence may be stronger, but source alone does not determine reliability.

## Population definition

Before sampling, document:

- population purpose;
- source systems;
- date range;
- inclusion and exclusion rules;
- expected record count;
- duplicate handling;
- cancelled, failed, emergency, or overridden items;
- reconciliation to authoritative records;
- known data limitations.

## Sampling approaches

Use as appropriate:

- random sampling;
- systematic sampling;
- stratified sampling;
- targeted or judgmental sampling;
- monetary or impact-based sampling;
- attribute sampling;
- full-population analytics;
- event-triggered sampling;
- specialist technical selection.

Judgmental samples may identify risk but do not support statistical projection unless designed for that purpose.

## Risk-based stratification

Consider separate strata for:

- high-risk systems;
- prohibited-practice screening decisions;
- material model or vendor changes;
- incidents and complaints;
- sensitive data processing;
- low-confidence outputs;
- overrides and exceptions;
- failed controls;
- high-impact decisions;
- specific countries, business units, or user groups.

## Sample size considerations

Determine sample size based on:

- control frequency;
- population size;
- risk severity;
- reliance planned;
- expected deviation rate;
- evidence quality;
- degree of automation;
- prior findings;
- population variability;
- whether statistical projection is intended.

Document professional judgment and limitations.

## Conflicting or missing evidence

When evidence conflicts or is incomplete:

- identify the authoritative source;
- obtain corroborating records;
- investigate system and process differences;
- expand the sample where warranted;
- assess whether missing evidence represents control failure;
- document unresolved uncertainty;
- limit or qualify the conclusion.

Absence of required evidence should not automatically be treated as proof that a control operated.

## GlobalWay Travel Services example

GlobalWay provides a spreadsheet listing 200 AI changes. The auditor reconciles it to deployment logs and identifies 18 emergency changes and 7 vendor-controlled updates omitted from the spreadsheet. The population is therefore incomplete.

The auditor reconstructs the population, stratifies emergency and vendor changes, selects all high-impact items plus a random sample of routine changes, and qualifies conclusions where vendor evidence remains unavailable.

## Control activities

- Define and reconcile complete populations.
- Select a sampling method suited to the objective.
- Include high-risk and exception strata.
- Document sample logic and reproducibility.
- Assess evidence reliability and integrity.
- Corroborate management-prepared evidence.
- Expand testing when deviations or gaps arise.
- qualify conclusions when evidence is insufficient.

## Evidence

- population definitions;
- reconciliations;
- source-system extracts;
- sampling methodology;
- random seeds or selection logic where applicable;
- selected-item lists;
- evidence-reliability assessments;
- chain-of-custody records;
- corroboration results;
- limitations and qualified conclusions.

## Audit tests

1. Verify that the population matches the audit objective and period.
2. Reconcile population totals to authoritative sources.
3. Confirm high-risk, failed, emergency, and overridden items were considered.
4. Evaluate whether the sample method and size support the conclusion.
5. Inspect the reliability of management and system-generated evidence.
6. Trace selected items to original records.
7. Review whether deviations or missing evidence required expanded testing or qualification.

## Metrics

- populations requiring reconstruction;
- unreconciled records;
- evidence gaps;
- samples expanded because of deviations;
- management-prepared reports failing reliability tests;
- qualified assurance conclusions;
- repeated evidence-retention failures.

## Management checklist

- Is the population complete and reconciled?
- Does the sample include high-risk and exception items?
- Is the evidence authentic, reliable, and timely?
- Can the selection be reproduced?
- Are limitations and uncertainty clearly stated?
- Does the evidence actually support the conclusion?

## Figure specification — Evidence Reliability Pyramid and Sampling Flow

Create a combined visual showing an evidence-reliability pyramid and a sampling flow from objective and population definition through reconciliation, stratification, selection, testing, deviation analysis, and conclusion.

**Alt text:** Evidence-reliability pyramid beside a sampling flow from audit objective and population reconciliation through stratification, selection, testing, deviation analysis, and conclusion.