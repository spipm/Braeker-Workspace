def factorial(n, acc=1):
  return acc if n <= 1 else factorial(n-1, n*acc)
