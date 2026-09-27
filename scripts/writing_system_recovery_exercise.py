#!/usr/bin/env python3
"""Executable recovery exercise for the controlled writing/publication system."""
from __future__ import annotations
import argparse,json,py_compile,shutil,subprocess,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

REQUIRED=[
 "config/writing_system_manifest.json",
 "config/controlled_publications/index.json",
 "config/controlled_publication_manifest.schema.json",
 "scripts/controlled_publication_qa.py",
 "scripts/publication_roundtrip_qa.py",
 "scripts/publication_layout_qa.py",
 "scripts/publication_accessibility_qa.py",
 "scripts/semantic_writing_qa.py"
]

def run(require_pdf_tools:bool=False)->dict:
    errors=[];evidence={}
    for rel in REQUIRED:
        if not (ROOT/rel).is_file():errors.append(f"missing recovery component: {rel}")
    manifest=json.loads((ROOT/"config/writing_system_manifest.json").read_text(encoding="utf-8"))
    for rel in manifest.get("json_configs",[]):
        try:json.loads((ROOT/rel).read_text(encoding="utf-8"))
        except Exception as e:errors.append(f"invalid JSON {rel}: {e}")
    for rel in manifest.get("python_modules",[]):
        try:py_compile.compile(str(ROOT/rel),doraise=True)
        except Exception as e:errors.append(f"compile failure {rel}: {e}")
    tools={x:bool(shutil.which(x)) for x in ("git","pdftotext","pdfinfo")}
    evidence["tools"]=tools
    if require_pdf_tools and not all(tools.values()):errors.append("required recovery tools are unavailable")
    with tempfile.TemporaryDirectory() as td:
        target=Path(td)/"recovery"
        target.mkdir()
        for rel in REQUIRED:
            src=ROOT/rel
            if src.is_file():
                dst=target/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
        evidence["copied_components"]=sum(1 for p in target.rglob("*") if p.is_file())
    return {"schema_version":1,"status":"FAIL" if errors else "PASS","errors":errors,"evidence":evidence}

def main()->int:
    p=argparse.ArgumentParser();p.add_argument("--require-pdf-tools",action="store_true");p.add_argument("--output");a=p.parse_args()
    r=run(a.require_pdf_tools);out=json.dumps(r,indent=2)+"\n"
    if a.output:Path(a.output).write_text(out,encoding="utf-8")
    print(out,end="");return 0 if r["status"]=="PASS" else 1
if __name__=="__main__":raise SystemExit(main())
