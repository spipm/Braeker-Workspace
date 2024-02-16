def add(x, y):
    """Add Function"""
    return x + y
def subtract(x, y):
    """Subtract Function"""
    return x - y
def multiply(x, y):
    """Multiply Function"""
    return x * y
def divide(x, y):
    """Divide Function"""
    if y != 0:
        return x / y
    else:
        return "Error, division by zero."
import math
def square_root(n):
  return math.sqrt(n)
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
