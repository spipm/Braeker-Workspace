import unittest
from source_code.main import add, subtract, multiply
class TestMain(unittest.TestCase): def test_add(self): self.assertEqual(add(5, 7), 12)
def test_subtract(self): self.assertEqual(subtract(10, 5), 5)
def test_multiply(self): self.assertEqual(multiply(3, 7), 21)
if __name__ == '__main__': unittest.main()
