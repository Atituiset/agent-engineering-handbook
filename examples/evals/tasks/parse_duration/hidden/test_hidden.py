import unittest

from solution import parse_duration

class T(unittest.TestCase):
    def test_hm(self):
        self.assertEqual(parse_duration("1h30m"), 5400)
    def test_seconds(self):
        self.assertEqual(parse_duration("90s"), 90)
    def test_all(self):
        self.assertEqual(parse_duration("1h1m1s"), 3661)
    def test_invalid(self):
        with self.assertRaises(ValueError):
            parse_duration("abc")
        with self.assertRaises(ValueError):
            parse_duration("")
