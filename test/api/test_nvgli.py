import unittest
from pynvg.api import nvgli

class NVGLiTestCase(unittest.TestCase):

    def test_nvgli(self):
        url = "nvg-grou.com";
        result="https://nvg.li/nvg";

        test=nvgli(url);
        self.assertEqual(test,result)

if(__name__=="main"):
    unittest.main()