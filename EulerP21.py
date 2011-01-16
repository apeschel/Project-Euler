from EulerP12 import findDivisors
from functools import reduce

def findProperDivs(x):
  x_divs = findDivisors(x)
  x_divs.remove(x)
  if len(x_divs) == 0:
    return [0]
  else:
    return x_divs


def isAmicableNumber(a):
  b = reduce(lambda x, y: x + y, findProperDivs(a))
  b_sum = reduce(lambda x, y: x + y, findProperDivs(b))

  if a == b_sum and not a == b:
    return True
  else:
    return False


if __name__ == '__main__':
  sum = 0

  for a in range(1, 10000):
    if isAmicableNumber(a):
      sum += a

  print(sum)
