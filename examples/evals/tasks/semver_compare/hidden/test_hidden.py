import unittest

from solution import semver_compare

class T(unittest.TestCase):
    def test_core(self):
        self.assertEqual(semver_compare("1.2.3", "1.10.0"), -1)
    def test_equal(self):
        self.assertEqual(semver_compare("2.0.0", "2.0.0"), 0)
    def test_prerelease_lower(self):
        self.assertEqual(semver_compare("1.0.0-alpha", "1.0.0"), -1)
    def test_prerelease_order(self):
        self.assertEqual(semver_compare("1.0.0-alpha.2", "1.0.0-alpha.10"), -1)
        self.assertEqual(semver_compare("1.0.0-beta", "1.0.0-alpha.1"), 1)
