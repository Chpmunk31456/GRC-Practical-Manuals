# Data Lineage, Quality, and Validation

## Lineage

Each reported result must trace to authoritative source systems, extracts, transformations, calculations, adjustments, and publication outputs. Record source owners, system identifiers, query or report names, extraction timestamps, filters, joins, mapping tables, and storage locations.

Screenshots and manually copied totals may support review but should not replace reproducible source evidence when system data are available.

## Quality dimensions

Assess at least completeness, accuracy, validity, consistency, timeliness, uniqueness, and traceability. Define acceptance criteria appropriate to the decision. A board report may require stronger validation than an exploratory operational view.

Unknown and missing values are data, not zero. Report their quantity and potential effect. Do not convert “not assessed,” “not applicable,” and “no issue” into the same value.

## Validation controls

Use automated schema, range, type, duplicate, reconciliation, and referential-integrity checks where practical. Add reasonableness review, source-to-report sampling, prior-period comparison, and independent formula review.

Quality exceptions must identify the affected metric, period, records, root cause, estimated effect, compensating review, owner, corrective action, and decision on publication.

## Timeliness

Define the measurement date, data cutoff, extraction time, refresh cadence, and expected latency. A precisely calculated stale result can still mislead. Reports should disclose material lag and whether late data will trigger restatement.

## Change control

Source-system changes, field renaming, migrations, new business units, acquisitions, and process redesign can break comparability. Data owners must notify metric owners before implementation when possible. Validate mapping and parallel-run results before relying on the revised pipeline.

## Access and retention

Restrict source and intermediate data according to sensitivity. Retain enough evidence to reproduce reported results and support review, while observing privacy, contractual, records-management, and legal requirements.

## Quality rating

A quality rating should summarize documented tests, not replace them. Define the rating scale, evidence, reviewer, and effect on use. If quality is below the approved minimum, suppress the result or publish it with a prominent limitation and an approved decision rationale.