import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))

from semantic_writing_qa import compare, load_policy as load_semantic_policy
from unified_writing_engine import validate_feedback
from writing_observability import summarize
from writing_system_integrity import run as integrity_run


class Phase3WritingSystemTests(unittest.TestCase):
    def setUp(self):
        self.semantic_policy=load_semantic_policy(ROOT/"config"/"writing_semantic_policy.json")

    def test_semantic_verifier_detects_altered_number(self):
        with tempfile.TemporaryDirectory() as d:
            source=Path(d)/"source.txt"; target=Path(d)/"target.txt"
            source.write_text("The threshold is 95%.",encoding="utf-8")
            target.write_text("The threshold is 90%.",encoding="utf-8")
            result=compare(source,target,self.semantic_policy,"en","en")
            self.assertEqual(result["status"],"FAIL")
            codes={x["code"] for x in result["findings"]}
            self.assertIn("removed_numbers",codes)
            self.assertIn("introduced_numbers",codes)

    def test_semantic_verifier_detects_modal_change(self):
        with tempfile.TemporaryDirectory() as d:
            source=Path(d)/"source.txt"; target=Path(d)/"target.txt"
            source.write_text("The owner must review evidence.",encoding="utf-8")
            target.write_text("The owner may review evidence.",encoding="utf-8")
            result=compare(source,target,self.semantic_policy,"en","en")
            self.assertEqual(result["status"],"FAIL")
            self.assertIn("modal_strength_change",{x["code"] for x in result["findings"]})

    def test_cross_language_concept_preservation(self):
        with tempfile.TemporaryDirectory() as d:
            source=Path(d)/"source.txt"; target=Path(d)/"target.txt"
            source.write_text("Human oversight governs residual risk and evidence.",encoding="utf-8")
            target.write_text("La supervisión humana gobierna el riesgo residual y la evidencia.",encoding="utf-8")
            result=compare(source,target,self.semantic_policy,"en","es-419")
            self.assertFalse(any(x["code"]=="missing_critical_concepts" for x in result["findings"]))

    def test_unapproved_feedback_fails_closed(self):
        errors=validate_feedback({"approved_rules":[{"approved":False,"provenance":"x"}],"approved_examples":[]})
        self.assertTrue(errors)

    def test_approved_feedback_requires_provenance(self):
        errors=validate_feedback({"approved_rules":[{"approved":True}],"approved_examples":[]})
        self.assertTrue(errors)

    def test_observability_aggregates_reports(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"report.json"
            p.write_text(json.dumps({
                "status":"FAIL","context":"resume",
                "writing_qa":{"counts":{"errors":1,"warnings":2},"findings":[{"code":"x"}]},
                "semantic_qa":{"status":"FAIL","findings":[{"code":"removed_numbers"}]}
            }),encoding="utf-8")
            result=summarize([p])
            self.assertEqual(result["metrics"]["reports"],1)
            self.assertEqual(result["metrics"]["semantic_failures"],1)

    def test_context_profiles_cover_phase3_surfaces(self):
        data=json.loads((ROOT/"config"/"writing_context_profiles.json").read_text(encoding="utf-8"))
        required={"technical_documentation","executive_report","resume","cover_letter","recruiter_reply","general_professional"}
        self.assertTrue(required.issubset(data["profiles"]))

    def test_integrity_manifest_passes(self):
        result=integrity_run()
        self.assertEqual(result["status"],"PASS","\n".join(result["errors"]))


if __name__=="__main__":
    unittest.main()
