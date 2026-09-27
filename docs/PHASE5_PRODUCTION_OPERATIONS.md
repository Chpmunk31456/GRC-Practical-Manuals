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
