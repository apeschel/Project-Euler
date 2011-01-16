from math import floor, ceil, sqrt 

'''
Returns the smallest divisor of n greater than 1.
'''
def smallest_divisor(n):
  if n == 1:
    return None
  for d in range(2, ceil(sqrt(n) + 1)):
    if n % d == 0:
      return d
  return n


'''
def proper_divisors(n):
  result = [1]
  d = smallest_divisor(n)
  while d < n:
    cur = d 
    while n % d == 0:
      n //= d
      result.append(cur)
      if n != cur:
        result.append(n)
      cur *= d
    d += 1
  return result
'''

def proper_divisors(n):
  result = [1]
  if n == 1:
    return result

  d = smallest_divisor(n)
  for d in range(d, n // d + 1):
    if n % d == 0:
      result.append(d)
  return result

def is_abundant(n):
  divs = proper_divisors(n)

  if sum(divs) > n:
    return True
  else:
    return False

'''
def abun(n):
  ab_nums = []

  for i in range(1,21000):
    if is_abundant(i):
      ab_nums.append(i)

  return ab_nums
'''

def abun(N):
  Q = dict.fromkeys(range(1, N+1), 0) 
  for q in Q:
    for k in [q*n for n in range(1, N//q+1)]:
      if q != k: 
        Q[k] += q
  return [q for q in Q if Q[q] > q]

if __name__ == "__main__":
  N = 20161
  ab_nums = abun(N)
  is_ab = (N+1) * [False]

  for i in ab_nums:
    is_ab[i] = True

  result = []
  for j in range (1,N):
    for num in ab_nums:
      if num > j:
        result.append(j)
        break
      elif is_ab[j - num]:
        break;

  print(sum(result))
