import unittest
from pynvg.var import bitvector

class BitVectorTestCase(unittest.TestCase):

    def test_bitvector2(self):
        expected=bitvector(1)
        result=[1,0]
        self.assertEqual(result,expected)

    def test_bitvector5(self):
        expected=bitvector(2,5)
        result=[0,1,0,0,0]
        self.assertEqual(result,expected)

    def test_bitvectorTrue(self):
        expected=bitvector(True)
        result=[1,0]
        self.assertEqual(result,expected)

if(__name__=="main"):
    unittest.main()