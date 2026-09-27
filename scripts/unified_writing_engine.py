#!/usr/bin/env python3
"""Unified context-aware writing QA engine.

Combines context selection, approved-feedback validation, grammar/style QA and
optional semantic-preservation checks into one non-destructive report.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from document_writing_qa import analyze_file, load_policy as load_writing_policy  # noqa: E402
from semantic_writing_qa import compare as semantic_compare, load_policy as load_semantic_policy  # noqa: E402

CONTEXTS=ROOT/"config"/"writing_context_profiles.json"
FEEDBACK=ROOT/"config"/"approved_writing_feedback.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_feedback(data: dict) -> list[str]:
    errors=[]
    for bucket in ("approved_rules","approved_examples"):
        for idx,item in enumerate(data.get(bucket,[])):
            if item.get("approved") is not True:
                errors.append(f"{bucket}[{idx}] is not explicitly approved")
            if not item.get("provenance"):
                errors.append(f"{bucket}[{idx}] lacks provenance")
    return errors


def main() -> int:
    p=argparse.ArgumentParser()
    p.add_argument("file")
    p.add_argument("--context")
    p.add_argument("--semantic-source")
    p.add_argument("--source-locale",default="en")
    p.add_argument("--target-locale",default="en")
    p.add_argument("--languagetool-url")
    p.add_argument("--require-languagetool",action="store_true")
    p.add_argument("--output")
    args=p.parse_args()

    contexts=load_json(CONTEXTS)
    context_name=args.context or contexts["default_context"]
    if context_name not in contexts["profiles"]:
        print(f"Unknown writing context: {context_name}",file=sys.stderr); return 2

    feedback=load_json(FEEDBACK)
    feedback_errors=validate_feedback(feedback)
    if feedback_errors:
        print("\n".join(feedback_errors),file=sys.stderr); return 2

    path=Path(args.file)
    if not path.is_absolute(): path=ROOT/path
    writing_policy=load_writing_policy()
    result=analyze_file(
        path,writing_policy,
        endpoint=args.languagetool_url or (writing_policy["privacy"]["default_endpoint"] if args.require_languagetool else None),
        require_languagetool=args.require_languagetool,
    )

    combined={
        "schema_version":1,
        "context":context_name,
        "context_profile":contexts["profiles"][context_name],
        "approved_feedback":{"rules":len(feedback.get("approved_rules",[])),"examples":len(feedback.get("approved_examples",[]))},
        "writing_qa":result,
        "semantic_qa":None,
    }

    status="FAIL" if result["counts"]["errors"] else "PASS"
    if args.semantic_source:
        src=Path(args.semantic_source)
        if not src.is_absolute(): src=ROOT/src
        sem=semantic_compare(src,path,load_semantic_policy(),args.source_locale,args.target_locale)
        combined["semantic_qa"]=sem
        if sem["status"]=="FAIL": status="FAIL"
    combined["status"]=status

    rendered=json.dumps(combined,ensure_ascii=False,indent=2)+"\n"
    if args.output: Path(args.output).write_text(rendered,encoding="utf-8")
    print(rendered,end="")
    return 0 if status=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
