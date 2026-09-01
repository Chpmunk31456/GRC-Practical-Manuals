# Manual 53 — Localization and Candidate Architecture

**Controlled stage:** 3 — scenario/evidence depth, localization architecture, and candidate-preparation design  
**Date:** 1 September 2026

## Objective

Prepare Manual 53 for controlled EN / es-419 / pt-BR publication without collapsing jurisdiction-specific privacy obligations into false equivalence.

## Controlled language package

Each locale will preserve the same control identifiers and evidence anchors while using natural professional language appropriate to the locale.

- English: canonical source language for control IDs, evidence IDs, source-status qualifiers, and cross-jurisdiction comparison logic.
- es-419: Latin American Spanish, preserving legal-source names and jurisdiction-specific terms where translation could alter legal meaning.
- pt-BR: Brazilian Portuguese, preserving LGPD-specific terminology and distinguishing Brazilian legal concepts from GDPR or other regimes.

## Mandatory parity anchors

Every locale must preserve:

1. lawful/authorized data-use decision points;
2. AI data inventory, provenance, lineage, and purpose;
3. data minimisation and sensitive-data controls;
4. training, tuning, evaluation, RAG, vector-store, and prompt/context boundaries;
5. retention, deletion, correction, and rights-support workflows;
6. cross-border transfer analysis;
7. DPIA / AI-impact-assessment integration;
8. third-party/provider data controls;
9. incident, breach, change, and revalidation controls;
10. evidence and residual-risk decision records.

## Jurisdiction separation rule

Localized publication must not imply that GDPR, LGPD, Colombian privacy law, U.S. state privacy laws, or other regimes are interchangeable. Each jurisdiction/source row must identify scope, applicability trigger, relationship to the enterprise control, evidence expectation, and limitation.

## Candidate build design

The deterministic candidate builder will:

- ingest one controlled Markdown source per locale;
- generate one DOCX and one PDF per locale;
- preserve stable heading/control structure;
- record SHA-256 and byte count for all six binaries;
- produce a candidate manifest tied to the exact source commit;
- run visible-text validation on every PDF;
- raster-render at least the first page of every PDF;
- check parity anchors across all locales;
- fail closed on missing or empty artifacts.

## Candidate freeze gates

Before freezing the Manual 53 six-binary candidate:

- reverify fast-moving privacy/regulatory source status;
- confirm jurisdiction rows do not overstate legal equivalence;
- confirm scenario/evidence coverage is release-depth;
- complete controlled EN / es-419 / pt-BR sources;
- run deterministic build and render validation;
- record exact candidate provenance.

## Stage-3 completion criterion

Stage 3 is complete when the jurisdiction/source matrix, scenarios, evidence model, control architecture, localization design, and deterministic-candidate specification are sufficient to begin controlled trilingual source construction without reopening the core architecture.