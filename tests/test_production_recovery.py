import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import production_recovery as recovery
from controlled_release import verify_toolchain_record

class ProductionRecoveryTests(unittest.TestCase):
    def test_production_dockerfile_is_backed_up(self):
        self.assertTrue(recovery.allowed("Dockerfile.production"))

    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
    def fixture(self,name='docs/example.md'):
        archive=self.root/'backup.zip';data=b'public test fixture'
        with zipfile.ZipFile(archive,'w') as output:output.writestr(name,data)
        return archive,{'archive_sha256':recovery.sha256(archive),'files':{name:hashlib.sha256(data).hexdigest()}}
    def test_unverified_production_toolchain_blocks(self):
        with self.assertRaises(ValueError):verify_toolchain_record({'status':'REVIEW_REQUIRED'})
    def test_deleted_environment_fields_cannot_bypass_gate(self):
        with self.assertRaises(ValueError):verify_toolchain_record({'status':'VERIFIED','python':'3.12.14','pdf_toolchain':{},'build_environment':{}})
    def test_complete_toolchain_record_shape(self):
        verify_toolchain_record({'status':'VERIFIED','python':'3.12.14',
            'pdf_toolchain':{'poppler_package_version':'test-version','container_digest':'sha256:'+'a'*64},
            'build_environment':{'generator_dependency_lock_sha256':'b'*64,'container_digest':'sha256:'+'c'*64}})
    def test_restore_exact_bytes(self):
        archive,receipt=self.fixture();target=self.root/'restored'
        self.assertEqual(recovery.restore(archive,receipt,target),1)
        self.assertEqual((target/'docs/example.md').read_bytes(),b'public test fixture')
    def test_archive_corruption_fails(self):
        archive,receipt=self.fixture();archive.write_bytes(b'corrupt')
        with self.assertRaises(ValueError):recovery.restore(archive,receipt,self.root/'restored')
    def test_file_hash_corruption_fails(self):
        archive,receipt=self.fixture();receipt['files']['docs/example.md']='a'*64
        with self.assertRaises(ValueError):recovery.restore(archive,receipt,self.root/'restored')
    def test_no_overwrite(self):
        archive,receipt=self.fixture()
        with self.assertRaises(ValueError):recovery.restore(archive,receipt,self.root)
    def test_path_escape_fails(self):
        archive,receipt=self.fixture('../escape')
        with self.assertRaises(ValueError):recovery.restore(archive,receipt,self.root/'restored')
    def test_private_files_excluded(self):
        for name in ['.env','docs/private-sample.md','credentials/key.json','docs/key.pem','local/sample.docx']:
            self.assertFalse(recovery.allowed(name))
    def test_inventory_mismatch_fails(self):
        archive,receipt=self.fixture();receipt['files']={}
        with self.assertRaises(ValueError):recovery.restore(archive,receipt,self.root/'restored')
    def test_duplicate_members_fail(self):
        archive,receipt=self.fixture()
        with zipfile.ZipFile(archive,'a') as output:output.writestr('docs/example.md',b'duplicate')
        receipt['archive_sha256']=recovery.sha256(archive)
        with self.assertRaises(ValueError):recovery.restore(archive,receipt,self.root/'restored')
if __name__=='__main__':unittest.main()
