digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def all_perms(ls):
  if len(ls) == 1:
    yield ls
  else:
    for perm in all_perms(ls[1:]):
      for i in range(len(perm) + 1):
        yield perm[:i] + ls[0:1] + perm[i:]

if __name__ == "__main__":
  perms = sorted([int(''.join(p)) for p in all_perms(digits)])
  print(perms[1000000 - 1])
