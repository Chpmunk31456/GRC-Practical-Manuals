from pathlib import Path
import sys
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import review_evidence_status as evidence
import review_readiness_packets as readiness
from controlled_publication_qa import sha256


class ReviewEvidenceStatusTests(unittest.TestCase):
    def test_empty_bindings_are_incomplete_and_never_authorize(self):
        result = evidence.run(bindings={})
        self.assertEqual(result["status"], "INCOMPLETE")
        self.assertFalse(result["publication_authorized"])
        self.assertGreater(result["candidate_count"], 0)
        for manual in result["manuals"]:
            self.assertEqual(manual["evidence_status"], "INCOMPLETE")
            self.assertEqual(manual["readiness_status"], "REVIEW_REQUIRED")
            self.assertFalse(manual["publication_authorized"])

    def test_old_packet_binding_is_stale(self):
        packets = readiness.run()["packets"]
        packet = packets[0]
        review_path = packet["review_records"][0]["path"]
        bindings = {
            packet["manual_id"]: {
                review_path: {
                    "packet_sha256": "0" * 64,
                    "evidence_path": review_path,
                    "evidence_sha256": sha256(ROOT / review_path),
                }
            }
        }
        result = evidence.run(bindings=bindings)
        manual = next(m for m in result["manuals"] if m["manual_id"] == packet["manual_id"])
        row = next(r for r in manual["review_evidence"] if r["review_record"] == review_path)
        self.assertEqual(row["status"], "STALE")
        self.assertEqual(row["reason"], "packet_hash_mismatch")

    def test_exact_packet_and_file_hash_is_current_metadata_only(self):
        packet = readiness.run()["packets"][0]
        review_path = packet["review_records"][0]["path"]
        bindings = {
            packet["manual_id"]: {
                review_path: {
                    "packet_sha256": packet["packet_sha256"],
                    "evidence_path": review_path,
                    "evidence_sha256": sha256(ROOT / review_path),
                }
            }
        }
        result = evidence.run(bindings=bindings)
        manual = next(m for m in result["manuals"] if m["manual_id"] == packet["manual_id"])
        row = next(r for r in manual["review_evidence"] if r["review_record"] == review_path)
        self.assertEqual(row["status"], "CURRENT")
        self.assertFalse(result["publication_authorized"])
        self.assertEqual(manual["readiness_status"], "REVIEW_REQUIRED")

    def test_hash_mismatch_is_stale(self):
        packet = readiness.run()["packets"][0]
        review_path = packet["review_records"][0]["path"]
        bindings = {
            packet["manual_id"]: {
                review_path: {
                    "packet_sha256": packet["packet_sha256"],
                    "evidence_path": review_path,
                    "evidence_sha256": "f" * 64,
                }
            }
        }
        result = evidence.run(bindings=bindings)
        manual = next(m for m in result["manuals"] if m["manual_id"] == packet["manual_id"])
        row = next(r for r in manual["review_evidence"] if r["review_record"] == review_path)
        self.assertEqual(row["status"], "STALE")
        self.assertEqual(row["reason"], "evidence_hash_mismatch")

    def test_invalid_injected_revision_still_fails_closed(self):
        with mock.patch.dict("os.environ", {"CONTROLLED_SOURCE_REVISION": "bad"}, clear=False):
            with self.assertRaises(ValueError):
                evidence.run(bindings={})


if __name__ == "__main__":
    unittest.main()
