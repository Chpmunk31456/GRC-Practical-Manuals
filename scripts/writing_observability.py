#!/usr/bin/env python3
"""Aggregate writing QA reports into machine-readable quality telemetry."""
from __future__ import annotations
import argparse, json
from collections import Counter
from pathlib import Path


def summarize(paths: list[Path]) -> dict:
    counters=Counter()
    codes=Counter()
    contexts=Counter()
    for path in paths:
        data=json.loads(path.read_text(encoding="utf-8"))
        counters["reports"]+=1
        if data.get("status")=="FAIL": counters["failed_reports"]+=1
        if data.get("context"): contexts[data["context"]]+=1
        w=data.get("writing_qa",data)
        counts=w.get("counts",{})
        counters["grammar_errors"]+=int(counts.get("errors",0))
        counters["warnings"]+=int(counts.get("warnings",0))
        for f in w.get("findings",[]):
            codes[f.get("code","unknown")]+=1
        sem=data.get("semantic_qa")
        if sem:
            counters["semantic_checks"]+=1
            if sem.get("status")=="FAIL": counters["semantic_failures"]+=1
            for f in sem.get("findings",[]):
                codes["semantic:"+f.get("code","unknown")]+=1
    return {
        "schema_version":1,
        "metrics":dict(counters),
        "finding_codes":dict(codes.most_common()),
        "contexts":dict(contexts),
    }


def main()->int:
    p=argparse.ArgumentParser()
    p.add_argument("reports",nargs="+")
    p.add_argument("--output")
    args=p.parse_args()
    result=summarize([Path(x) for x in args.reports])
    out=json.dumps(result,indent=2,ensure_ascii=False)+"\n"
    if args.output: Path(args.output).write_text(out,encoding="utf-8")
    print(out,end="")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
