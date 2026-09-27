import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import review_readiness_packets as readiness
import repository_publication_qa as repository


class ReviewReadinessPacketTests(unittest.TestCase):
    def test_every_candidate_has_deterministic_packet(self):
        manifests, _ = repository.discover()
        expected = [m["manual_id"] for _, m in manifests if m["rollout_lane"] == "candidate"]
        first = readiness.run()
        second = readiness.run()
        self.assertEqual(first, second)
        self.assertEqual(first["candidate_count"], len(expected))
        self.assertEqual([p["manual_id"] for p in first["packets"]], expected)

    def test_active_manual_is_not_in_human_candidate_queue(self):
        result = readiness.run()
        self.assertNotIn("manual03-nist-ai-rmf", [p["manual_id"] for p in result["packets"]])

    def test_packets_bind_exact_revision_manifest_sources_artifacts_and_reviews(self):
        result = readiness.run()
        sha64 = re.compile(r"^[0-9a-f]{64}$")
        sha40 = re.compile(r"^[0-9a-f]{40}$")
        self.assertRegex(result["source_revision"], sha40)
        for packet in result["packets"]:
            self.assertEqual(packet["source_revision"], result["source_revision"])
            self.assertRegex(packet["packet_sha256"], sha64)
            self.assertRegex(packet["manifest"]["sha256"], sha64)
            self.assertFalse(packet["publication_authorized"])
            self.assertEqual(set(packet["sources"]), {"en", "es-419", "pt-BR"})
            self.assertEqual(set(packet["artifacts"]), {"en", "es-419", "pt-BR"})
            for locale in packet["sources"].values():
                self.assertTrue(locale)
                for row in locale:
                    self.assertRegex(row["sha256"], sha64)
            for locale in packet["artifacts"].values():
                self.assertEqual(set(locale), {"docx", "pdf"})
                for row in locale.values():
                    self.assertRegex(row["sha256"], sha64)
            self.assertTrue(packet["review_records"])
            for row in packet["review_records"]:
                self.assertEqual(row["status"], "REVIEW_REQUIRED")
                self.assertRegex(row["sha256"], sha64)

    def test_repository_blockers_are_fail_closed(self):
        blockers = readiness.repository_blockers()
        self.assertIn("approved_source_baselines_missing", blockers)
        self.assertIn("hash_bound_translation_reviews_missing", blockers)
        self.assertIn("independent_accessibility_reviews_missing", blockers)
        self.assertIn("production_toolchain_not_verified", blockers)
        self.assertIn("authorized_release_reviewers_missing", blockers)

    def test_queue_never_authorizes_publication(self):
        result = readiness.run()
        self.assertEqual(result["status"], "REVIEW_REQUIRED")
        self.assertFalse(result["publication_authorized"])
        for row in result["queue"]:
            self.assertEqual(row["status"], "REVIEW_REQUIRED")
            self.assertTrue(row["required_review_records"])


if __name__ == "__main__":
    unittest.main()
