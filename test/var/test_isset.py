import unittest
from pynvg.var import isset

class issetTestCase(unittest.TestCase):

    def test_isset(self):
       	a=173
        self.assertTrue(isset(a))

    def test_isntset(self):
        self.assertFalse(isset(b))

if(__name__=="main"):
    unittest.main()