import unittest
import application
class TestApplication(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(application.addition(5, 3), 8)
    def test_subtraction(self):
        self.assertEqual(application.subtraction(5, 3), 2)
    def test_multiplication(self):
        self.assertEqual(application.multiplication(5, 3), 15)
    def test_division(self):
        self.assertEqual(application.division(6, 3), 2)
        self.assertEqual(application.division(5, 0), 'Cannot divide by zero')
