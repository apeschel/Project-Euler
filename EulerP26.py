from itertools import count

def recurring_cycle(d):
  dict = {}
  num = 1
  for n in count(0):
    if num == 0:
      return 0
    elif num in dict:
      return n - dict[num]
    else:
      dict[num] = n
      num = num*10 % d
   
if __name__ == "__main__":
  max, den = 0, 0

  for d in range(1, 1000):
    if recurring_cycle(d) > max:
      max, den = recurring_cycle(d), d

  print(den)
  
