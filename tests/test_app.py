import unittest
from source_code.app import add, subtract, multiply, divide
class TestApp(unittest.TestCase):
    def test_add(self):
        result = add(10, 5)
        self.assertEqual(result, 15)
    def test_subtract(self):
        result = subtract(10, 5)
        self.assertEqual(result, 5)
    def test_multiply(self):
        result = multiply(10, 5)
        self.assertEqual(result, 50)
    def test_divide(self):
        result = divide(10, 5)
        self.assertEqual(result, 2)
