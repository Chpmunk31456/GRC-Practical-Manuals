#!/usr/bin/env python3
"""Combine writing/publication QA outputs and enforce the versioned quality baseline."""
from __future__ import annotations
import argparse,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def summarize(paths:list[Path])->dict:
    m=Counter();codes=Counter()
    for path in paths:
        d=json.loads(path.read_text(encoding="utf-8"));m["reports"]+=1
        kind=d.get("kind") or ("publication" if "results" in d and any("manual_id" in x for x in d.get("results",[])) else "writing")
        status=d.get("status")
        if status=="FAIL":m["failed_reports"]+=1
        if kind=="publication" and status=="FAIL":m["publication_failures"]+=1
        if "roundtrip" in path.name and status=="FAIL":m["roundtrip_failures"]+=1
        if "layout" in path.name and status=="FAIL":m["layout_failures"]+=1
        if "accessibility" in path.name and status=="FAIL":m["accessibility_failures"]+=1
        for r in d.get("results",[]):
            if isinstance(r,dict):
                if r.get("status")=="FAIL":m["component_failures"]+=1
                for f in r.get("findings",[]):codes[f.get("code","unknown")]+=1
                for lr in r.get("results",{}).values() if isinstance(r.get("results"),dict) else []:
                    for f in lr.get("findings",[]):codes[f.get("code","unknown")]+=1
        if d.get("semantic_qa",{}).get("status")=="FAIL":m["semantic_failures"]+=1
        for f in d.get("findings",[]):codes[f.get("code","unknown")]+=1
    return {"schema_version":1,"metrics":dict(m),"finding_codes":dict(codes.most_common())}

def check(summary:dict,policy:dict)->list[str]:
    failures=[]
    metrics=summary["metrics"]
    for key,limit in policy.get("thresholds",{}).items():
        value=int(metrics.get(key,0))
        if value>int(limit):failures.append(f"{key}={value} exceeds baseline limit {limit}")
    return failures

def main()->int:
    p=argparse.ArgumentParser();p.add_argument("reports",nargs="+")
    p.add_argument("--policy",default="config/writing_observability_policy.json");p.add_argument("--output");a=p.parse_args()
    s=summarize([Path(x) for x in a.reports]);policy=json.loads((ROOT/a.policy).read_text(encoding="utf-8"))
    failures=check(s,policy);s["status"]="FAIL" if failures else "PASS";s["baseline_failures"]=failures
    out=json.dumps(s,indent=2,ensure_ascii=False)+"\n"
    if a.output:Path(a.output).write_text(out,encoding="utf-8")
    print(out,end="");return 0 if s["status"]=="PASS" else 1
if __name__=="__main__":raise SystemExit(main())
