#!/usr/bin/env python3
"""Deterministic semantic-preservation checks for controlled writing.

The verifier is intentionally conservative and non-generative. It detects
changes to numbers, identifiers, modal strength, and configured critical
concepts. It never rewrites content and does not claim full semantic equivalence.
"""
from __future__ import annotations
import argparse, json, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from document_writing_qa import extract_blocks  # noqa: E402

DEFAULT_POLICY = ROOT / "config" / "writing_semantic_policy.json"

NUMBER_RE = re.compile(r"(?<![A-Za-z])[-+]?\d+(?:[.,]\d+)*(?:%|x|X)?")
URL_RE = re.compile(r"https?://\S+")


def load_policy(path: Path = DEFAULT_POLICY) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def text_of(path: Path) -> str:
    return "\n".join(block["text"] for block in extract_blocks(path))


def tokens(pattern: re.Pattern, text: str) -> Counter:
    return Counter(match.group(0) for match in pattern.finditer(text))


def identifier_tokens(text: str, policy: dict) -> Counter:
    values: list[str] = []
    for raw in policy.get("identifier_patterns", []):
        values.extend(match.group(0) for match in re.finditer(raw, text, re.IGNORECASE))
    return Counter(values)


def concept_presence(text: str, locale: str, policy: dict) -> set[str]:
    lowered = text.casefold()
    present: set[str] = set()
    for concept, locales in policy.get("critical_concepts", {}).items():
        for phrase in locales.get(locale, []):
            if phrase.casefold() in lowered:
                present.add(concept)
                break
    return present


def modal_counts(text: str, policy: dict) -> dict[str, int]:
    lowered = text.casefold()
    result = {}
    for group, words in policy.get("modal_groups", {}).items():
        total = 0
        for word in words:
            total += len(re.findall(r"(?<!\w)" + re.escape(word.casefold()) + r"(?!\w)", lowered))
        result[group] = total
    return result


def compare(source: Path, target: Path, policy: dict, source_locale: str, target_locale: str) -> dict:
    s = text_of(source)
    t = text_of(target)
    findings: list[dict] = []

    s_nums, t_nums = tokens(NUMBER_RE, s), tokens(NUMBER_RE, t)
    removed_nums = list((s_nums - t_nums).elements())
    introduced_nums = list((t_nums - s_nums).elements())
    if removed_nums:
        findings.append({"severity":"error","code":"removed_numbers","values":removed_nums})
    if introduced_nums:
        findings.append({"severity":"error","code":"introduced_numbers","values":introduced_nums})

    s_ids, t_ids = identifier_tokens(s, policy), identifier_tokens(t, policy)
    removed_ids = list((s_ids - t_ids).elements())
    introduced_ids = list((t_ids - s_ids).elements())
    if removed_ids:
        findings.append({"severity":"error","code":"removed_identifiers","values":removed_ids})
    if introduced_ids:
        findings.append({"severity":"error","code":"introduced_identifiers","values":introduced_ids})

    s_concepts = concept_presence(s, source_locale, policy)
    t_concepts = concept_presence(t, target_locale, policy)
    missing = sorted(s_concepts - t_concepts)
    if missing:
        findings.append({"severity":"error","code":"missing_critical_concepts","values":missing})

    if source_locale == target_locale:
        sm, tm = modal_counts(s, policy), modal_counts(t, policy)
        if sm != tm:
            findings.append({"severity":"error","code":"modal_strength_change","source":sm,"target":tm})

    s_urls, t_urls = tokens(URL_RE, s), tokens(URL_RE, t)
    if s_urls != t_urls:
        findings.append({
            "severity":"warning","code":"url_drift",
            "removed":list((s_urls-t_urls).elements()),
            "introduced":list((t_urls-s_urls).elements())
        })

    return {
        "schema_version":1,
        "source":source.relative_to(ROOT).as_posix() if source.is_relative_to(ROOT) else str(source),
        "target":target.relative_to(ROOT).as_posix() if target.is_relative_to(ROOT) else str(target),
        "source_locale":source_locale,
        "target_locale":target_locale,
        "status":"PASS" if not any(x["severity"]=="error" for x in findings) else "FAIL",
        "findings":findings,
    }


def main() -> int:
    p=argparse.ArgumentParser()
    p.add_argument("source")
    p.add_argument("target")
    p.add_argument("--source-locale", default="en")
    p.add_argument("--target-locale", default="en")
    p.add_argument("--policy", default=str(DEFAULT_POLICY))
    p.add_argument("--output")
    args=p.parse_args()
    source=Path(args.source); target=Path(args.target)
    if not source.is_absolute(): source=ROOT/source
    if not target.is_absolute(): target=ROOT/target
    result=compare(source,target,load_policy(Path(args.policy)),args.source_locale,args.target_locale)
    rendered=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if args.output: Path(args.output).write_text(rendered,encoding="utf-8")
    print(rendered,end="")
    return 0 if result["status"]=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
