import json,sys,tempfile,unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))

from controlled_publication_qa import run_manifest,validate_manifest_shape
from publication_roundtrip_qa import compare_text, signals, ID_RE
from publication_accessibility_qa import docx_checks,pdf_checks
from writing_observability_history import check
from writing_system_recovery_exercise import run as recovery_run
from semantic_writing_qa import compare,load_policy

class Phase4ControlledPublishingTests(unittest.TestCase):
    def test_manifest_index_preserves_phase4_reference_manuals(self):
        index=json.loads((ROOT/"config/controlled_publications/index.json").read_text(encoding="utf-8"))
        self.assertEqual(index["manifests"], ["config/controlled_publications/manual03.json"])
        self.assertIn("config/controlled_publications/manual04.json", index.get("candidate_manifests", []))
        self.assertGreaterEqual(len(index.get("candidate_manifests", [])), 1)

    def test_manifests_have_required_shape(self):
        index=json.loads((ROOT/"config/controlled_publications/index.json").read_text(encoding="utf-8"))
        for rel in index["manifests"] + index.get("candidate_manifests",[]):
            m=json.loads((ROOT/rel).read_text(encoding="utf-8"))
            self.assertEqual(validate_manifest_shape(m),[])

    def test_roundtrip_detects_numeric_loss(self):
        r=compare_text("Threshold 95%. Control 7.","Threshold 95%. Control 7.","Threshold 90%. Control 7.")
        self.assertEqual(r["status"],"FAIL")

    def test_identifier_parser_rejects_truncated_nist_suffix(self):
        self.assertIn("nist sp 800-53a", signals(ID_RE, "NIST SP 800-53A"))
        self.assertIn("nist sp 800-53a", signals(ID_RE, "NIST SP 800- 53A"))
        self.assertNotIn("nist sp 800-", signals(ID_RE, "NIST SP 800-"))

    def test_observability_threshold_blocks_regression(self):
        failures=check({"metrics":{"publication_failures":1}},{"thresholds":{"publication_failures":0}})
        self.assertTrue(failures)

    def test_recovery_exercise_core_passes(self):
        r=recovery_run(False)
        self.assertEqual(r["status"],"PASS","\n".join(r["errors"]))

    def test_semantic_negation_change_is_detected(self):
        policy=load_policy(ROOT/"config/writing_semantic_policy.json")
        with tempfile.TemporaryDirectory() as d:
            s=Path(d)/"s.txt";t=Path(d)/"t.txt"
            s.write_text("The owner must not approve the change.",encoding="utf-8")
            t.write_text("The owner must approve the change.",encoding="utf-8")
            r=compare(s,t,policy,"en","en")
            self.assertEqual(r["status"],"FAIL")
            self.assertIn("negation_change",{f["code"] for f in r["findings"]})

    def test_semantic_currency_drift_is_detected(self):
        policy=load_policy(ROOT/"config/writing_semantic_policy.json")
        with tempfile.TemporaryDirectory() as d:
            s=Path(d)/"s.txt";t=Path(d)/"t.txt"
            s.write_text("The approved limit is USD 5,000.",encoding="utf-8")
            t.write_text("The approved limit is USD 7,500.",encoding="utf-8")
            r=compare(s,t,policy,"en","en")
            self.assertEqual(r["status"],"FAIL")
            codes={f["code"] for f in r["findings"]}
            self.assertTrue("removed_currency" in codes or "introduced_currency" in codes)

if __name__=="__main__":unittest.main()
