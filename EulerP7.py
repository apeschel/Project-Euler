import math

def isPrime(n):
  ''' Returns True if input is prime.
      Returns False if input is not prime.'''
  if n <= 1:
    return False

  if n % 2 == 0:
    if n == 2:
      return True
    else:
      return False

  max = math.ceil(math.sqrt(n))
  for d in range(3, max + 1, 2):
    if n % d == 0:
      return False

  return True 

if __name__ == '__main__':
  primes = [2]
  n = 3
  while len(primes) < 10001:
    if isPrime(n):
      primes.append(n)
    n += 2
  print(primes[10000])
