import copy
from datetime import date
import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import source_monitoring as monitor

class SourceMonitoringTests(unittest.TestCase):
    def setUp(self):
        self.source={'id':'example','version':'1.0','last_verified':'2026-09-27','review_interval_days':30}
        self.baseline={'sha256':'a'*64,'revision':'1.0','publication_date':'2026-01-01','approval_evidence':'reviewed-record'}
        self.observed={'sha256':'a'*64}
    def assess(self,baseline=None,observed=None):
        return monitor.assess(self.source,baseline,observed,[{'manual_id':'example','chapters':[1]}],date(2026,9,27))
    def test_unchanged_observation_is_current(self):
        self.assertEqual(self.assess(self.baseline,self.observed)['status'],'CURRENT')
    def test_change_requires_review_without_mutation(self):
        before=copy.deepcopy(self.baseline)
        result=self.assess(self.baseline,{'sha256':'b'*64})
        self.assertIn('content_changed',result['reasons'])
        self.assertEqual(before,self.baseline)
    def test_absent_baseline_is_not_approved(self):
        self.assertIn('baseline_human_review_required',self.assess(None,self.observed)['reasons'])
    def test_network_failure_requires_review(self):
        self.assertIn('observation_unavailable',self.assess(self.baseline,None)['reasons'])
    def test_review_identifiers_are_stable(self):
        self.assertEqual(self.assess()['review_id'],self.assess()['review_id'])
    def test_due_review(self):
        self.source['last_verified']='2020-01-01'
        self.assertIn('review_date_due_or_invalid',self.assess(self.baseline,self.observed)['reasons'])
    def test_unsafe_urls_rejected(self):
        for url in ['http://www.nist.gov','https://localhost','https://www.nist.gov:8443','https://user@www.nist.gov']:
            with self.subTest(url=url),self.assertRaises(ValueError):monitor.validate_url(url)
    def test_approved_domain(self):
        monitor.validate_url('https://www.nist.gov/itl')
    def test_registry_and_chapter_mappings(self):
        result=monitor.run(False)
        self.assertTrue(result['results'])
        self.assertEqual(result['baseline_updates'],0)
        self.assertEqual(result['status'],'REVIEW_REQUIRED')
if __name__=='__main__':unittest.main()
