if __name__ == '__main__':
  num = 600851475143
  div = 3

  while div < num:
    while num % div == 0:
      num //= div
    div += 2
  
  print(num)
