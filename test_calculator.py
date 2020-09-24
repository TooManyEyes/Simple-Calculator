import unittest
from simple_calculator import Calculator
import time
import random


class TestCalculator(unittest.TestCase):

    def setUp(self):
        print('Set_up test begin:', time.asctime())
        self.calculator = Calculator(random.randint(1, 1000))
        print('Set_up test end:', time.asctime(), '\n --------------')

    def test_add(self):
        print('test_add begin:', time.asctime())
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(1, 2, 3).value, calc_value + 6)
        print('test_add end:', time.asctime(), '\n --------------')

    def test_mul(self):
        print('test_mul begin:', (time.asctime()))
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.multiply(5, 2, 90).value, calc_value * 900)
        print('test_mul end:', time.asctime(), '\n --------------')

    def test_divide(self):
        print('test_divide begin:', time.asctime())
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.divide(2, 3).value, calc_value / 6)
        print('test_divide end:', time.asctime(), '\n --------------')

    def test_power(self):
        print('test_power begin:', time.asctime())
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(2, 3).value, calc_value ** 6)
        print('test_power end:', time.asctime(), '\n --------------')

    def test_power_long(self):
        print('test_power_long begin:', time.asctime())
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(2, 3, 3, 4, 4, 5).value, calc_value ** 1440)
        print('test_root_long end:', time.asctime(), '\n --------------')

    def test_power_smaller(self):
        print('test_power_smaller begin:', time.asctime())
        calc_value = self.calculator.value
        self.assertLessEqual(self.calculator.power(10, 2).value, calc_value ** 100)
        print('test_power_smaller end:', time.asctime(), '\n --------------')

    def test_root_zero(self):
        print('test_root_zero begin:', time.asctime())
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(0).value, calc_value)
        print('test_root_zero end:', time.asctime(), '\n --------------')

    def test_power_zero(self):
        print('test_root_zero begin:', time.asctime())
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(0).value, 1)
        print('test_root_zero end:', time.asctime(), '\n --------------')

    def test_root(self):
        print('test_root begin:', time.asctime())
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(2, 3).value, calc_value ** (1/6))
        print('test_root end:', time.asctime(), '\n --------------')
        print('Использованное число:', calc_value)


if __name__ == '__main__':
    unittest.main()
