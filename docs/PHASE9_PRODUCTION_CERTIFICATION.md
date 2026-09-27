# Phase 9 — Production certification and controlled release

Phase 9 converts the production-readiness machinery from Phase 8 into evidence
that can support an exact controlled release. It remains fail-closed.

## Improvement 54 — immutable production environment contract

The production build contract is now pinned to:

- Python 3.12.14;
- linux/amd64;
- Docker Official Image `python:3.12.14-slim-bookworm`;
- exact amd64 manifest digest
  `sha256:1aaa65a85fda306ffb8b910824d4e93bdce61e212c7e87168123ea3073b41a1a`;
- no Python package dependencies;
- no network package installation inside the production build image.

The dependency contract is
`config/production_dependency_lock.json`. Its exact SHA-256 is
`de09ea78579a73a8236914019c13d3e7b7a8b83829209e770bf8dc424cd7e656`.

`Dockerfile.production` pins the exact base manifest. The PDF inspection
toolchain remains a separate contract because the Phase 8 hosted-CI Poppler
baseline must not be silently reinterpreted as an immutable production image.

Run:

`python scripts/production_environment_certification.py --output phase9-production-environment.json`

A valid contract is not certification. Phase 9 remains blocked until CI actually
builds/inspects the production image and separately supplies the immutable PDF
toolchain digest and reproducibility evidence. The script never changes
`production_toolchain.json` to `VERIFIED` by itself and never authorizes
publication.


### Runtime/source separation

The immutable production container contains the runtime/toolchain only. Repository
content is mounted into `/workspace` at execution time. This prevents
`config/production_toolchain.json` from being copied into the image whose digest
that same file records, eliminating a self-referential certification loop.

The environment image uses `SOURCE_DATE_EPOCH=0` during certification so its
content-addressed ID depends on the environment definition, not the source commit
timestamp.


## Improvement 55 — immutable PDF inspection toolchain

The PDF inspection environment is isolated from the Python runtime image and
pinned independently. Its contract uses:

- Ubuntu 24.04 linux/amd64 at exact manifest
  `sha256:496754492fb28b4d3049432f2ca787449331e23fb14f0dd3fffea86bf5a93eb4`;
- Ubuntu Snapshot ID `20260927T120000Z`;
- `poppler-utils=24.02.0-1ubuntu9.9`;
- expected `pdftotext` and `pdfinfo` version 24.02.0.

`Dockerfile.pdf-tools` installs only from that snapshot, verifies the exact
package and tool versions, and removes mutable apt indexes, caches, and logs
before export.

The Phase 9 certification workflow builds the PDF image independently on two
isolated BuildKit runners and compares their OCI manifest digests. Until both
builds reproduce and the resulting digest is pinned into
`config/production_toolchain.json`, the PDF toolchain remains blocked and the
overall production toolchain remains `REVIEW_REQUIRED`.

No PDF-toolchain certification authorizes publication.


## Improvement 55 — immutable PDF inspection runtime

The PDF runtime is separately pinned to the exact Ubuntu 24.04 amd64 base
manifest, Ubuntu snapshot `20260927T120000Z`, and
`poppler-utils=24.02.0-1ubuntu9.9`.

BuildKit may vary OCI creation/history metadata between otherwise identical
builds. Phase 9 therefore certifies a canonical runtime digest that retains the
runtime architecture, OS, executable OCI config, and a canonical inventory of
runtime filesystem paths, file bytes, symlink targets, permissions, and
ownership. It intentionally excludes volatile OCI `created`/history timestamps,
tar mtimes, and compressed-layer transport metadata.

Two isolated BuildKit jobs must independently produce the same canonical runtime
digest. Raw OCI manifest digests remain recorded as diagnostic evidence but are
not treated as equivalent when only volatile metadata differs.

This certification remains non-authorizing and does not satisfy any human
publication approval.
