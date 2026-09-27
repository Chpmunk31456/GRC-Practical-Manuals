#!/usr/bin/env python3
"""Reusable fail-closed controlled publication QA engine."""
from __future__ import annotations
import argparse,csv,hashlib,json,re,subprocess,sys,zipfile,xml.etree.ElementTree as ET
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
WORD="{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

def sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for c in iter(lambda:f.read(1024*1024),b""): h.update(c)
    return h.hexdigest()

def collect(root:Path,globs:list[str])->list[Path]:
    out=set()
    for g in globs: out.update(p for p in root.glob(g) if p.is_file())
    return sorted(out)

def chapter_numbers(text:str,pattern:str)->list[int]:
    return sorted({int(x) for x in re.findall(pattern,text,re.I|re.M)})

def docx_ok(path:Path)->tuple[bool,str]:
    try:
        with zipfile.ZipFile(path) as z:
            if "word/document.xml" not in z.namelist(): return False,"missing word/document.xml"
            root=ET.fromstring(z.read("word/document.xml"))
            if not any(True for _ in root.iter(WORD+"p")): return False,"no paragraphs"
    except Exception as e: return False,str(e)
    return True,"valid"

def pdf_ok(path:Path)->tuple[bool,str]:
    try:
        b=path.read_bytes()
    except OSError as e:return False,str(e)
    if not b.startswith(b"%PDF-"):return False,"missing PDF signature"
    if len(b)<1024:return False,"implausibly small"
    return True,"valid"

def checksum_manifest(path:Path,publication:Path)->dict[str,str]:
    out={}
    if not path.is_file():return out
    for line in path.read_text(encoding="utf-8",errors="replace").splitlines():
        m=re.match(r"^([0-9a-fA-F]{64})\s+[* ]?(.+)$",line.strip())
        if m: out[(publication/Path(m.group(2)).name).resolve().as_posix()]=m.group(1).lower()
    return out

def report_hashes(report:dict,publication:Path)->dict[str,str]:
    out={}
    for ed in report.get("editions",{}).values():
        for kind in ("docx","pdf"):
            a=ed.get("artifacts",{}).get(kind,{})
            if a.get("file") and a.get("sha256"): out[(publication/a["file"]).resolve().as_posix()]=a["sha256"].lower()
    return out

def git_time(path:Path)->int|None:
    rel=path.relative_to(ROOT).as_posix()
    r=subprocess.run(["git","log","-1","--format=%ct","--",rel],cwd=ROOT,capture_output=True,text=True)
    v=r.stdout.strip()
    return int(v) if v.isdigit() else None

def validate_manifest_shape(m:dict)->list[str]:
    errors=[]
    for key in ("manual_id","manual_root","expected_chapters","languages","publication_report","checksum_manifest","page_qa","release_controls"):
        if key not in m: errors.append(f"manifest missing {key}")
    if m.get("schema_version")!=1: errors.append("unsupported manifest schema_version")
    return errors

