#!/usr/bin/env python3
"""Fail-closed integrity and recovery preflight for the writing system."""
from __future__ import annotations
import argparse, json, py_compile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"config"/"writing_system_manifest.json"

def run() -> dict:
    manifest=json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors=[]
    for rel in manifest["required_files"]:
        p=ROOT/rel
        if not p.is_file(): errors.append(f"missing required file: {rel}")
    for rel in manifest["json_configs"]:
        p=ROOT/rel
        try: json.loads(p.read_text(encoding="utf-8"))
        except Exception as exc: errors.append(f"invalid JSON {rel}: {exc}")
    for rel in manifest["python_modules"]:
        p=ROOT/rel
        try: py_compile.compile(str(p),doraise=True)
        except Exception as exc: errors.append(f"compile failure {rel}: {exc}")
    return {"schema_version":1,"status":"PASS" if not errors else "FAIL","errors":errors}

def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("--output"); args=p.parse_args()
    result=run(); out=json.dumps(result,indent=2)+"\n"
    if args.output: Path(args.output).write_text(out,encoding="utf-8")
    print(out,end="")
    return 0 if result["status"]=="PASS" else 1

if __name__=="__main__": raise SystemExit(main())
