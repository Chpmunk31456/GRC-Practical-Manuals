#!/usr/bin/env python3
"""Fail-closed QA for release-manifest governance controls.

This check validates the repository-owned JSON Schema and the structural contract
of the YAML template without adding network or third-party package dependencies.
It does not treat a template as an approved release manifest.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / ".compliance" / "release-manifest.schema.json"
TEMPLATE_PATH = (
    REPO_ROOT
    / "governance"
    / "publication-controls"
    / "release-manifest.template.yaml"
)


class ValidationError(Exception):
    """Raised when a release-manifest control fails closed."""


def load_schema() -> dict:
    try:
        value = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationError("release-manifest schema is missing") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(f"release-manifest schema is invalid JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ValidationError("release-manifest schema root must be an object")
    return value


def unique_keys(keys: list[str], label: str) -> set[str]:
    duplicates = sorted(key for key, count in Counter(keys).items() if count > 1)
    if duplicates:
        raise ValidationError(f"{label} contains duplicate keys: {', '.join(duplicates)}")
    return set(keys)


def mapping_keys(text: str, indent: int, label: str) -> set[str]:
    prefix = " " * indent
    pattern = re.compile(rf"^{re.escape(prefix)}([A-Za-z0-9_-]+):(?:\s|$)", re.MULTILINE)
    return unique_keys(pattern.findall(text), label)


def artifact_keys(text: str) -> set[str]:
    first = re.findall(r"^  - ([A-Za-z0-9_-]+):(?:\s|$)", text, re.MULTILINE)
    rest = re.findall(r"^    ([A-Za-z0-9_-]+):(?:\s|$)", text, re.MULTILINE)
    return unique_keys(first + rest, "artifact template")


def required_keys(schema: dict, label: str) -> set[str]:
    required = schema.get("required")
    properties = schema.get("properties")
    if not isinstance(required, list) or not all(isinstance(item, str) for item in required):
        raise ValidationError(f"{label}.required must be a string array")
    if not isinstance(properties, dict):
        raise ValidationError(f"{label}.properties must be an object")
    required_set = unique_keys(required, f"{label}.required")
    property_set = set(properties)
    if required_set != property_set:
        missing = sorted(property_set - required_set)
        unknown = sorted(required_set - property_set)
        raise ValidationError(
            f"{label} must fail closed with every declared property required; "
            f"optional={missing}, unknown-required={unknown}"
        )
    if schema.get("additionalProperties") is not False:
        raise ValidationError(f"{label}.additionalProperties must be false")
    return required_set


def object_required(schema: dict, property_name: str) -> set[str]:
    value = schema["properties"].get(property_name)
    if not isinstance(value, dict) or value.get("type") != "object":
        raise ValidationError(f"schema property {property_name} must be an object")
    return required_keys(value, f"schema.properties.{property_name}")


def validate_schema(schema: dict) -> tuple[set[str], set[str]]:
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        raise ValidationError("schema must declare JSON Schema draft 2020-12")
    if schema.get("type") != "object":
        raise ValidationError("schema root type must be object")
    if schema.get("properties", {}).get("schema_version", {}).get("const") != "1.0":
        raise ValidationError("schema_version must be fixed at 1.0")
    if schema.get("properties", {}).get("repository", {}).get("const") != (
        "Chpmunk31456/GRC-Practical-Manuals"
    ):
        raise ValidationError("repository identity must be fixed in the schema")

    top_level = required_keys(schema, "schema")
    defs = schema.get("$defs")
    if not isinstance(defs, dict):
        raise ValidationError("schema.$defs must be an object")
    for name in ("gitSha", "date", "nullableReference", "localeStatusMap", "artifact"):
        if name not in defs:
            raise ValidationError(f"schema definition is missing: {name}")

    if defs["gitSha"].get("pattern") != "^[0-9a-f]{40}$":
        raise ValidationError("gitSha must require a lowercase 40-character Git SHA")
    artifact_required = required_keys(defs["artifact"], "schema.$defs.artifact")
    sha256 = defs["artifact"]["properties"].get("sha256", {})
    variants = sha256.get("oneOf")
    if not isinstance(variants, list) or not any(
        item.get("pattern") == "^[0-9a-f]{64}$"
        for item in variants
        if isinstance(item, dict)
    ):
        raise ValidationError("artifact sha256 must enforce a lowercase 64-character digest")

    for collection in ("languages", "artifacts"):
        definition = schema["properties"].get(collection, {})
        if definition.get("type") != "array" or definition.get("minItems", 0) < 1:
            raise ValidationError(f"{collection} must be a non-empty array")

    return top_level, artifact_required


def validate_template(
    text: str,
    schema: dict,
    top_required: set[str],
    artifact_required: set[str],
) -> None:
    if "\t" in text:
        raise ValidationError("YAML template must not contain tab indentation")
    if re.search(r"(^|\s)(?:&|\*|!!)[A-Za-z0-9_-]+", text):
        raise ValidationError("YAML anchors, aliases, and explicit tags are forbidden")
    if re.search(r"^\s*<<:", text, re.MULTILINE):
        raise ValidationError("YAML merge keys are forbidden")

    top_keys = mapping_keys(text, 0, "top-level template")
    if top_keys != top_required:
        raise ValidationError(
            "template top-level keys do not exactly match schema.required: "
            f"missing={sorted(top_required - top_keys)}, extra={sorted(top_keys - top_required)}"
        )

    for name in ("human_approval", "qa", "github_release", "zenodo"):
        block = re.search(
            rf"^{re.escape(name)}:\s*$\n(?P<body>(?:^  .*(?:\n|$))*)",
            text,
            re.MULTILINE,
        )
        if block is None:
            raise ValidationError(f"template block is missing: {name}")
        actual = mapping_keys(block.group("body"), 2, f"{name} template block")
        expected = object_required(schema, name)
        if actual != expected:
            raise ValidationError(
                f"{name} template keys differ from schema: "
                f"missing={sorted(expected - actual)}, extra={sorted(actual - expected)}"
            )

    actual_artifact = artifact_keys(text)
    if actual_artifact != artifact_required:
        raise ValidationError(
            "artifact template keys differ from schema: "
            f"missing={sorted(artifact_required - actual_artifact)}, "
            f"extra={sorted(actual_artifact - artifact_required)}"
        )

    required_literals = {
        'schema_version: "1.0"',
        'repository: "Chpmunk31456/GRC-Practical-Manuals"',
        'release_commit_sha: "replace-with-40-character-git-sha"',
        'source_verification_date: "YYYY-MM-DD"',
        'status: "pending"',
    }
    missing_literals = sorted(item for item in required_literals if item not in text)
    if missing_literals:
        raise ValidationError(
            "template lost required fail-closed placeholders: " + ", ".join(missing_literals)
        )


def main() -> int:
    try:
        schema = load_schema()
        top_required, artifact_required = validate_schema(schema)
        try:
            template = TEMPLATE_PATH.read_text(encoding="utf-8")
        except FileNotFoundError as exc:
            raise ValidationError("release-manifest YAML template is missing") from exc
        validate_template(template, schema, top_required, artifact_required)
    except ValidationError as exc:
        print(f"[FAIL] release manifest controls: {exc}")
        return 1

    print("[PASS] release manifest controls")
    print(f"  schema: {SCHEMA_PATH.relative_to(REPO_ROOT)}")
    print(f"  template: {TEMPLATE_PATH.relative_to(REPO_ROOT)}")
    print(f"  required top-level fields: {len(top_required)}")
    print(f"  required artifact fields: {len(artifact_required)}")
    print("  template remains intentionally pending and is not release approval")
    return 0


if __name__ == "__main__":
    sys.exit(main())
