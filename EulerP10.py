#!/usr/bin/env python

from eulerfuncs import isPrime

if __name__ == '__main__':
  primes = [2]
  for n in range(3, 2000000, 2):
    if isPrime(n):
      primes.append(n)
  total = sum(primes)
  print(total)
