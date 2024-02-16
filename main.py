def add_numbers(a, b):
    return a + b
def subtract_numbers(a, b):
    return a - b
def multiply_numbers(a, b):
    return a * b
def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError('Cannot divide by zero.')
import sys
if __name__ == '__main__':
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print('Add:', add_numbers(a, b))
    print('Subtract:', subtract_numbers(a, b))
    print('Multiply:', multiply_numbers(a, b))
    print('Divide:', divide_numbers(a, b))
def square_number(a):
    return a**2
