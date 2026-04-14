# https://github.com/samfreitag18-ai/lab11-SF
# Partner 1: Samuel Freitag
# Partner 2: No one reached out :(

import unittest
import calculator


class TestCalculator(unittest.TestCase):

    # Partner 2 tests
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(10, 100), 2.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)

    # Partner 1 tests
    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(calculator.divide(2, 10), 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 8)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(9), 3.0)


if __name__ == "__main__":
    unittest.main()