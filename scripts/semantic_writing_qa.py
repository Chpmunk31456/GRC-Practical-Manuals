#!/usr/bin/env python3
"""Deterministic semantic-preservation checks for controlled writing.

This verifier is deliberately conservative. It detects high-value drift signals
without claiming full semantic equivalence and never rewrites source content.
"""
from __future__ import annotations
import argparse,json,re,sys
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from document_writing_qa import extract_blocks  # noqa: E402

DEFAULT_POLICY=ROOT/"config"/"writing_semantic_policy.json"
NUMBER_RE=re.compile(r"(?<![A-Za-z])[-+]?\d+(?:[.,]\d+)*(?:%|x|X)?")
URL_RE=re.compile(r"https?://\S+")
CITATION_RE=re.compile(r"(?:\[[0-9A-Za-z._-]+\]|\([A-Za-z][A-Za-z .-]+,?\s+\d{4}\))")
LIST_MARKER_RE=re.compile(r"(?m)^\s*(?:[-*+] |\d+[.)]\s+)")

def load_policy(path:Path=DEFAULT_POLICY)->dict:
    return json.loads(path.read_text(encoding="utf-8"))

def text_of(path:Path)->str:
    return "\n".join(block["text"] for block in extract_blocks(path))

def raw_text(path:Path)->str:
    if path.suffix.lower()==".docx": return text_of(path)
    return path.read_text(encoding="utf-8",errors="replace")

def tokens(pattern:re.Pattern,text:str)->Counter:
    return Counter(m.group(0) for m in pattern.finditer(text))

def patterns_tokens(text:str,patterns:list[str])->Counter:
    vals=[]
    for raw in patterns:
        vals.extend(m.group(0) for m in re.finditer(raw,text,re.I))
    return Counter(vals)

def concept_presence(text:str,locale:str,policy:dict)->set[str]:
    lowered=text.casefold();present=set()
    for concept,locales in policy.get("critical_concepts",{}).items():
        if any(phrase.casefold() in lowered for phrase in locales.get(locale,[])): present.add(concept)
    return present

def word_group_counts(text:str,groups:dict[str,list[str]])->dict[str,int]:
    lowered=text.casefold();out={}
    for group,words in groups.items():
        out[group]=sum(len(re.findall(r"(?<!\w)"+re.escape(w.casefold())+r"(?!\w)",lowered)) for w in words)
    return out

def add_counter_drift(findings:list[dict],code_prefix:str,s:Counter,t:Counter,severity:str="error")->None:
    removed=list((s-t).elements());introduced=list((t-s).elements())
    if removed: findings.append({"severity":severity,"code":f"removed_{code_prefix}","values":removed[:100]})
    if introduced: findings.append({"severity":severity,"code":f"introduced_{code_prefix}","values":introduced[:100]})

def compare(source:Path,target:Path,policy:dict,source_locale:str,target_locale:str)->dict:
    s=text_of(source);t=text_of(target);sr=raw_text(source);tr=raw_text(target);findings=[]

    add_counter_drift(findings,"numbers",tokens(NUMBER_RE,s),tokens(NUMBER_RE,t))
    add_counter_drift(findings,"identifiers",patterns_tokens(s,policy.get("identifier_patterns",[])),patterns_tokens(t,policy.get("identifier_patterns",[])))
    add_counter_drift(findings,"dates",patterns_tokens(s,policy.get("date_patterns",[])),patterns_tokens(t,policy.get("date_patterns",[])))
    add_counter_drift(findings,"currency",patterns_tokens(s,policy.get("currency_patterns",[])),patterns_tokens(t,policy.get("currency_patterns",[])))

    missing=sorted(concept_presence(s,source_locale,policy)-concept_presence(t,target_locale,policy))
    if missing: findings.append({"severity":"error","code":"missing_critical_concepts","values":missing})

    if source_locale==target_locale:
        sm=word_group_counts(s,policy.get("modal_groups",{}));tm=word_group_counts(t,policy.get("modal_groups",{}))
        if sm!=tm: findings.append({"severity":"error","code":"modal_strength_change","source":sm,"target":tm})
        neg_groups={"negation":policy.get("negation_terms",[])}
        sn=word_group_counts(s,neg_groups);tn=word_group_counts(t,neg_groups)
        if sn!=tn: findings.append({"severity":"error","code":"negation_change","source":sn,"target":tn})
        sl=len(LIST_MARKER_RE.findall(sr));tl=len(LIST_MARKER_RE.findall(tr))
        if tl<sl: findings.append({"severity":"error","code":"list_item_loss","source_count":sl,"target_count":tl})
        sc=tokens(CITATION_RE,s);tc=tokens(CITATION_RE,t)
        removed=list((sc-tc).elements())
        if removed: findings.append({"severity":"error","code":"citation_loss","values":removed[:100]})

    su,tu=tokens(URL_RE,s),tokens(URL_RE,t)
    if su!=tu:
        findings.append({"severity":"warning","code":"url_drift","removed":list((su-tu).elements())[:50],"introduced":list((tu-su).elements())[:50]})

    return {
        "schema_version":2,
        "source":source.relative_to(ROOT).as_posix() if source.is_relative_to(ROOT) else str(source),
        "target":target.relative_to(ROOT).as_posix() if target.is_relative_to(ROOT) else str(target),
        "source_locale":source_locale,
        "target_locale":target_locale,
        "status":"FAIL" if any(x["severity"]=="error" for x in findings) else "PASS",
        "findings":findings,
    }

def main()->int:
    p=argparse.ArgumentParser();p.add_argument("source");p.add_argument("target")
    p.add_argument("--source-locale",default="en");p.add_argument("--target-locale",default="en")
    p.add_argument("--policy",default=str(DEFAULT_POLICY));p.add_argument("--output");a=p.parse_args()
    source=Path(a.source);target=Path(a.target)
    if not source.is_absolute(): source=ROOT/source
    if not target.is_absolute(): target=ROOT/target
    r=compare(source,target,load_policy(Path(a.policy)),a.source_locale,a.target_locale)
    out=json.dumps(r,ensure_ascii=False,indent=2)+"\n"
    if a.output: Path(a.output).write_text(out,encoding="utf-8")
    print(out,end="");return 0 if r["status"]=="PASS" else 1
if __name__=="__main__":raise SystemExit(main())
