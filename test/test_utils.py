import unittest
from src.utils import get_array_length, get_first_element


class TestUtils(unittest.TestCase):
    def test_get_first_element(self):
        test_values = ["foo", "bar", "biz", "bap"]
        test = get_first_element(array=test_values)
        self.assertEqual(test, "foo")

    def test_get_array_length(self):
        test_values = ["foo", "bar", "biz", "bap"]
        test = get_array_length(array=test_values)
        self.assertEqual(test, 4)
