import unittest
from main import add_numbers, subtract_numbers, multiply_numbers, divide_numbers
class TestMain(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)
    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(5, 2), 3)
    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)
    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(6, 2), 3)
    def test_divide_by_zero_error(self):
        with self.assertRaises(ValueError):
            divide_numbers(1, 0)
    def test_square_number(self):
        self.assertEqual(square_number(3), 9)
