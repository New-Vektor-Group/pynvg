import unittest
from pynvg.text import ordlist

class OrdListTestCase(unittest.TestCase):

    def test_ordlist(self):
        expectedList=[72,101,108,108,111]
        result=ordlist("Hello")
        self.assertEqual(result,expectedList)

if(__name__=="main"):
    unittest.main()