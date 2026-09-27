# Phase 5 production operations

## Repository deployment (improvement 33)

Phase 4 was merged in PR #520 at `3decacbe04fa4f8843327c88eea8ffd793b663a4`.
The canonical manual catalog remains `.compliance/manual-catalog.json`.
Publication configurations remain in `config/controlled_publications`.
The rollout index records active manifests and candidate manifests separately.
A candidate is not publication-approved when automated checks pass.

Run `python scripts/repository_publication_qa.py --discover --output inventory.json`
to discover catalog coverage. Unconfigured manuals are reported as
`onboarding_required`; their eligibility and source conventions require review.
No manual is silently enrolled and no existing source or artifact is rewritten.

Run `python scripts/repository_publication_qa.py --output publication.json`
to execute publication integrity, semantic round-trip, layout and structural
accessibility checks for every registered manual, including candidates.
The process exits nonzero when any gate fails or cannot execute. Other gates
still run so the summary does not hide additional defects. Python 3.12, Git,
`pdftotext` and `pdfinfo` are required in the validation environment.

The JSON output records per-gate status and elapsed seconds. Console output
contains manual identifiers and statuses only. Extracted prose and exception
contents are excluded. Automated success grants no human publication approval.

To onboard a manual, review its source conventions, publication report,
checksums, review records and protected terms. Add a per-manual manifest in the
configuration directory and register it in the appropriate index lane. Every
controlled locale and mandatory validation control must remain enabled.
Duplicate, unregistered, malformed and escaping configurations fail closed.
The workflow discovers the index instead of maintaining a second manual list.

## Verification and limitations

Run `python -m unittest discover -s tests -v`,
`python scripts/writing_system_integrity.py`,
`python scripts/compliance_qa.py workflow-security`, and
`python scripts/workflow_trigger_dependency_qa.py` before submitting changes.
The Controlled Publication Quality workflow runs the full unit suite and all
registered document gates. Existing writing QA and recovery controls remain.

Manual 03 and Manual 04 are the initial integration targets. Manual 04 remains
in the candidate lane with human semantic review outstanding. All other catalog
entries retain their existing publication state and are listed for onboarding.
This change generalizes validation; it does not regenerate approved documents
or certify their accessibility. Source monitoring, lifecycle, release,
accessibility, maintenance and optimization extensions follow in improvements
34 through 40 with separate review evidence.

## Authoritative source monitoring (improvement 34)

The existing scheduled Source Watch checks registry deadlines and URLs, then runs
`python scripts/source_monitoring.py --network --output source-review-queue.json`.
The queue contains source identifiers, revision metadata, content hashes,
review reasons and affected chapters. Response bodies are not retained.
Redirects must remain on the existing authoritative-domain allowlist.

`config/source_monitoring.json` supplements the canonical source registry.
Baselines begin empty: existing URL verification is not content-hash approval.
A human must review and commit the publication date, revision, exact SHA-256
and approval evidence before a source can be reported current. Changed content,
missing observations, overdue dates and missing mappings produce review items.
No observation rewrites a manual or replaces a baseline. Whole-manual mappings
for the initial two manuals are conservative; other mappings remain outstanding.
The scheduled workflow retains metadata for 30 days. Durable review decisions
belong in repository-controlled evidence through a reviewed pull request.

## Translation lifecycle (improvement 35)

Run `python scripts/translation_lifecycle.py --output translation-lifecycle.json`.
The report binds each controlled Spanish and Portuguese source inventory to the
English inventory and terminology policy. Added, removed or changed files reopen
review. Impact mapping conservatively includes every chapter of the manual.
Regional locales and existing protected terms remain unchanged.

`config/translation_lifecycle.json` contains dependency snapshots and review
records. An observation is not approval. Review records require the reviewer,
date, decision, exact source and translation hash maps, terminology hash, and an
existing evidence file with its SHA-256. Changed evidence invalidates the record.
The initial records are empty because existing reviews have not been migrated
and verified against this exact contract. The report therefore requires review.
Even current translation evidence is not independent publication approval.

## Publication quality dashboard (improvement 36)

Run `python scripts/publication_dashboard.py --output dashboard.json --summary dashboard.md`.
Both outputs cover source currency, translation review, writing and regression
results, DOCX/PDF validation, accessibility, visual review and release approval.
Collection checks the available publication and lifecycle controls. Evidence
that was not supplied remains missing; structural accessibility checks alone
cannot complete the independent accessibility review.

For a consolidated evidence package, pass `--evidence evidence.json --revision SHA`.
Each category requires a status, exact source revision, timezone-aware observation
time and unresolved-defect list. Evidence expires after 24 hours. Missing,
stale, failed and pending categories block readiness. Approval history is shown
as supplied evidence, not authenticated by the dashboard. The release gate must
independently verify approvals before publication. The dashboard never grants
publication authorization, even when every category has passing evidence.

## Controlled releases (improvement 37)

Release verification is explicit and read-only:
`python scripts/controlled_release.py candidate.json --first-build BUILD1 --second-build BUILD2 --output release-check.json`.
Release verification requires a clean checkout at the exact candidate SHA.
The manual must be active. Both independent builds must reproduce every declared
DOCX/PDF hash. Source, translation, accessibility and visual evidence must match.
It reruns publication and lifecycle controls. No command publishes or merges.

A candidate records `manual_id`, semantic `version`, `source_revision`,
`pull_request`, `toolchain_sha256`, and path-to-SHA-256 maps named `artifacts`,
`source_provenance`, `translation_evidence`, `accessibility_evidence` and
`visual_evidence`. Every locale's DOCX and PDF must be present. Each build directory
contains `build-receipt.json` with the same revision and toolchain hash and a
unique `build_id`. Build execution and receipt provenance require review; byte
comparison alone does not prove that an independent build actually occurred.

Two authorized human reviewers must independently approve the exact PR head.
Their GitHub approval bodies must include `Publication approval: SHA256=DIGEST`,
where DIGEST is the canonical candidate fingerprint produced by
`controlled_release.fingerprint`. The PR author and bots cannot satisfy this gate.
Dismissed or superseded approvals, changed hashes and missing CI checks block it.
The approver policy is fetched from `main`, never from the candidate branch.
The initial reviewer allowlist is empty and must be configured through governance.
No human identity or approval has been invented. The required toolchain manifest
is supplied by the maintenance improvement; until then release remains blocked.

A successful verification is evidence for the controlled publication process.
It is not a standalone publication command. Existing release-manifest governance
and final human publication approval continue to apply.

## Accessibility validation (improvement 38)

Run `python scripts/accessibility_validation.py --output accessibility-review.json`.
DOCX checks cover heading hierarchy, locale, header-row structure, alternative
text, declared font compatibility and title metadata. PDF checks use `pdfinfo`
and `pdffonts` for tagging, title, encryption, embedding and Unicode mappings.
Uncertain structures remain review requirements rather than automatic passes.

Independent review must cover reading order, screen-reader behavior, table
relationships, alternative-text meaning, font compatibility and visual layout.
Records in `config/accessibility_reviews.json` require distinct producer and
reviewer identities, exact artifact hashes, date, decision, all review scopes,
and a hashed evidence file. The initial review map is empty.
The controlled release verifier blocks on unresolved structural findings or
missing independent review. Passing automatic checks never establishes that a
document is fully accessible. Existing approved binaries remain unchanged;
remediation that changes them requires regeneration and renewed approval.
