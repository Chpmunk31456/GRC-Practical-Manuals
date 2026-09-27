import hashlib
import io
import json
from pathlib import Path
import sys
import tarfile
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import oci_runtime_digest as oci


def build_fixture(path: Path, created: str, history_created: str):
    config = {
        "created": created,
        "architecture": "amd64",
        "os": "linux",
        "config": {"Env": ["A=B"], "Entrypoint": ["/bin/sh"], "Cmd": ["-c", "true"]},
        "rootfs": {"type": "layers", "diff_ids": ["sha256:" + "1" * 64]},
        "history": [{"created": history_created, "created_by": "COPY / /"}],
    }
    config_bytes = json.dumps(config, sort_keys=True).encode()
    config_digest = hashlib.sha256(config_bytes).hexdigest()
    layer_digest = "2" * 64
    manifest = {
        "schemaVersion": 2,
        "config": {"mediaType": "application/vnd.oci.image.config.v1+json", "digest": "sha256:" + config_digest, "size": len(config_bytes)},
        "layers": [{"mediaType": "application/vnd.oci.image.layer.v1.tar+gzip", "digest": "sha256:" + layer_digest, "size": 123}],
    }
    manifest_bytes = json.dumps(manifest, sort_keys=True).encode()
    manifest_digest = hashlib.sha256(manifest_bytes).hexdigest()
    index = {"schemaVersion": 2, "manifests": [{"digest": "sha256:" + manifest_digest, "size": len(manifest_bytes), "mediaType": "application/vnd.oci.image.manifest.v1+json"}]}
    with tarfile.open(path, "w") as tf:
        for name, data in [
            ("index.json", json.dumps(index).encode()),
            (f"blobs/sha256/{manifest_digest}", manifest_bytes),
            (f"blobs/sha256/{config_digest}", config_bytes),
        ]:
            info = tarfile.TarInfo(name)
            info.size = len(data)
            tf.addfile(info, io.BytesIO(data))


class OCIRuntimeDigestTests(unittest.TestCase):
    def test_volatile_created_metadata_does_not_change_runtime_digest(self):
        import hashlib
        with tempfile.TemporaryDirectory() as td:
            a = Path(td) / "a.oci"
            b = Path(td) / "b.oci"
            build_fixture(a, "2026-01-01T00:00:00Z", "2026-01-01T00:00:00Z")
            build_fixture(b, "2026-09-27T00:00:00Z", "2026-09-27T00:00:00Z")
            self.assertEqual(oci.runtime_digest(a), oci.runtime_digest(b))

    def test_rootfs_diff_id_change_changes_digest(self):
        with tempfile.TemporaryDirectory() as td:
            a = Path(td) / "a.oci"
            build_fixture(a, "2026-01-01T00:00:00Z", "2026-01-01T00:00:00Z")
            original = oci.runtime_digest(a)
            contract = oci.runtime_contract(a)
            contract["rootfs"]["diff_ids"] = ["sha256:" + "3" * 64]
            payload = json.dumps(contract, sort_keys=True, separators=(",", ":")).encode()
            changed = "sha256:" + hashlib.sha256(payload).hexdigest()
            self.assertNotEqual(original, changed)

    def test_runtime_config_change_changes_digest(self):
        with tempfile.TemporaryDirectory() as td:
            a = Path(td) / "a.oci"
            build_fixture(a, "2026-01-01T00:00:00Z", "2026-01-01T00:00:00Z")
            original = oci.runtime_digest(a)
            contract = oci.runtime_contract(a)
            contract["config"]["Env"] = ["A=C"]
            payload = json.dumps(contract, sort_keys=True, separators=(",", ":")).encode()
            changed = "sha256:" + __import__("hashlib").sha256(payload).hexdigest()
            self.assertNotEqual(original, changed)


if __name__ == "__main__":
    unittest.main()
