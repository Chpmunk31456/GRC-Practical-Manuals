#!/usr/bin/env python3
"""Rendered-publication regression checks using retained page QA and PDF metadata."""
from __future__ import annotations
import csv,json,shutil,subprocess
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def pdf_pages(path:Path)->int|None:
    exe=shutil.which("pdfinfo")
    if not exe: return None
    r=subprocess.run([exe,str(path)],check=True,capture_output=True,text=True,errors="replace")
    for line in r.stdout.splitlines():
        if line.startswith("Pages:"): return int(line.split(":",1)[1].strip())
    return None

def run(manifest:dict)->dict:
    root=ROOT/manifest["manual_root"]; report=json.loads((root/manifest["publication_report"]).read_text(encoding="utf-8"))
    rows=list(csv.DictReader((root/manifest["page_qa"]).open(encoding="utf-8")))
    findings=[]; by_pdf=defaultdict(list)
    for row in rows: by_pdf[row["pdf"]].append(row)
    for locale,cfg in manifest["languages"].items():
        pdf=root/cfg["artifacts"]["pdf"]; name=pdf.name
        expected=int(report["editions"][locale]["artifacts"]["pdf"]["pages"])
        page_rows=by_pdf.get(name,[])
        if len(page_rows)!=expected: findings.append({"severity":"error","code":"page_qa_count_mismatch","pdf":name,"expected":expected,"actual":len(page_rows)})
        if any((r.get("automated_status") or "").upper()!="PASS" for r in page_rows):
            findings.append({"severity":"error","code":"page_qa_nonpass","pdf":name})
        blank=[int(r["page"]) for r in page_rows if int(r.get("text_chars") or 0)<30]
        if blank: findings.append({"severity":"error","code":"blank_or_near_blank_pages","pdf":name,"pages":blank})
        dims={(r.get("width_pt"),r.get("height_pt")) for r in page_rows}
        if len(dims)>1: findings.append({"severity":"warning","code":"mixed_page_dimensions","pdf":name,"dimensions":sorted(dims)})
        actual=pdf_pages(pdf)
        if actual is not None and actual!=expected: findings.append({"severity":"error","code":"pdfinfo_page_count_mismatch","pdf":name,"expected":expected,"actual":actual})
    return {"schema_version":1,"manual_id":manifest["manual_id"],"status":"FAIL" if any(f["severity"]=="error" for f in findings) else "PASS","findings":findings}

if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser();p.add_argument("manifest");p.add_argument("--output");a=p.parse_args()
    m=json.loads(Path(a.manifest).read_text(encoding="utf-8"));r=run(m);out=json.dumps(r,indent=2)+"\n"
    if a.output: Path(a.output).write_text(out,encoding="utf-8")
    print(out,end="");raise SystemExit(0 if r["status"]=="PASS" else 1)
