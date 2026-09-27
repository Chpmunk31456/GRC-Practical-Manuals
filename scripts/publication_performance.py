#!/usr/bin/env python3
"""Measure sequential/concurrent publication validation without reusing PASS results."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import subprocess
import sys
import time
from repository_publication_qa import ROOT, run


def control_outcomes(report):
    return {item['manual_id']:{name:gate['status'] for name,gate in item['gates'].items()} for item in report['results']}


def benchmark():
    sequential=run(workers=1)
    concurrent=run(workers=2)
    started=time.perf_counter()
    tests=subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-q'],cwd=ROOT,capture_output=True,timeout=180)
    return {'schema_version':1,'source_revision':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
            'status':'PASS' if sequential['status']=='PASS' and concurrent['status']=='PASS' and tests.returncode==0
                     and control_outcomes(sequential)==control_outcomes(concurrent) else 'FAIL',
            'validation_sequential_seconds':sequential['seconds'],
            'validation_concurrent_seconds':concurrent['seconds'],
            'speedup':round(sequential['seconds']/max(concurrent['seconds'],0.000001),3),
            'regression_seconds':round(time.perf_counter()-started,6),'regression_exit_code':tests.returncode,
            'outcomes_equal':control_outcomes(sequential)==control_outcomes(concurrent),
            'mandatory_gates_executed_per_manual':list(next(iter(control_outcomes(sequential).values()))),
            'dependency_installation':'NO_NEW_PYTHON_DEPENDENCIES',
            'artifact_generation':'NOT_MEASURED_REQUIRES_VERIFIED_PRODUCTION_TOOLCHAIN',
            'incremental_artifact_builds':'DISABLED_PENDING_REPRODUCIBILITY_VERIFICATION',
            'validation_result_cache':'DISABLED'}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=benchmark()
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('Publication performance: '+result['status'])
    return 0 if result['status']=='PASS' else 1
if __name__=='__main__':raise SystemExit(main())
