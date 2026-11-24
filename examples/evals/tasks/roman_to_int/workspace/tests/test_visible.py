import unittest

from solution import roman_to_int

class T(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)
