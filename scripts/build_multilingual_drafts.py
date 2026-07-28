#!/usr/bin/env python3
"""Create Spanish and Brazilian Portuguese Markdown drafts from extracted English GRC sources.

The script uses locally installed Argos Translate models. It preserves fenced code blocks,
URLs, inline code, Markdown link targets, and common framework/control identifiers. Generated
files are explicitly labeled as machine-assisted drafts pending human language review.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import argostranslate.translate

ROOT = Path(__file__).resolve().parents[1]

LANGUAGES = {
    "es": {
        "folder": "Espanol",
        "label": "Español (América Latina)",
        "notice": (
            "> **Estado de revisión:** Borrador de traducción asistida por máquina. Requiere revisión humana de "
            "terminología, significado, enlaces, formato y vigencia técnica antes de marcarse como edición final."
        ),
        "suffix": "Espanol_v1.0",
    },
    "pt": {
        "folder": "Portugues_BR",
        "label": "Português do Brasil",
        "notice": (
            "> **Status da revisão:** Rascunho de tradução assistida por máquina. Requer revisão humana de "
            "terminologia, significado, links, formatação e atualidade técnica antes de ser marcado como edição final."
        ),
        "suffix": "Portugues_BR_v1.0",
    },
}

PROTECTED_PATTERNS = [
    re.compile(r"https?://[^\s)>]+"),
    re.compile(r"`[^`]+`"),
    re.compile(r"\]\([^)]+\)"),
    re.compile(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}(?:-\d+)?\b"),
    re.compile(r"\b(?:NIST|CSF|RMF|CIS|ISO|IEC|SOC|GDPR|HIPAA|PCI DSS|OWASP|API|RACI|GRC)\b"),
]

DEFAULT_MAX_CHARS = 800
CHECKPOINT_VERSION = 1
GENERATOR_ID = "scripts/build_multilingual_drafts.py"


def log(message: str) -> None:
    print(message, flush=True)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def checkpoint_path(destination: Path) -> Path:
    return destination.with_suffix(destination.suffix + ".translation-checkpoint.json")


def generation_settings(*, max_chars: int, line_limit: int | None) -> dict[str, object]:
    return {
        "source_language": "en",
        "translation_engine": "argos",
        "max_chars": max_chars,
        "line_limit": line_limit,
    }


def expected_checkpoint(
    *,
    source_text: str,
    output_text: str,
    target: str,
    max_chars: int,
    line_limit: int | None,
) -> dict[str, object]:
    return {
        "generator": GENERATOR_ID,
        "checkpoint_version": CHECKPOINT_VERSION,
        "source_sha256": sha256_text(source_text),
        "output_sha256": sha256_text(output_text),
        "target_language": target,
        "settings": generation_settings(max_chars=max_chars, line_limit=line_limit),
    }


def read_checkpoint(path: Path) -> dict[str, object] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def trusted_generated_checkpoint(checkpoint: dict[str, object] | None) -> bool:
    return bool(
        checkpoint
        and checkpoint.get("generator") == GENERATOR_ID
        and checkpoint.get("checkpoint_version") == CHECKPOINT_VERSION
        and isinstance(checkpoint.get("output_sha256"), str)
    )


def atomic_write(path: Path, text: str) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def protect(text: str) -> tuple[str, dict[str, str]]:
    mapping: dict[str, str] = {}
    counter = 0
    for pattern in PROTECTED_PATTERNS:
        while True:
            match = pattern.search(text)
            if not match:
                break
            token = f"ZXPROTECTED{counter}XZ"
            mapping[token] = match.group(0)
            text = text[: match.start()] + token + text[match.end() :]
            counter += 1
    return text, mapping


def restore(text: str, mapping: dict[str, str]) -> str:
    # Reverse insertion order so nested protections (for example, a URL inside
    # a Markdown link destination) are fully restored.
    for token, value in reversed(mapping.items()):
        text = text.replace(token, value)
    return text


def bounded_chunks(text: str, max_chars: int) -> list[str]:
    """Split prose at whitespace where possible while preserving exact separators."""
    if max_chars < 100:
        raise ValueError("--max-chars must be at least 100")
    if len(text) <= max_chars:
        return [text]

    chunks: list[str] = []
    remaining = text
    while len(remaining) > max_chars:
        split_at = remaining.rfind(" ", 0, max_chars + 1)
        if split_at <= 0:
            split_at = remaining.rfind("\t", 0, max_chars + 1)
        if split_at <= 0:
            split_at = max_chars
        else:
            split_at += 1
        chunks.append(remaining[:split_at])
        remaining = remaining[split_at:]
    if remaining:
        chunks.append(remaining)
    return chunks


def translate_markdown(
    source: str,
    target: str,
    notice: str,
    *,
    source_name: str,
    max_chars: int,
) -> str:
    lines = source.splitlines()
    output: list[str] = [notice, ""]
    in_fence = False

    for line_number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith(("```", "~~~")):
            in_fence = not in_fence
            output.append(line)
            continue
        if in_fence or not stripped:
            output.append(line)
            continue

        protected, mapping = protect(line)
        chunks = bounded_chunks(protected, max_chars)
        chunk_count = len(chunks)
        translated_chunks: list[str] = []
        for chunk_number, chunk in enumerate(chunks, start=1):
            log(
                f"[translate] source={source_name} target={target} "
                f"line={line_number}/{len(lines)} chunk={chunk_number}/{chunk_count}"
            )
            try:
                translated = argostranslate.translate.translate(chunk, "en", target)
            except Exception as exc:
                raise RuntimeError(
                    f"Translation failed: source={source_name} target={target} "
                    f"line={line_number} chunk={chunk_number}/{chunk_count}: {exc}"
                ) from exc
            translated_chunks.append(restore(translated, mapping))
        output.append("".join(translated_chunks))

    return "\n".join(output).rstrip() + "\n"


def output_name(source: Path, suffix: str) -> str:
    stem = source.stem
    stem = re.sub(r"^English_Source_", "", stem)
    stem = re.sub(r"_v1\.0$", "", stem)
    return f"{stem}_{suffix}.md"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--refresh-generated",
        action="store_true",
        help="Refresh only stale, unmodified outputs with trusted workflow checkpoints.",
    )
    parser.add_argument(
        "--allow-unresolved-existing",
        action="store_true",
        help="Return success after clearly reporting protected or stale existing outputs.",
    )
    parser.add_argument("--target", choices=sorted(LANGUAGES), action="append", help="Limit target language.")
    parser.add_argument("--source", action="append", help="Limit sources by repository-relative path or filename.")
    parser.add_argument("--source-limit", type=int, help="Process at most this many matched source files.")
    parser.add_argument("--line-limit", type=int, help="Translate at most this many source lines (smoke tests only).")
    parser.add_argument("--max-chars", type=int, default=DEFAULT_MAX_CHARS, help="Maximum translation chunk size.")
    parser.add_argument(
        "--destination-root",
        type=Path,
        help="Write outputs below this directory instead of beside sources (for smoke tests).",
    )
    return parser.parse_args(argv)


def source_matches(source: Path, filters: list[str] | None) -> bool:
    if not filters:
        return True
    relative = source.relative_to(ROOT).as_posix()
    return any(item == source.name or item == relative for item in filters)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.line_limit is not None and args.line_limit < 1:
        raise SystemExit("--line-limit must be at least 1")
    sources = sorted(ROOT.glob("[0-9][0-9]-*/**/English_Source_*.md"))
    sources = [source for source in sources if source_matches(source, args.source)]
    if args.source_limit is not None:
        if args.source_limit < 1:
            raise SystemExit("--source-limit must be at least 1")
        sources = sources[: args.source_limit]
    if not sources:
        raise SystemExit("No extracted English source Markdown files found.")

    targets = args.target or list(LANGUAGES)
    generated = 0
    skipped = 0
    protected = 0
    stale = 0
    for source in sources:
        complete_source = source.read_text(encoding="utf-8-sig", errors="strict")
        original = complete_source
        if args.line_limit is not None:
            original = "\n".join(original.splitlines()[: args.line_limit]) + "\n"
        relative_source = source.relative_to(ROOT)
        for target in targets:
            cfg = LANGUAGES[target]
            if args.destination_root:
                folder = args.destination_root / relative_source.parent / cfg["folder"]
            else:
                folder = source.parent / cfg["folder"]
            folder.mkdir(parents=True, exist_ok=True)
            destination = folder / output_name(source, cfg["suffix"])
            display_destination = (
                str(destination.relative_to(ROOT))
                if destination.is_relative_to(ROOT)
                else str(destination)
            )
            metadata_path = checkpoint_path(destination)
            if destination.is_file():
                existing = destination.read_text(encoding="utf-8")
                checkpoint = read_checkpoint(metadata_path)
                if not trusted_generated_checkpoint(checkpoint):
                    log(
                        f"[protected] output={display_destination} reason=no-trusted-checkpoint "
                        "classification=manual-or-legacy action=leave-unchanged"
                    )
                    protected += 1
                    continue
                if checkpoint["output_sha256"] != sha256_text(existing):
                    log(
                        f"[protected] output={display_destination} reason=output-modified-after-generation "
                        "classification=manual-or-reviewed action=leave-unchanged"
                    )
                    protected += 1
                    continue

                current = expected_checkpoint(
                    source_text=complete_source,
                    output_text=existing,
                    target=target,
                    max_chars=args.max_chars,
                    line_limit=args.line_limit,
                )
                comparable_keys = (
                    "generator",
                    "checkpoint_version",
                    "source_sha256",
                    "target_language",
                    "settings",
                )
                if all(checkpoint.get(key) == current[key] for key in comparable_keys):
                    log(f"[skip] valid checkpoint: {display_destination}")
                    skipped += 1
                    continue
                if not args.refresh_generated:
                    log(
                        f"[stale] output={display_destination} reason=source-or-settings-changed "
                        "action=rerun-with---refresh-generated"
                    )
                    stale += 1
                    continue
                log(f"[refresh] trusted stale generated output: {display_destination}")

            log(f"[start] source={relative_source} target={target} output={display_destination}")
            translated = translate_markdown(
                original,
                target,
                cfg["notice"],
                source_name=relative_source.as_posix(),
                max_chars=args.max_chars,
            )
            metadata = expected_checkpoint(
                source_text=complete_source,
                output_text=translated,
                target=target,
                max_chars=args.max_chars,
                line_limit=args.line_limit,
            )
            atomic_write(destination, translated)
            atomic_write(metadata_path, json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
            log(f"[complete] output={display_destination} chars={len(translated)}")
            generated += 1
    unresolved = protected + stale
    log(
        f"[summary] generated={generated} skipped={skipped} protected={protected} stale={stale} "
        f"sources={len(sources)} targets={len(targets)}"
    )
    if unresolved and not args.allow_unresolved_existing:
        log(
            "[action-required] Existing outputs were left unchanged. Review the classifications; "
            "use --refresh-generated only for trusted stale generated files, or "
            "--allow-unresolved-existing to acknowledge protected legacy/manual outputs."
        )
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
