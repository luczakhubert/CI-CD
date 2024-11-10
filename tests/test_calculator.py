import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Testy dla metody add
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_positive_and_negative(self):
        self.assertEqual(self.calc.add(2, -3), -1)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(2, 0), 2)

    # Testy dla metody subtract
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtract_positive_and_negative(self):
        self.assertEqual(self.calc.subtract(5, -3), 8)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # Testy dla metody multiply
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, -3), 12)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(self.calc.multiply(4, -3), -12)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(4, 0), 0)

    # Testy dla metody divide
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-6, -3), 2)

    def test_divide_positive_and_negative(self):
        self.assertEqual(self.calc.divide(6, -3), -2)

    def test_divide_by_one(self):
        self.assertEqual(self.calc.divide(6, 1), 6)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            self.calc.divide(6, 0)


if __name__ == "__main__":
    unittest.main()
