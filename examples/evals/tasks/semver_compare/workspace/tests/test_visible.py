import unittest

from solution import semver_compare

class T(unittest.TestCase):
    def test_core(self):
        self.assertEqual(semver_compare("1.2.3", "1.10.0"), -1)
