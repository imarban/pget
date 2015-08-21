import unittest
from client import get_size

__author__ = 'igomez'


class TestGetSize(unittest.TestCase):
    def test_existent_file(self):
        self.assertEqual(get_size("LICENSE"), 11358)

    def test_no_existent_file(self):
        self.assertEqual(get_size("LICENSE1"), 0)
