#!/usr/bin/env python3
"""Source -> DOCX -> PDF round-trip preservation checks."""
from __future__ import annotations
import json,re,shutil,subprocess,sys,zipfile,xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
WORD_NS="{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
NUM_RE=re.compile(r"(?<![A-Za-z])[-+]?\d+(?:[.,]\d+)*(?:%|x|X)?")
ID_RE=re.compile(r"\b(?:NIST(?:\s+AI)?\s+[A-Z0-9.-]+(?:\s+[0-9.-]+)?|ISO(?:/IEC)?\s+[0-9-]+(?::[0-9]{4})?|CVE-[0-9]{4}-[0-9]{4,})\b",re.I)

def docx_text(path:Path)->str:
    with zipfile.ZipFile(path) as z:
        root=ET.fromstring(z.read("word/document.xml"))
    return "\n".join("".join(n.text or "" for n in p.iter(WORD_NS+"t")) for p in root.iter(WORD_NS+"p"))

def pdf_text(path:Path)->str:
    exe=shutil.which("pdftotext")
    if not exe: raise RuntimeError("pdftotext is required for round-trip validation")
    r=subprocess.run([exe,"-layout",str(path),"-"],check=True,capture_output=True,text=True,errors="replace")
    return r.stdout

def tokens(rx,text): return Counter(m.group(0) for m in rx.finditer(text))

def compare_text(source:str,docx:str,pdf:str)->dict:
    findings=[]
    for name,rx in (("numbers",NUM_RE),("identifiers",ID_RE)):
        s,d,p=tokens(rx,source),tokens(rx,docx),tokens(rx,pdf)
        missing_docx=list((s-d).elements())
        missing_pdf=list((d-p).elements())
        introduced_pdf=list((p-d).elements())
        if missing_docx: findings.append({"severity":"error","code":f"source_to_docx_{name}_loss","values":missing_docx[:50]})
        if missing_pdf: findings.append({"severity":"error","code":f"docx_to_pdf_{name}_loss","values":missing_pdf[:50]})
        if introduced_pdf: findings.append({"severity":"warning","code":f"docx_to_pdf_{name}_introduced","values":introduced_pdf[:50]})
    ratios={
      "docx_to_source": len(docx.strip())/max(1,len(source.strip())),
      "pdf_to_docx": len(pdf.strip())/max(1,len(docx.strip()))
    }
    if ratios["docx_to_source"]<0.55: findings.append({"severity":"error","code":"docx_text_loss_ratio","ratio":ratios["docx_to_source"]})
    if ratios["pdf_to_docx"]<0.55: findings.append({"severity":"error","code":"pdf_text_loss_ratio","ratio":ratios["pdf_to_docx"]})
    return {"status":"FAIL" if any(f["severity"]=="error" for f in findings) else "PASS","ratios":ratios,"findings":findings}

def run(manifest:dict)->dict:
    root=ROOT/manifest["manual_root"]; results={}; failures=[]
    for locale,cfg in manifest["languages"].items():
        sources=[]
        for pat in cfg["source_globs"]: sources.extend(sorted(root.glob(pat)))
        source="\n\n".join(p.read_text(encoding="utf-8",errors="replace") for p in sources if p.is_file())
        try:
            result=compare_text(source,docx_text(root/cfg["artifacts"]["docx"]),pdf_text(root/cfg["artifacts"]["pdf"]))
        except Exception as e:
            result={"status":"FAIL","findings":[{"severity":"error","code":"roundtrip_execution","message":str(e)}]}
        results[locale]=result
        if result["status"]=="FAIL": failures.append(locale)
    return {"schema_version":1,"manual_id":manifest["manual_id"],"status":"FAIL" if failures else "PASS","results":results}

if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser();p.add_argument("manifest");p.add_argument("--output");a=p.parse_args()
    m=json.loads(Path(a.manifest).read_text(encoding="utf-8"));r=run(m);out=json.dumps(r,indent=2,ensure_ascii=False)+"\n"
    if a.output: Path(a.output).write_text(out,encoding="utf-8")
    print(out,end="");raise SystemExit(0 if r["status"]=="PASS" else 1)
