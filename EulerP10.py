#!/usr/bin/env python

from EulerP7 import isPrime
from functools import reduce

if __name__ == '__main__':
  primes = [2]
  for n in range(3, 2000000, 2):
    if isPrime(n):
      primes.append(n)
  sum = reduce(lambda x, y: x + y, primes)
  print(sum)
