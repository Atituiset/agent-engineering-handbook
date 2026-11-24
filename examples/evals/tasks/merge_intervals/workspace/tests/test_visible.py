import unittest

from solution import merge_intervals

class T(unittest.TestCase):
    def test_overlap(self):
        self.assertEqual(merge_intervals([[1, 3], [2, 5]]), [[1, 5]])
