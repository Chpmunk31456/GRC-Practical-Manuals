#!/usr/bin/env python3
"""Inspect accessibility structure and require independent exact-artifact review."""
from __future__ import annotations
import argparse
from datetime import date
import json
from pathlib import Path
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
import zipfile
from repository_publication_qa import ROOT, discover, contained, read_json
from controlled_publication_qa import sha256

W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
SCOPES={'reading_order','screen_reader','table_relationships','alternative_text','font_compatibility','visual_layout'}
FONTS={'Arial','Calibri','Aptos','Cambria','Times New Roman','Liberation Sans','Liberation Serif','DejaVu Sans','Courier New','Consolas'}


def docx_findings(path,locale):
    findings=[]
    with zipfile.ZipFile(path) as archive:
        document=ET.fromstring(archive.read('word/document.xml'))
        styles=ET.fromstring(archive.read('word/styles.xml'))
        metadata=ET.fromstring(archive.read('docProps/core.xml'))
    levels=[]
    for paragraph in document.iter(W+'p'):
        style=paragraph.find(W+'pPr/'+W+'pStyle')
        if style is not None:
            match=re.fullmatch(r'Heading([1-9])',style.get(W+'val',''),re.I)
            if match:levels.append(int(match.group(1)))
    if not levels:findings.append('heading_structure_missing')
    if levels and (levels[0]!=1 or any(b>a+1 for a,b in zip(levels,levels[1:]))):
        findings.append('heading_level_skipped')
    languages={node.get(W+'val') for node in styles.iter(W+'lang')}
    accepted={'en','en-US'} if locale=='en' else {locale}
    if not languages.intersection(accepted):findings.append('document_language_missing_or_mismatched')
    for table in document.iter(W+'tbl'):
        rows=table.findall(W+'tr')
        if not rows or rows[0].find(W+'trPr/'+W+'tblHeader') is None:
            findings.append('table_header_structure_missing')
    for node in document.iter():
        if node.tag.endswith('}docPr') and not (node.get('descr','').strip() or node.get('title','').strip()):
            findings.append('alternative_text_missing')
    fonts={value for tree in (document,styles) for node in tree.iter(W+'rFonts')
           for key,value in node.attrib.items() if key in {W+'ascii',W+'hAnsi',W+'eastAsia',W+'cs'}}
    if not fonts or fonts-FONTS:findings.append('font_compatibility_review_required')
    title=metadata.find('{http://purl.org/dc/elements/1.1/}title')
    if title is None or not (title.text or '').strip():findings.append('accessible_title_missing')
    return sorted(set(findings))


def pdf_findings(path,locale):
    if not shutil.which('pdfinfo') or not shutil.which('pdffonts'):
        return ['pdf_inspection_tools_missing']
    info=subprocess.check_output(['pdfinfo',str(path)],text=True,errors='replace')
    fonts=subprocess.check_output(['pdffonts',str(path)],text=True,errors='replace')
    findings=[]
    if not re.search(r'^Tagged:\s+yes\s*$',info,re.M):findings.append('pdf_tag_structure_missing')
    if not re.search(r'^Title:\s+\S',info,re.M):findings.append('pdf_accessible_title_missing')
    if re.search(r'^Encrypted:\s+yes',info,re.M):findings.append('pdf_encryption_review_required')
    # Font rows end in emb/sub/uni and object ID; uncertain formats require review.
    rows=fonts.splitlines()[2:]
    if not rows or any(not re.search(r'\byes\s+(?:yes|no)\s+yes\s+\d+\s+\d+\s*$',row) for row in rows if row.strip()):
        findings.append('pdf_font_embedding_or_unicode_review_required')
    # PDF language and meaningful reading order require parsed structure/human review.
    findings.append('pdf_language_and_reading_order_independent_review')
    return findings


def review_current(review,artifacts,root=ROOT):
    try:
        return (review['decision']=='APPROVED' and bool(review['reviewer'].strip())
                and review['reviewer']!=review['producer'] and bool(review['producer'].strip())
                and date.fromisoformat(review['date'])<=date.today()
                and set(review['scopes'])==SCOPES and review['artifacts']==artifacts
                and sha256(contained(root,review['evidence_path']))==review['evidence_sha256'])
    except (KeyError,ValueError,TypeError,OSError):return False


def run():
    reviews=read_json(ROOT/'config/accessibility_reviews.json')['reviews']
    manifests,_=discover();results=[]
    for _,manifest in manifests:
        root=contained(ROOT,manifest['manual_root']);artifacts={};findings=[]
        for locale,cfg in manifest['languages'].items():
            for kind in ('docx','pdf'):
                relative=manifest['manual_root']+'/'+cfg['artifacts'][kind]
                path=contained(ROOT,relative)
                try:
                    artifacts[relative]=sha256(path)
                    codes=docx_findings(path,locale) if kind=='docx' else pdf_findings(path,locale)
                except (OSError,ValueError,KeyError,ET.ParseError,zipfile.BadZipFile,subprocess.CalledProcessError):
                    codes=['artifact_inspection_failed']
                findings += [{'locale':locale,'kind':kind,'code':code} for code in codes]
        review=reviews.get(manifest['manual_id'],{})
        human=review_current(review,artifacts)
        automatic=[f for f in findings if f['code']!='pdf_language_and_reading_order_independent_review']
        results.append({'manual_id':manifest['manual_id'],'artifacts':artifacts,'findings':findings,
                        'independent_review':'CURRENT' if human else 'REQUIRED',
                        'status':'PASS' if human and not automatic else 'REVIEW_REQUIRED',
                        'fully_accessible_claim':False})
    return {'schema_version':1,'status':'PASS' if all(r['status']=='PASS' for r in results) else 'REVIEW_REQUIRED','results':results}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=run()
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('Accessibility validation: '+result['status'])
    return 0
if __name__=='__main__':raise SystemExit(main())
