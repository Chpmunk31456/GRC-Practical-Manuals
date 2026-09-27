import json
import sys
import tempfile
from datetime import date
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import translation_lifecycle as lifecycle

class TranslationLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);(self.root/'review.md').write_text('Synthetic reviewer evidence')
        self.source={'source.md':'a'*64};self.target={'target.md':'b'*64}
        self.previous={'source':self.source,'translation':self.target}
        self.review={'decision':'APPROVED','reviewer':'test-reviewer','date':date.today().isoformat(),
                     'source':self.source,'translation':self.target,'terminology_sha256':'c'*64,
                     'evidence_path':'review.md','evidence_sha256':lifecycle.sha256(self.root/'review.md')}
    def assess(self,source=None,target=None,review=True,missing=None):
        return lifecycle.assess(source or self.source,target or self.target,self.previous,
             self.review if review else None,'c'*64,missing or [],self.root)
    def test_exact_evidence(self):
        self.assertEqual(self.assess()['status'],'REVIEW_EVIDENCE_CURRENT')
    def test_changed_english_invalidates_review(self):
        result=self.assess(source={'source.md':'d'*64})
        self.assertIn('english_source_changed',result['reasons'])
        self.assertIn('review_evidence_missing_or_stale',result['reasons'])
    def test_changed_translation_invalidates_review(self):
        self.assertIn('translation_changed',self.assess(target={'target.md':'d'*64})['reasons'])
    def test_missing_human_review(self):
        self.assertEqual(self.assess(review=False)['status'],'REVIEW_REQUIRED')
    def test_tampered_evidence(self):
        (self.root/'review.md').write_text('tampered')
        self.assertEqual(self.assess()['status'],'REVIEW_REQUIRED')
    def test_changed_terminology(self):
        self.review['terminology_sha256']='d'*64
        self.assertEqual(self.assess()['status'],'REVIEW_REQUIRED')
    def test_missing_term(self):
        self.assertIn('controlled_terminology_missing',self.assess(missing=['NIST'])['reasons'])
    def test_empty_sources_fail(self):
        with self.assertRaises(ValueError):lifecycle.inventory(self.root,['absent/*.md'])
    def test_repository_locales_remain_unapproved(self):
        result=lifecycle.run()
        self.assertEqual({r['locale'] for r in result['results']},{'es-419','pt-BR'})
        self.assertTrue(all(r['status']=='REVIEW_REQUIRED' for r in result['results']))
if __name__=='__main__':unittest.main()
