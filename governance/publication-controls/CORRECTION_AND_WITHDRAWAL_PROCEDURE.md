# Correction and Withdrawal Procedure

Use this procedure when a material error is discovered after publication. Never silently overwrite published evidence or erase the historical record.

## 1. Intake and triage

Record:

- affected manual/version/language;
- reporter/source;
- date detected;
- affected claim, control, graphic, citation, artifact, DOI, or metadata;
- evidence supporting the concern.

Classify severity:

- `LOW`: cosmetic/editorial issue with no implementation impact.
- `MEDIUM`: meaningful clarity or usability issue; implementation meaning remains substantially intact.
- `HIGH`: material error could lead to incorrect control, evidence, risk, audit, or compliance decisions.
- `CRITICAL`: published content materially misstates a binding requirement, normative standard meaning, safety/security boundary, certification/conformity claim, or other point that could cause serious reliance harm.

## 2. Immediate containment

For HIGH or CRITICAL issues:

- add a visible warning/correction notice where practical;
- stop promoting the affected artifact as current;
- preserve the affected release and evidence;
- open a controlled maintenance branch and PR;
- identify whether Zenodo or other publication metadata needs a notice or new version.

Do not delete or replace the historical release merely to hide the defect.

## 3. Root cause and scope

Determine whether the issue originated in:

- authoritative-source research;
- controlled English source;
- translation/terminology;
- editorial revision;
- graphic/visual simplification;
- DOCX/PDF generation;
- accessibility processing;
- release metadata/DOI handling;
- repository/security workflow.

Identify every affected language, chapter, graphic, template, artifact, crosswalk, and downstream release.

## 4. Corrective action

Use a protected-branch workflow:

1. create/update a maintenance branch;
2. correct the controlled source first where substantive meaning is affected;
3. rerun every affected downstream gate;
4. regenerate affected artifacts;
5. complete human approval when semantic meaning changed;
6. perform release/security QA;
7. generate a new release manifest and checksums;
8. publish a new version rather than overwriting historical release bytes.

## 5. Release decision

Choose one:

- `CORRECTION NOTICE ONLY`: historical artifact remains usable with a documented non-material correction.
- `NEW PATCH/MINOR VERSION`: corrected release supersedes the prior version.
- `WITHDRAW CURRENT VERSION`: affected version should not be relied upon; retain historical provenance and publish a replacement when ready.
- `NO CHANGE`: concern investigated and not substantiated; preserve the decision evidence.

## 6. GitHub and Zenodo handling

- Preserve original tags/releases unless an exceptional repository-integrity issue requires otherwise.
- Publish the corrected material as a new version/tag.
- Update README/CITATION/current-version pointers to the corrected release.
- Reconcile Zenodo version DOI and concept DOI after publication.
- Clearly link the replacement to the superseded/withdrawn version where supported.
- Never reuse a prior checksum for changed bytes.

## 7. Closure evidence

Record:

- severity and root cause;
- branch/PR;
- corrected commit SHA;
- affected and regenerated files;
- human approval evidence;
- QA results;
- new release/tag;
- new Zenodo version DOI if applicable;
- supersession/withdrawal notice;
- monitoring action to prevent recurrence.

## Principle

Corrections must improve trust through traceability. Historical records should show what changed, why it changed, who approved the correction, and which release supersedes the affected material.
