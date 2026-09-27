from pathlib import Path
import sys
import tempfile
import unittest
import zipfile
from datetime import date
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import accessibility_validation as access

class AccessibilityValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
    def make_docx(self,level=1,language='en-US',table='',alt='descr="Description"'):
        path=self.root/'test.docx'
        with zipfile.ZipFile(path,'w') as archive:
            archive.writestr('word/document.xml',f'<w:document xmlns:w="{access.W[1:-1]}" xmlns:wp="urn:test"><w:p><w:pPr><w:pStyle w:val="Heading{level}"/></w:pPr></w:p>{table}<wp:docPr {alt}/></w:document>')
            archive.writestr('word/styles.xml',f'<w:styles xmlns:w="{access.W[1:-1]}"><w:lang w:val="{language}"/><w:rFonts w:ascii="Arial"/></w:styles>')
            archive.writestr('docProps/core.xml','<core xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:title>Test</dc:title></core>')
        return path
    def test_structural_fixture(self):self.assertEqual(access.docx_findings(self.make_docx(),'en'),[])
    def test_skipped_heading(self):self.assertIn('heading_level_skipped',access.docx_findings(self.make_docx(level=3),'en'))
    def test_wrong_locale(self):self.assertIn('document_language_missing_or_mismatched',access.docx_findings(self.make_docx(),'pt-BR'))
    def test_missing_table_headers(self):self.assertIn('table_header_structure_missing',access.docx_findings(self.make_docx(table='<w:tbl><w:tr/></w:tbl>'),'en'))
    def test_missing_alt(self):self.assertIn('alternative_text_missing',access.docx_findings(self.make_docx(alt=''),'en'))
    def test_corrupt_package(self):
        path=self.root/'bad.docx';path.write_bytes(b'not a docx')
        with self.assertRaises(zipfile.BadZipFile):access.docx_findings(path,'en')
    def test_exact_independent_review(self):
        path=self.root/'review.md';path.write_text('Synthetic test record')
        artifacts={'a.pdf':'a'*64}
        review={'decision':'APPROVED','reviewer':'reviewer','producer':'producer','date':date.today().isoformat(),
                'scopes':sorted(access.SCOPES),'artifacts':artifacts,'evidence_path':'review.md','evidence_sha256':access.sha256(path)}
        self.assertTrue(access.review_current(review,artifacts,self.root))
        self.assertFalse(access.review_current(review,{'a.pdf':'b'*64},self.root))
        review['reviewer']='producer'
        self.assertFalse(access.review_current(review,artifacts,self.root))
    def test_absent_review(self):self.assertFalse(access.review_current({},{}))
if __name__=='__main__':unittest.main()
