import unittest
from pynvg.math import isPrime

class IsPrimeTestCase(unittest.TestCase):

    def test_isprime_true(self):
        result=isPrime(173)
        self.assertTrue(result)

    def test_isprime_false(self):
        result=isPrime(20)
        self.assertFalse(result)

    def test_isprime_negative(self):
        result=isPrime(-19)
        self.assertFalse(result)

if(__name__=="main"):
    unittest.main()