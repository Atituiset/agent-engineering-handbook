import unittest

from solution import roman_to_int

class T(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)
        self.assertEqual(roman_to_int("XLII"), 42)
    def test_invalid(self):
        for s in ["IIII", "VV", "IC", ""]:
            with self.assertRaises(ValueError):
                roman_to_int(s)
