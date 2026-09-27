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


def build_fixture(path: Path, created: str, history_created: str, payload: bytes = b"runtime"):
    layer_buffer = io.BytesIO()
    with tarfile.open(fileobj=layer_buffer, mode="w") as layer_tar:
        info = tarfile.TarInfo("usr/bin/tool")
        info.mode = 0o755
        info.uid = 0
        info.gid = 0
        info.mtime = int(created[:4]) if created[:4].isdigit() else 0
        info.size = len(payload)
        layer_tar.addfile(info, io.BytesIO(payload))
    layer_bytes = layer_buffer.getvalue()
    layer_digest = hashlib.sha256(layer_bytes).hexdigest()

    config = {
        "created": created,
        "architecture": "amd64",
        "os": "linux",
        "config": {"Env": ["A=B"], "Entrypoint": ["/bin/sh"], "Cmd": ["-c", "true"]},
        "rootfs": {"type": "layers", "diff_ids": ["sha256:" + hashlib.sha256(layer_bytes).hexdigest()]},
        "history": [{"created": history_created, "created_by": "COPY / /"}],
    }
    config_bytes = json.dumps(config, sort_keys=True).encode()
    config_digest = hashlib.sha256(config_bytes).hexdigest()
    manifest = {
        "schemaVersion": 2,
        "config": {"mediaType": "application/vnd.oci.image.config.v1+json", "digest": "sha256:" + config_digest, "size": len(config_bytes)},
        "layers": [{"mediaType": "application/vnd.oci.image.layer.v1.tar", "digest": "sha256:" + layer_digest, "size": len(layer_bytes)}],
    }
    manifest_bytes = json.dumps(manifest, sort_keys=True).encode()
    manifest_digest = hashlib.sha256(manifest_bytes).hexdigest()
    index = {"schemaVersion": 2, "manifests": [{"digest": "sha256:" + manifest_digest, "size": len(manifest_bytes), "mediaType": "application/vnd.oci.image.manifest.v1+json"}]}
    with tarfile.open(path, "w") as tf:
        for name, data in [
            ("index.json", json.dumps(index).encode()),
            (f"blobs/sha256/{manifest_digest}", manifest_bytes),
            (f"blobs/sha256/{config_digest}", config_bytes),
            (f"blobs/sha256/{layer_digest}", layer_bytes),
        ]:
            info = tarfile.TarInfo(name)
            info.size = len(data)
            tf.addfile(info, io.BytesIO(data))

