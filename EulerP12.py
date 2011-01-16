from math import sqrt 
from math import ceil

def findDivisors(n):
  max = ceil(sqrt(n))
  divisors = [] 

  if max * max == n:
    divisors.append(max)

  for d in range(1, max):
    if n % d == 0:
      divisors.append(d)
      divisors.append(n // d)

  return divisors

def countDivisors(n):
  ''' Returns the number of divisors the given integer n has'''
  return len(findDivisors(n))

if __name__ == '__main__':
  i = 1
  num = 1 

  while countDivisors(num) <= 500:
    i += 1
    num += i

  print(num)
