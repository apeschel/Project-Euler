#!/usr/bin/env python

from eulerfuncs import isPrime

if __name__ == '__main__':
  primes = [2]
  n = 3
  while len(primes) < 10001:
    if isPrime(n):
      primes.append(n)
    n += 2
  print(primes[10000])
