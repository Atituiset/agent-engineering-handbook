import unittest

from solution import merge_intervals

class T(unittest.TestCase):
    def test_overlap(self):
        self.assertEqual(merge_intervals([[1, 3], [2, 5]]), [[1, 5]])
    def test_touching(self):
        self.assertEqual(merge_intervals([[1, 2], [2, 3]]), [[1, 3]])
    def test_unsorted(self):
        self.assertEqual(merge_intervals([[5, 6], [1, 2]]), [[1, 2], [5, 6]])
    def test_empty(self):
        self.assertEqual(merge_intervals([]), [])
