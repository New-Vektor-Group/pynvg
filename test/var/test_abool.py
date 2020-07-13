import unittest
from pynvg.var import abool

class ABoolTestCase(unittest.TestCase):

    def test_aboolTrue(self):
        result=abool(True)
        self.assertTrue(result)

    def test_aboolFalse(self):
        result=abool(False)
        self.assertFalse(result)

    def test_aboolOne(self):
        result=abool(1)
        self.assertTrue(result)

   	def test_aboolTextTrue(self):
        result=abool("Hello World")
        self.assertTrue(result)

    def test_aboolTextFalse(self):
        result=abool("")
        self.assertFalse(result)

if(__name__=="main"):
    unittest.main()