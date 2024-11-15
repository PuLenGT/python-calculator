import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-4, -6), -10)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), -2)
        self.assertEqual(self.calc.subtract(2, 4), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(8, 5), -3)

    def test_subtract_with_negative_result(self):
        self.assertEqual(self.calc.subtract(5, 8), 3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 3), -3)
        self.assertEqual(self.calc.multiply(0, 3), 0)

    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(7, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(5, 10), 0)  

    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_when_dividend_is_smaller(self):
        self.assertEqual(self.calc.divide(3, 5), 0)  

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(9, 3), 0)
        self.assertEqual(self.calc.modulo(5, 10), 5)

    def test_modulo_with_remainder(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_when_divisible(self):
        self.assertEqual(self.calc.modulo(9, 3), 0)

if __name__ == '__main__':
    unittest.main()
