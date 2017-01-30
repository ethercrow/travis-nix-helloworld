
import unittest

import lib

class TestFactorial(unittest.TestCase):
    def test_0(self):
        self.assertEqual(lib.factorial(0), 1)
    def test_5(self):
        self.assertEqual(lib.factorial(5), 120)
    def test_7(self):
        self.assertEqual(lib.factorial(7), 5040)

if __name__ == '__main__':
    unittest.main()
