#!/usr/bin/env python3
"""Validate localized DOCX package integrity and embedded local images."""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlparse
from xml.etree import ElementTree


EXPECTED_DOCX_COUNT = 22
IMAGE_RELATIONSHIP_TYPE = (
    "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image"
)
MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*]\((?:<([^>]+)>|([^) \t]+))(?:[ \t]+[^)]*)?\)")
HTML_IMAGE_RE = re.compile(
    r"<img\b[^>]*\bsrc\s*=\s*[\"']([^\"']+)[\"'][^>]*>", re.IGNORECASE
)


def localized_markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if path.parent.name in {"Espanol", "Portugues_BR"}
    )


def local_image_targets(source: Path) -> set[Path]:
    text = source.read_text(encoding="utf-8")
    references = [
        match.group(1) or match.group(2) for match in MARKDOWN_IMAGE_RE.finditer(text)
    ]
    references.extend(match.group(1) for match in HTML_IMAGE_RE.finditer(text))

    targets: set[Path] = set()
    for reference in references:
        parsed = urlparse(reference)
        if parsed.scheme or parsed.netloc or reference.startswith("#"):
            continue
        target = source.parent / unquote(parsed.path)
        if target.is_file():
            targets.add(target.resolve())
    return targets


def inspect_docx(docx: Path) -> tuple[int, int]:
    try:
        with zipfile.ZipFile(docx) as package:
            bad_member = package.testzip()
            if bad_member:
                raise ValueError(f"CRC failure in {bad_member}")

            media_count = sum(
                1
                for name in package.namelist()
                if name.startswith("word/media/") and not name.endswith("/")
            )
            relationships = ElementTree.fromstring(
                package.read("word/_rels/document.xml.rels")
            )
    except (KeyError, OSError, ValueError, zipfile.BadZipFile) as exc:
        raise ValueError(f"invalid DOCX package: {exc}") from exc

    relationship_count = sum(
        1
        for relationship in relationships
        if relationship.attrib.get("Type") == IMAGE_RELATIONSHIP_TYPE
        and relationship.attrib.get("Target", "").startswith("media/")
    )
    return media_count, relationship_count


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    sources = localized_markdown_files(root)
    packages = sorted(source.with_suffix(".docx") for source in sources)
    failures: list[str] = []

    if len(packages) != EXPECTED_DOCX_COUNT:
        failures.append(
            f"expected {EXPECTED_DOCX_COUNT} localized DOCX packages, found {len(packages)}"
        )

    for source, docx in zip(sources, packages):
        if not docx.is_file():
            failures.append(f"missing DOCX package: {docx.relative_to(root)}")
            continue

        try:
            media_count, relationship_count = inspect_docx(docx)
        except ValueError as exc:
            failures.append(f"{docx.relative_to(root)}: {exc}")
            continue

        image_targets = local_image_targets(source)
        if image_targets and media_count == 0:
            failures.append(
                f"{docx.relative_to(root)}: source has {len(image_targets)} "
                "resolvable local image reference(s), but DOCX has no embedded media"
            )
        if image_targets and relationship_count == 0:
            failures.append(
                f"{docx.relative_to(root)}: source has resolvable local images, "
                "but DOCX has no embedded image relationships"
            )

        print(
            f"{docx.relative_to(root)}: "
            f"source_images={len(image_targets)} "
            f"media={media_count} image_relationships={relationship_count}"
        )

    if failures:
        print("\nDOCX embedded-media validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(
        f"\nValidated {len(packages)} localized DOCX packages; "
        "all packages are valid ZIP archives and sources with resolvable local "
        "images have embedded media relationships."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
