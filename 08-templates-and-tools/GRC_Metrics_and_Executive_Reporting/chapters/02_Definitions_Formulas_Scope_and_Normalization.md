# Definitions, Formulas, Scope, and Normalization

## Controlled definition

Every approved measure needs a stable definition. At minimum, record the name, identifier, class, purpose, owner, audience, scope, population, inclusion and exclusion rules, numerator, denominator, unit, formula, direction of favorable movement, reporting period, frequency, data sources, calculation method, threshold logic, limitations, and version.

A label such as “patch compliance” is insufficient. It may refer to devices patched within a service-level target, the percentage with no overdue critical findings, or the percentage successfully scanned. These are materially different measures.

## Numerators and denominators

Ratios must define both numerator and denominator at the same point in time and under compatible scope rules. Report excluded, unknown, unscanned, unavailable, and newly onboarded populations separately when they could change interpretation.

Do not silently remove failed, missing, or late records from the denominator. If data quality requires exclusion, record the reason, amount, approval, and effect on the result.

## Time and cohort controls

Specify whether the measure is a point-in-time snapshot, period total, rolling average, cohort result, cumulative value, or rate. Define event dates, cutoff times, time zones, reopened items, and late-arriving data. Comparative periods must use equivalent duration and scope unless the report discloses the difference.

## Normalization

Raw counts can be misleading when organization size or exposure changes. Normalize only when the denominator represents the decision context. Examples include incidents per thousand endpoints, overdue actions per active finding, or exceptions per material supplier. Publish the raw count with the normalized rate when both are relevant.

Normalization must not conceal concentration risk. A low enterprise-wide rate may coexist with severe exposure in one business unit, jurisdiction, platform, or critical service.

## Aggregation

Do not average percentages with unequal denominators unless the method is mathematically appropriate and documented. Enterprise aggregation should normally recompute from source numerators and denominators or use an approved weighting model. Record weights, rationale, sensitivity, and known distortion.

Red, amber, and green states must derive from documented rules. Avoid averaging ordinal maturity scores or traffic-light states as though they were interval data unless the approved model explicitly supports that treatment.

## Changes and restatement

Formula, scope, threshold, source, or frequency changes require version control and impact assessment. Determine whether prior periods must be recalculated. If not restated, mark the break in series and explain why comparisons are limited.

## Reproducibility

An independent reviewer should be able to reproduce the result from retained source data, transformation rules, code or workbook logic, and the approved definition. Manual adjustments must retain the original value, revised value, reason, approver, date, and supporting evidence.