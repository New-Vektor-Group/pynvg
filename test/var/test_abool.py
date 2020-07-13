import unittest
from pynvg.var import abool

class ABoolTestCase(unittest.TestCase):

    def test_aboolTrue(self):
        result=abool(True)
        self.assertTrue(result)
if(__name__=="main"):
    unittest.main()