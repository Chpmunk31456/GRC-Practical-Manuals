#!/usr/bin/env python3
"""Structural accessibility checks for controlled DOCX/PDF publication artifacts."""
from __future__ import annotations
import json,re,zipfile,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
W="{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
A="{http://schemas.openxmlformats.org/drawingml/2006/main}"

def docx_checks(path:Path)->list[dict]:
    f=[]
    with zipfile.ZipFile(path) as z:
        names=set(z.namelist()); root=ET.fromstring(z.read("word/document.xml"))
        styles=ET.fromstring(z.read("word/styles.xml")) if "word/styles.xml" in names else None
        settings=ET.fromstring(z.read("word/settings.xml")) if "word/settings.xml" in names else None
    headings=0
    for p in root.iter(W+"p"):
        ps=p.find(W+"pPr/"+W+"pStyle")
        if ps is not None and "heading" in ps.attrib.get(W+"val","").lower(): headings+=1
    if headings==0: f.append({"severity":"error","code":"docx_no_heading_styles"})
    lang_nodes=[]
    if styles is not None: lang_nodes=list(styles.iter(W+"lang"))
    if not lang_nodes: f.append({"severity":"warning","code":"docx_language_not_declared_in_styles"})
    drawings=list(root.iter(A+"blip"))
    docprs=[e for e in root.iter() if e.tag.endswith("}docPr")]
    missing_alt=sum(1 for e in docprs if not (e.attrib.get("descr") or e.attrib.get("title")))
    if drawings and missing_alt: f.append({"severity":"error","code":"docx_missing_alt_text","count":missing_alt})
    return f

def pdf_checks(path:Path)->list[dict]:
    data=path.read_bytes()
    f=[]
    if b"/Lang" not in data: f.append({"severity":"warning","code":"pdf_language_marker_missing"})
    if b"/StructTreeRoot" not in data: f.append({"severity":"warning","code":"pdf_tag_tree_marker_missing"})
    if b"/Outlines" not in data: f.append({"severity":"warning","code":"pdf_outline_marker_missing"})
    return f

def run(manifest:dict)->dict:
    root=ROOT/manifest["manual_root"]; results={}; allf=[]
    for locale,cfg in manifest["languages"].items():
        f=docx_checks(root/cfg["artifacts"]["docx"])+pdf_checks(root/cfg["artifacts"]["pdf"])
        results[locale]={"findings":f,"status":"FAIL" if any(x["severity"]=="error" for x in f) else "PASS"}
        allf.extend(f)
    return {"schema_version":1,"manual_id":manifest["manual_id"],"status":"FAIL" if any(x["severity"]=="error" for x in allf) else "PASS","results":results}

if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser();p.add_argument("manifest");p.add_argument("--output");a=p.parse_args()
    m=json.loads(Path(a.manifest).read_text(encoding="utf-8"));r=run(m);out=json.dumps(r,indent=2)+"\n"
    if a.output: Path(a.output).write_text(out,encoding="utf-8")
    print(out,end="");raise SystemExit(0 if r["status"]=="PASS" else 1)
