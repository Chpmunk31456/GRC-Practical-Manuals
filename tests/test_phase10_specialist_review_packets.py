from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import phase10_specialist_review_packets as packets


class Phase10SpecialistReviewPacketTests(unittest.TestCase):
    def test_packets_cover_specialist_decisions(self):
        result = packets.run()
        decision_types = {row["decision_type"] for row in result["packets"]}
        self.assertIn("localization_semantic", decision_types)
        self.assertIn("accessibility", decision_types)
        self.assertIn("legal_semantic", decision_types)
        self.assertIn("privacy_legal", decision_types)

    def test_each_packet_is_exactly_bound(self):
        result = packets.run()
        self.assertGreater(result["packet_count"], 0)
        for row in result["packets"]:
            self.assertEqual(len(row["packet_sha256"]), 64)
            self.assertEqual(len(row["source_revision"]), 40)
            self.assertTrue(row["artifacts"])
            self.assertTrue(row["review_scope"])
            self.assertIn("reviewer_id", row["submission_required_fields"])
            self.assertIn("evidence_sha256", row["submission_required_fields"])

    def test_artifact_inventory_is_trilingual_docx_pdf(self):
        result = packets.run()
        for row in result["packets"]:
            locales = {a["locale"] for a in row["artifacts"]}
            kinds = {a["kind"] for a in row["artifacts"]}
            self.assertEqual(locales, {"en", "es-419", "pt-BR"})
            self.assertEqual(kinds, {"docx", "pdf"})
            self.assertEqual(len(row["artifacts"]), 6)

    def test_automation_never_authors_specialist_decisions(self):
        result = packets.run()
        self.assertEqual(result["automation_authored_decisions"], 0)
        self.assertFalse(result["publication_authorized"])
        self.assertTrue(all(row["automation_authored_decision"] is False for row in result["packets"]))
        self.assertTrue(all(row["publication_authorized"] is False for row in result["packets"]))


if __name__ == "__main__":
    unittest.main()
