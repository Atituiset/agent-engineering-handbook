import unittest

from solution import parse_duration

class T(unittest.TestCase):
    def test_hm(self):
        self.assertEqual(parse_duration("1h30m"), 5400)
