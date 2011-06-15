if __name__ == '__main__':
  num = 2 ** 1000 
  sum = 0
  while num > 0:
    digit = num % 10
    num //= 10
    sum += digit
  print(sum)
