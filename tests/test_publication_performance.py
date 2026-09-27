from pathlib import Path
import sys
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import repository_publication_qa as publication
from publication_performance import control_outcomes

class PublicationPerformanceTests(unittest.TestCase):
    def test_parallel_and_serial_execute_identical_gates(self):
        with patch.object(publication,'execute_gate',return_value={'status':'PASS'}) as gate:
            serial=publication.run(workers=1);parallel=publication.run(workers=2)
        self.assertEqual(control_outcomes(serial),control_outcomes(parallel))
        self.assertEqual(gate.call_count,16)
        self.assertFalse(parallel['validation_cache_used'])
    def test_affected_document_cannot_reuse_previous_pass(self):
        with patch.object(publication,'execute_gate',return_value={'status':'PASS'}):
            first=publication.run(workers=2)
        def changed(name,path,manifest):
            return {'status':'FAIL' if name=='roundtrip' else 'PASS'}
        with patch.object(publication,'execute_gate',side_effect=changed) as gate:
            second=publication.run(workers=2)
        self.assertEqual(first['status'],'PASS')
        self.assertEqual(second['status'],'FAIL')
        self.assertEqual(gate.call_count,8)
    def test_failure_in_one_worker_preserves_other_gates(self):
        def broken(name,path,manifest):
            if name=='publication':raise RuntimeError('test failure')
            return {'status':'PASS'}
        with patch.object(publication,'execute_gate',side_effect=broken) as gate:
            result=publication.run(workers=4)
        self.assertEqual(result['status'],'FAIL');self.assertEqual(gate.call_count,8)
        self.assertTrue(all(x['gates']['accessibility']['status']=='PASS' for x in result['results']))
    def test_workers_bounded(self):
        for workers in (0,5,True):
            with self.subTest(workers=workers),self.assertRaises(ValueError):publication.run(workers=workers)
if __name__=='__main__':unittest.main()