def run_manifest(path:Path)->dict:
    m=json.loads(path.read_text(encoding="utf-8"));fail=validate_manifest_shape(m);warn=[];evidence={"languages":{},"artifacts":{}}
    if fail:return {"schema_version":1,"manifest":path.as_posix(),"manual_id":m.get("manual_id"),"status":"FAIL","failures":fail,"warnings":warn,"evidence":evidence}
    root=ROOT/m["manual_root"];pub=root/"publication";expected=list(range(1,int(m["expected_chapters"])+1))
    report_path=root/m["publication_report"]
    report=json.loads(report_path.read_text(encoding="utf-8")) if report_path.is_file() else {}
    if not report: fail.append("publication report missing or empty")
    rh=report_hashes(report,pub); cm=checksum_manifest(root/m["checksum_manifest"],pub)
    if not cm:fail.append("checksum manifest missing or empty")
    for rec in m.get("review_records",[]):
        p=root/rec["path"]
        if not p.is_file(): fail.append(f"missing review record: {rec['path']}");continue
        txt=p.read_text(encoding="utf-8",errors="replace").casefold()
        for marker in rec.get("required_markers",[]):
            if marker.casefold() not in txt: fail.append(f"review marker missing in {rec['path']}: {marker}")
    for locale,cfg in m["languages"].items():
        sources=collect(root,cfg["source_globs"]);txt="\n\n".join(p.read_text(encoding="utf-8",errors="replace") for p in sources)
        nums=chapter_numbers(txt,cfg["chapter_heading_pattern"])
        if nums!=expected:fail.append(f"{locale}: chapter inventory mismatch")
        missing=[x for x in cfg.get("required_terms",[]) if x.casefold() not in txt.casefold()]
        if missing:fail.append(f"{locale}: missing required terms: {', '.join(missing)}")
        evidence["languages"][locale]={"sources":[p.relative_to(ROOT).as_posix() for p in sources],"chapter_count":len(nums)}
        arts=cfg["artifacts"]; evidence["artifacts"][locale]=[]
        art_paths=[]
        for kind in ("docx","pdf"):
            p=root/arts[kind];art_paths.append(p)
            rec={"kind":kind,"path":p.relative_to(ROOT).as_posix()}
            if not p.is_file():fail.append(f"{locale}: missing {kind} artifact");evidence["artifacts"][locale].append(rec);continue
            digest=sha256(p);rec["sha256"]=digest
            if m["release_controls"].get("require_report_hash_match") and rh.get(p.resolve().as_posix())!=digest:fail.append(f"{locale}: publication-report hash mismatch for {p.name}")
            if m["release_controls"].get("require_checksum_match") and cm.get(p.resolve().as_posix())!=digest:fail.append(f"{locale}: checksum mismatch for {p.name}")
            ok,detail=docx_ok(p) if kind=="docx" else pdf_ok(p)
            if not ok:fail.append(f"{locale}: invalid {kind}: {detail}")
            evidence["artifacts"][locale].append(rec)
        if m["release_controls"].get("require_stale_artifact_check") and sources and all(p.is_file() for p in art_paths):
            st=[git_time(p) for p in sources]; at=[git_time(p) for p in art_paths]
            st=[x for x in st if x is not None];at=[x for x in at if x is not None]
            if st and at and max(st)>min(at):fail.append(f"{locale}: controlled source is newer than publication artifact")
    page=root/m["page_qa"]
    if m["release_controls"].get("require_page_qa_pass"):
        if not page.is_file():fail.append("page QA record missing")
        else:
            rows=list(csv.DictReader(page.open(encoding="utf-8")))
            bad=[r for r in rows if (r.get("automated_status") or "").upper()!="PASS"]
            if bad:fail.append(f"page QA contains {len(bad)} non-PASS row(s)")
    return {"schema_version":1,"manifest":path.relative_to(ROOT).as_posix(),"manual_id":m["manual_id"],"status":"FAIL" if fail else "PASS","failures":fail,"warnings":warn,"evidence":evidence}

def main()->int:
    p=argparse.ArgumentParser();p.add_argument("manifests",nargs="*");p.add_argument("--index");p.add_argument("--output");a=p.parse_args()
    paths=[ROOT/x for x in a.manifests]
    if a.index:
        idx=json.loads((ROOT/a.index).read_text(encoding="utf-8"));paths.extend(ROOT/x for x in idx["manifests"])
    if not paths:p.error("provide manifest(s) or --index")
    results=[run_manifest(x) for x in paths];status="FAIL" if any(x["status"]=="FAIL" for x in results) else "PASS"
    out=json.dumps({"schema_version":1,"status":status,"results":results},indent=2,ensure_ascii=False)+"\n"
    if a.output:Path(a.output).write_text(out,encoding="utf-8")
    print(out,end="");return 0 if status=="PASS" else 1
if __name__=="__main__":raise SystemExit(main())
