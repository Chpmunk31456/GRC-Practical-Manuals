from datetime import datetime, timezone, timedelta
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import publication_dashboard as dashboard

class PublicationDashboardTests(unittest.TestCase):
    def setUp(self):
        self.now=datetime.now(timezone.utc)
        self.revision='a'*40
        self.evidence={'categories':{key:{'status':'PASS','source_revision':self.revision,
            'observed_at':self.now.isoformat(),'unresolved_defects':[]} for key in dashboard.CATEGORIES}}
    def test_complete_evidence_is_only_ready_for_release_check(self):
        result=dashboard.summarize(self.evidence,self.revision,self.now)
        self.assertEqual(result['status'],'READY_FOR_INDEPENDENT_RELEASE_CHECK')
        self.assertFalse(result['publication_authorized'])
    def test_missing_category_blocks(self):
        del self.evidence['categories']['visual_review']
        self.assertIn('visual_review',dashboard.summarize(self.evidence,self.revision,self.now)['blocking_categories'])
    def test_stale_revision_blocks(self):
        self.evidence['categories']['writing']['source_revision']='b'*40
        self.assertEqual(dashboard.summarize(self.evidence,self.revision,self.now)['categories']['writing'],'STALE_REVISION')
    def test_expired_report_blocks(self):
        self.evidence['categories']['sources']['observed_at']=(self.now-timedelta(days=2)).isoformat()
        self.assertEqual(dashboard.summarize(self.evidence,self.revision,self.now)['categories']['sources'],'STALE_OBSERVATION')
    def test_future_report_blocks(self):
        self.evidence['categories']['pdf']['observed_at']=(self.now+timedelta(days=2)).isoformat()
        self.assertEqual(dashboard.summarize(self.evidence,self.revision,self.now)['status'],'BLOCKED')
    def test_defects_block_even_with_pass(self):
        self.evidence['categories']['docx']['unresolved_defects']=['test-defect']
        self.assertEqual(dashboard.summarize(self.evidence,self.revision,self.now)['status'],'BLOCKED')
    def test_pending_review_is_not_success(self):
        self.evidence['categories']['release_approval']['status']='PENDING'
        self.assertEqual(dashboard.summarize(self.evidence,self.revision,self.now)['status'],'BLOCKED')
    def test_human_summary_covers_every_control(self):
        summary=dashboard.render(dashboard.summarize({},self.revision,self.now))
        for key in dashboard.CATEGORIES:self.assertIn(key,summary)
if __name__=='__main__':unittest.main()
