#!/usr/bin/env python3
"""Verify a public tracked-file backup and exercise recovery in isolation."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import tempfile
import time
import zipfile
from repository_publication_qa import ROOT, read_json
from controlled_publication_qa import sha256

MAX_TOTAL=1024*1024*1024


def allowed(name):
    path=PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or '\\' in name or ':' in name:
        return False
    if any(re.search(r'(^\.env|private|credentials|secret|writing.samples|\.pem$|\.key$)',part,re.I) for part in path.parts):
        return False
    return path.parts[0] in {'scripts','tests','config','.compliance','.github','governance','docs','qa',
         '01-foundations','02-management-systems','03-assurance-and-audit','04-regulatory-compliance',
         '05-operational-resilience','06-cloud-and-technology-risk','07-third-party-risk','08-templates-and-tools',
         '09-enterprise-grc','10-ai-governance'} or len(path.parts)==1 and path.suffix.lower() in {'.md','.json','.ini'}


def backup(destination):
    destination.mkdir(parents=True,exist_ok=False)
    revision=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    names=subprocess.check_output(['git','ls-tree','-r','--name-only',revision],cwd=ROOT,text=True).splitlines()
    selected=[name for name in names if allowed(name)]
    # Archive committed public files only: local documents and credentials are never read.
    with tempfile.TemporaryDirectory() as td:
        raw=Path(td)/'tracked.zip'
        subprocess.run(['git','archive','--format=zip','--output',str(raw),revision],cwd=ROOT,check=True)
        digests={}
        with zipfile.ZipFile(raw) as original,zipfile.ZipFile(destination/'backup.zip','w',compression=zipfile.ZIP_DEFLATED) as output:
            for name in selected:
                info=original.getinfo(name)
                if stat.S_ISLNK(info.external_attr>>16):raise ValueError('links are not permitted in backup')
                data=original.read(name)
                output.writestr(name,data)
                digests[name]=hashlib.sha256(data).hexdigest()
    receipt={'schema_version':1,'source_revision':revision,'archive_sha256':sha256(destination/'backup.zip'),'files':digests}
    (destination/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    return receipt


def restore(archive,receipt,target):
    if target.exists():raise ValueError('recovery destination must not exist')
    if sha256(archive)!=receipt['archive_sha256']:raise ValueError('archive digest mismatch')
    with zipfile.ZipFile(archive) as source:
        members=source.infolist()
        names=[item.filename for item in members]
        if len(names)!=len(set(names)) or set(names)!=set(receipt['files']):
            raise ValueError('backup inventory mismatch')
        if sum(item.file_size for item in members)>MAX_TOTAL:raise ValueError('backup size limit exceeded')
        for item in members:
            if not allowed(item.filename) or item.is_dir() or stat.S_ISLNK(item.external_attr>>16):
                raise ValueError('unsafe backup member')
            if hashlib.sha256(source.read(item)).hexdigest()!=receipt['files'][item.filename]:
                raise ValueError('file digest mismatch')
        target.mkdir(parents=True)
        for item in members:
            path=target/item.filename;path.parent.mkdir(parents=True,exist_ok=True)
            path.write_bytes(source.read(item))
    return len(members)


def exercise():
    start=time.perf_counter()
    with tempfile.TemporaryDirectory() as td:
        root=Path(td)
        receipt=backup(root/'snapshot')
        count=restore(root/'snapshot/backup.zip',receipt,root/'restored')
        checks=[]
        for command in ([sys.executable,'scripts/writing_system_integrity.py'],
                        [sys.executable,'-m','unittest','discover','-s','tests','-q']):
            run=subprocess.run(command,cwd=root/'restored',capture_output=True,timeout=180)
            checks.append({'check':'integrity' if 'scripts/writing_system_integrity.py' in command else 'regression',
                           'exit_code':run.returncode})
    return {'schema_version':1,'status':'PASS' if all(c['exit_code']==0 for c in checks) else 'FAIL',
            'source_revision':receipt['source_revision'],'archive_sha256':receipt['archive_sha256'],
            'restored_files':count,'checks':checks,'seconds':round(time.perf_counter()-start,3),
            'production_overwritten':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=exercise()
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('Isolated backup recovery: '+result['status'])
    return 0 if result['status']=='PASS' else 1
if __name__=='__main__':raise SystemExit(main())
