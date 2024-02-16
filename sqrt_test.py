def test_true(): assert True
from app import square_root
def test_square_root():
  assert square_root(4) == 2.0
def test_factorial():
  assert factorial(5) == 120
def test_factorial_zero():
  assert factorial(0) == 1
import pytest
def main():
  pytest.main()
if __name__ == '__main__':
  main()
