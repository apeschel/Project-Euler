from math import factorial

def N(p,q):
  sum = 0
  for n in range(q + 1):
    sum += T(n, p) * (p ** n)
  return sum


def T(n, p):
  return S(n) % p


def S(n):
  result = 0
  for i in range(n + 1):
    if i == 0:
      result = 290797
    else:
      (result ** 2) % 50515093
  return result


def Nfac(p,q):
  return factorial(N(p,q))


if __name__ == '__main__':
  print(N(3, 10000))
