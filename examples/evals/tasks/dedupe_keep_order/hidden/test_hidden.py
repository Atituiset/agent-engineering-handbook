import unittest

from solution import dedupe_keep_order

class T(unittest.TestCase):
    def test_order(self):
        self.assertEqual(dedupe_keep_order([3, 1, 3, 2, 1]), [3, 1, 2])
    def test_strings(self):
        self.assertEqual(dedupe_keep_order(list("banana")), ["b", "a", "n"])
