#!/usr/bin/env python

from eulerfuncs import isPrime
from itertools import count

A_MAX, B_MAX = 1000, 1000

def countPrimes(a, b):
  for n in count(0):
    if not isPrime(n**2 + a*n + b):
      return n

if __name__ == "__main__":
  max = 0, 0, 0

  for a in range(-A_MAX + 1, A_MAX):
    for b in range(-B_MAX + 1, B_MAX):
      if countPrimes(a, b) > max[0]:
        max = countPrimes(a, b), a, b

  print('{0} primes, a = {1}, b = {2}'.format(max[0], max[1], max[2]))
