import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import controlled_release as release

class ControlledReleaseTests(unittest.TestCase):
    def setUp(self):
        self.c={'source_revision':'a'*40,'version':'1.0.0','artifacts':{'a.pdf':'b'*64}}
        self.pull={'head':{'sha':'a'*40},'user':{'login':'author'}}
        self.policy={'reviewers':['one','two'],'minimum_independent_reviewers':2,'required_checks':sorted(release.REQUIRED_CHECKS)}
        self.checks=[{'id':i,'name':n,'head_sha':'a'*40,'conclusion':'success','app':{'slug':'github-actions'}} for i,n in enumerate(release.REQUIRED_CHECKS)]
        self.reviews=[{'id':i,'user':{'login':name,'type':'User'},'state':'APPROVED','commit_id':'a'*40,
            'body':'Publication approval: SHA256='+release.fingerprint(self.c)} for i,name in enumerate(['one','two'])]
    def verify(self):return release.verify_approvals(self.c,self.pull,self.reviews,self.checks,self.policy)
    def test_two_exact_independent_approvals(self):self.assertEqual(self.verify(),['one','two'])
    def test_hash_change_invalidates_approvals(self):
        self.c['artifacts']['a.pdf']='c'*64
        with self.assertRaises(ValueError):self.verify()
    def test_source_change_invalidates_approvals(self):
        self.c['source_revision']='c'*40
        with self.assertRaises(ValueError):self.verify()
    def test_self_approval_rejected(self):
        self.pull['user']['login']='one'
        with self.assertRaises(ValueError):self.verify()
    def test_bot_approval_rejected(self):
        self.reviews[0]['user']['type']='Bot'
        with self.assertRaises(ValueError):self.verify()
    def test_dismissed_review_rejected(self):
        self.reviews[0]['state']='DISMISSED'
        with self.assertRaises(ValueError):self.verify()
    def test_unknown_approvers_rejected(self):
        self.policy['reviewers']=[]
        with self.assertRaises(ValueError):self.verify()
    def test_failed_check_rejected(self):
        self.checks[0]['conclusion']='failure'
        with self.assertRaises(ValueError):self.verify()
    def test_non_github_check_cannot_spoof_success(self):
        self.checks[0]['app']['slug']='untrusted-app'
        with self.assertRaises(ValueError):self.verify()
    def test_removed_mandatory_checks_rejected(self):
        self.policy['required_checks']=[]
        with self.assertRaises(ValueError):self.verify()
    def test_semantic_versions(self):
        for value in ['1.2.3','0.1.0-rc.1+build.7']:self.assertIsNotNone(release.SEMVER.fullmatch(value))
        for value in ['1.2','01.2.3','1.2.3-01']:self.assertIsNone(release.SEMVER.fullmatch(value))
    def test_two_builds_hash_and_inventory(self):
        with tempfile.TemporaryDirectory() as td:
            roots=[Path(td)/'first',Path(td)/'second']
            manifest={'manual_root':'manual','languages':{'en':{'artifacts':{'docx':'x.docx','pdf':'x.pdf'}}}}
            candidate={'source_revision':'a'*40,'toolchain_sha256':'b'*64,'artifacts':{}}
            for i,root in enumerate(roots):
                (root/'manual').mkdir(parents=True)
                for name in ['x.docx','x.pdf']:
                    (root/'manual'/name).write_bytes(b'synthetic')
                    candidate['artifacts']['manual/'+name]=release.sha256(root/'manual'/name)
                (root/'build-receipt.json').write_text(json.dumps({'source_revision':'a'*40,'toolchain_sha256':'b'*64,'build_id':str(i)}))
            release.verify_builds(candidate,manifest,*roots)
            (roots[1]/'manual/x.pdf').write_bytes(b'changed')
            with self.assertRaises(ValueError):release.verify_builds(candidate,manifest,*roots)
            with self.assertRaises(ValueError):release.verify_builds(candidate,manifest,roots[0],roots[0])
if __name__=='__main__':unittest.main()
