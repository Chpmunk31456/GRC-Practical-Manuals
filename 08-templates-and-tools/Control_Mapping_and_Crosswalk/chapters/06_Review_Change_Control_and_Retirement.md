# Review, Change Control, and Retirement

## 1. Treat mappings as controlled records

A mapping set is a versioned analytical product. It should have an owner, approved methodology, release identifier, effective date, source manifest, reviewer record, change log, and retirement process.

## 2. Establish review triggers

Review mappings when:

- either source framework or regulation changes;
- an official interpretation, erratum, or amendment is issued;
- source identifiers or control structures change;
- the organization's control design changes;
- system, service, data, entity, or jurisdiction scope changes;
- supplier or shared-responsibility arrangements change;
- audit findings challenge a relationship;
- evidence demonstrates that an assumed control does not operate as expected;
- licensing or source-access conditions change;
- the intended use of the mapping changes.

Also assign a periodic review date even when no event occurs.

## 3. Perform impact analysis

For each change, identify:

- affected mapping sets and rows;
- changed source meaning or identifier;
- affected organization controls;
- impacted evidence and tests;
- gaps created or closed;
- reports, dashboards, policies, and audit workpapers that depend on the mapping;
- users who must be notified;
- whether prior conclusions remain valid.

## 4. Version mapping sets

Use a controlled version scheme. A major version may reflect methodology or source-structure changes; a minor version may reflect approved additions or corrections. Record the exact source versions included in every release.

Do not overwrite an approved historical mapping without preserving the prior state.

## 5. Revalidate inherited and imported mappings

External mappings can accelerate analysis, but they remain third-party assertions. Before adoption:

- identify publisher and methodology;
- confirm source versions;
- review licensing and attribution;
- test representative relationships;
- identify scope assumptions;
- document local modifications;
- assign internal ownership and approval.

## 6. Retire mappings safely

Retirement is appropriate when a source is withdrawn, a relationship is invalidated, the intended use ends, or a replacement mapping is approved. A retired record should retain:

- retirement date;
- reason;
- approving authority;
- replacement record or version;
- affected reports and users;
- retention period;
- warning against future use.

## 7. Correct errors transparently

When an approved mapping is found to be wrong:

1. suspend affected claims or reports;
2. identify downstream use;
3. correct the mapping with review evidence;
4. notify relevant users;
5. reassess gaps, controls, and audit conclusions;
6. retain the correction history.

## 8. Quality assurance sampling

Periodically sample mapping records for:

- current source versions;
- complete identifiers;
- correct granularity;
- explicit direction and relationship type;
- supportable confidence;
- rationale and limitations;
- valid implementation and evidence links;
- independent review;
- timely review dates;
- absence of prohibited compliance claims.

## 9. Release criteria

A mapping release should fail closed if:

- required source records are missing;
- proprietary text is included without an established access basis;
- relationship definitions are inconsistent;
- unreviewed mappings are represented as approved;
- unresolved placeholders remain;
- source versions are unknown;
- confidence or limitations are omitted;
- output integrity checks fail.

## 10. Human-review boundaries

Automation can verify field counts, identifiers, dates, required values, broken references, checksum integrity, document structure, and some consistency rules. It cannot determine legal equivalence, interpret proprietary standards authoritatively, validate native-language nuance, or replace qualified audit and control judgment.
