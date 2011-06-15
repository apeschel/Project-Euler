from math import factorial

if __name__ == '__main__':
  num = factorial(100)
  sum = 0
  while num > 0:
    sum += num % 10
    num //= 10
  print(sum)
