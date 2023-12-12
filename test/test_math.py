import unittest
from src.math import add, subtract, multiply, exponent


class TestMath(unittest.TestCase):
    def test_add(self):
        a = 10
        b = 5

        test = add(a, b)

        self.assertEqual(test, a + b)

    def test_subtract(self):
        a = 3
        b = 4

        test = subtract(a, b)

        self.assertEqual(test, a - b)

    def test_multiply(self):
        a = 6
        b = 7

        test = multiply(a, b)

        self.assertEqual(test, a * b)

    def test_exponent(self):
        a = 4
        b = 12

        test = exponent(a, b)

        self.assertEqual(test, a**b)


if __name__ == "__main__":
    unittest.main()
