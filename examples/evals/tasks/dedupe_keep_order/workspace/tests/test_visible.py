import unittest

from solution import dedupe_keep_order

class T(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(sorted(dedupe_keep_order([1, 2, 1])), [1, 2])
