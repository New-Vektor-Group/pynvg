import unittest
from pynvg.math import isPrime

class IsPrimeTestCase(unittest.TestCase):

    def test_isprime_true(self):
        result=isPrime(173)
        self.assertTrue(result)

if(__name__=="main"):
    unittest.main()