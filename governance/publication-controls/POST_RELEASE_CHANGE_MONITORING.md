# Post-Release Change Monitoring

Publication is not the end of the control lifecycle. Every released manual must remain subject to monitored change triggers.

## Review triggers

Monitor for:

- new or amended laws/regulations;
- standards revisions, amendments, corrigenda, withdrawals, or superseding editions;
- official regulator or standards-body guidance changes;
- authoritative source URL changes or broken links;
- framework revisions (for example NIST profiles/frameworks used in crosswalks);
- major vendor/supplier or technology changes that invalidate implementation guidance;
- translation corrections or terminology changes;
- accessibility defects;
- security or workflow defects affecting publication integrity;
- reader-reported factual or implementation errors;
- discovered citation, DOI, metadata, or provenance inconsistencies.

## Review cadence

Each source registry record should retain a review interval appropriate to its volatility. In addition, conduct an event-driven review whenever a material trigger is detected.

## Impact classification

Classify detected change as:

- `NO IMPACT`: monitored and documented; no manual change required.
- `EDITORIAL`: wording/link/metadata correction with no implementation meaning change.
- `SUBSTANTIVE`: changes implementation meaning, control design, obligation interpretation, risk treatment, audit/evidence expectations, or localized meaning.
- `RELEASE-BLOCKING`: current published content may materially mislead implementation or evidence decisions.

## Required impact analysis

For `SUBSTANTIVE` or `RELEASE-BLOCKING` changes, identify:

- affected manual/chapter/control;
- affected authoritative source and version;
- affected translations;
- affected diagrams/graphics;
- affected DOCX/PDF artifacts;
- affected crosswalks and evidence templates;
- whether the current release requires correction, new version, warning notice, or withdrawal.

## Re-entry rule

A material change sends the affected content back through every impacted gate. Typical re-entry is:

source verification → controlled-source update → translation/semantic review → editorial QA → human approval → graphics/document regeneration → accessibility/security QA → new release manifest → GitHub/Zenodo update.

Do not rerun unaffected gates merely for appearance; do not skip an affected gate for convenience.

## Monitoring record

Record:

- trigger date;
- source/event;
- reviewer;
- impact classification;
- affected files/releases;
- action decision;
- branch/PR if remediation is required;
- target version;
- closure evidence.
