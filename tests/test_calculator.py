import unittest

from calculator import *


class TestCalculator(unittest.TestCase):
    def test_add_number(self):
        # test if input increases total correct

        calc = Calculater()

        calc.add(25)
        self.assertEqual(calc.total, 25)

        calc.subtract(5)
        self.assertEqual(calc.total, 20)

        calc.divide(4)
        self.assertEqual(calc.total, 5)

        calc.multiply(5)
        self.assertEqual(calc.total, 25)

    def test_should_not_divide_by_zero(self):
        calc = Calculater()
        calc.total = 50

        self.assertRaises(ZeroDivisionError, calc.divide, 0)

    def test_type(self):
        calc = Calculater()

        self.assertRaises(TypeError, calc.add, [])
        self.assertRaises(TypeError, calc.multiply, True)
        self.assertRaises(TypeError, calc.subtract, "")
