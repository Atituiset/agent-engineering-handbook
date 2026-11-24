import unittest

from solution import slugify

class T(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello World"), "hello-world")
    def test_collapse(self):
        self.assertEqual(slugify("a -- b!!c"), "a-b-c")
    def test_strip(self):
        self.assertEqual(slugify("  --Agent Evals--  "), "agent-evals")
    def test_empty(self):
        self.assertEqual(slugify("!!!"), "")
