from math import log, floor

def fib(n):
 return fib2(n-1)[0]

def fib2(n):
  if n == 0:
    return 1, 1
  elif n == 1:
    return 1, 2
  else:
    a, b = fib2(n // 2 - 1)
    c = a + b
    if n % 2 == 0:
      return a*a + b*b, c*c - a*a
    else:
      return c*c - a*a, b*b + c*c

if __name__ == "__main__":
  GOAL = 10**999
  n = floor(999*log(10))

  while fib(n) < GOAL:
    n += 1

  print(n)
