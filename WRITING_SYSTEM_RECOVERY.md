# Writing System Recovery and Rollback

This runbook covers the controlled writing-quality subsystem: grammar/style QA, context routing, semantic-preservation checks, approved-feedback rules, multilingual controls, publication validation, and quality telemetry.

## Recovery principles

The repository is the source of truth. Generated DOCX/PDF artifacts, temporary CI reports, local caches, and tool downloads are never the sole authoritative copy of configuration or controlled content.

Recovery must be deterministic and fail closed. Do not reconstruct a lost rule from memory, accept an unreviewed tool upgrade, or silently regenerate a publication package and treat it as approved.

## Minimum recovery package

A recoverable revision contains:

- `DOCUMENT_WRITING_STANDARD.md`;
- all `config/*writing*.json` policy and manifest files;
- writing QA and semantic QA scripts;
- context profiles;
- the explicitly approved feedback registry;
- regression tests;
- the pinned GitHub Actions workflow;
- manual-specific publication gates and release evidence where applicable.

## Standard rollback

1. Identify the last known-good commit or release tag.
2. Compare the writing-system files against that revision.
3. Revert only the defective writing-system change when practical; do not overwrite unrelated manual content.
4. Run:
   - `python scripts/writing_system_integrity.py`
   - `python -m unittest tests.test_document_writing_qa tests.test_manual03_end_to_end_qa tests.test_phase3_writing_system tests.test_phase4_controlled_publishing -v`
5. Run the Document Writing Quality workflow.
6. For any affected controlled manual, rerun its source-to-publication gate.
7. Do not release regenerated artifacts until their hashes, manifests, semantic/localization checks, and human release requirements are satisfied.

## Tool-version rollback

If LanguageTool, Vale, Python, Java, a GitHub Action, or document-generation tooling introduces regressions:

1. restore the last known-good pinned version;
2. verify the downloaded artifact checksum where applicable;
3. rerun regression tests and representative multilingual fixtures;
4. compare finding counts against the prior baseline;
5. record intentional policy changes separately from tool-version changes.

## Approved-feedback recovery

The approved-feedback registry is fail closed. An entry may influence writing only when it records explicit approval and provenance. After recovery, unapproved or provenance-free entries must not be inferred, recreated, or activated.

## Disaster test

At least quarterly, or after a material writing-system change:

1. check out a clean repository revision;
2. run the integrity preflight;
3. run all writing-system tests without local caches;
4. start the pinned local LanguageTool instance and run a representative English, es-419, and pt-BR check;
5. validate one controlled manual from source through publication artifacts;
6. document any non-reproducible dependency or recovery gap as a blocking maintenance defect.

A successful restore means the system can reproduce its validation behavior. It does not by itself re-approve old publication artifacts or replace required human review.


## Phase 4 repository-wide recovery

The controlled publication engine is manifest-driven. Recovery therefore also requires:

- `config/controlled_publication_manifest.schema.json`;
- `config/controlled_publications/index.json`;
- every onboarded per-manual manifest;
- round-trip, layout, accessibility, semantic, and observability QA scripts;
- the versioned observability baseline and history record.

Run the executable exercise with:

`python scripts/writing_system_recovery_exercise.py --require-pdf-tools`

Then run repository-wide publication validation:

`python scripts/controlled_publication_qa.py --index config/controlled_publications/index.json`

For every onboarded manual, run round-trip, layout, and accessibility QA before declaring recovery successful. A recovered environment that cannot reproduce those checks is not production-ready.
