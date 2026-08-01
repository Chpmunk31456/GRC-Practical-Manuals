# Requirement Decomposition and Normalization

## 1. Map comparable units

Mappings fail when analysts compare units at different levels. A broad framework outcome cannot be treated as equivalent to a detailed technical requirement merely because both concern the same topic. Before mapping, decompose each source into comparable analytical units.

A useful requirement model separates:

- **actor** — who must act or remain accountable;
- **action** — what must be established, performed, prohibited, reviewed, or demonstrated;
- **object** — the system, information, process, person, supplier, facility, or record affected;
- **condition** — when, where, or under what trigger the requirement applies;
- **frequency or timing** — how often or within what period action is expected;
- **quality threshold** — required rigor, completeness, independence, or performance;
- **evidence expectation** — what records could demonstrate implementation or operation;
- **outcome** — the intended protection, governance result, or assurance objective;
- **exceptions** — explicit alternatives, compensating mechanisms, or applicability limits.

## 2. Preserve source identity

Every decomposed unit must retain its parent source identifier and version. Do not assign a new identifier that obscures the authoritative reference. If an organization creates sub-elements for analysis, use a transparent suffix such as `ORG-SEG-01` and record that it is an analytical segment, not an official source identifier.

## 3. Distinguish requirement types

Classify the source unit before normalizing it. Common types include:

- governance obligation;
- policy or procedure requirement;
- risk-management activity;
- technical safeguard;
- physical safeguard;
- workforce or training requirement;
- supplier requirement;
- monitoring or detection requirement;
- response or recovery requirement;
- privacy principle or individual right;
- documentation or retention requirement;
- assessment, testing, or assurance requirement;
- reporting or notification requirement.

Requirements of different types may support one another without being equivalent.

## 4. Write a normalized control objective

A normalized objective should be concise, technology-neutral where appropriate, and faithful to the source. Use this structure:

> The organization [action] [object] [condition or scope] to achieve [outcome], with [timing, quality, or evidence condition].

The normalized objective is an analytical aid. It must not replace or paraphrase away legally meaningful qualifiers.

## 5. Retain mandatory qualifiers

Words such as “shall,” “must,” “at least annually,” “without undue delay,” “reasonable,” “appropriate,” “independent,” and “documented” can materially alter the obligation. Record these qualifiers in dedicated fields or in the interpretation notes. Do not normalize them out merely to make two items appear similar.

## 6. Handle outcome-based and prescriptive sources

Outcome-based frameworks describe desired results and may allow multiple implementations. Prescriptive sources may specify methods, frequencies, technologies, or records. A prescriptive requirement may be one implementation path toward an outcome, but the outcome does not necessarily satisfy the prescriptive detail.

Record the relationship as “supports,” “partial overlap,” or another qualified type unless all relevant conditions align.

## 7. Manage source granularity

Use a granularity label:

- framework function or domain;
- category or objective;
- control family;
- control or requirement;
- control enhancement or subrequirement;
- implementation statement;
- assessment procedure;
- evidence attribute.

Mapping records should normally compare the same or adjacent granularity levels. High-level mappings may be retained for navigation, but they must not be used as detailed compliance assertions.

## 8. Identify hidden scope differences

Two requirements may look similar while differing in:

- protected data type;
- covered entity or regulated actor;
- internal versus external systems;
- production versus development environments;
- all assets versus high-risk assets;
- design requirement versus operating requirement;
- policy existence versus implementation evidence;
- preventive versus detective objective;
- organization-wide versus system-specific scope.

Document these differences before assigning relationship strength.

## 9. Decomposition quality checks

A decomposed requirement is ready for mapping when:

- the official source and version are traceable;
- the unit is understandable without changing its meaning;
- mandatory qualifiers are retained;
- applicability conditions are explicit;
- the granularity level is identified;
- the normalized objective is separate from source language;
- licensing restrictions are respected;
- an analyst can explain what evidence would and would not demonstrate the objective.
