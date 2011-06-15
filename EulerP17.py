def genWordFromNum(n):
  num_word = {0:'zero',
              1:'one',
              2:'two',
              3:'three',
              4:'four',
              5:'five',
              6:'six',
              7:'seven',
              8:'eight',
              9:'nine',
              10:'ten',
              11:'eleven',
              12:'twelve',
              13:'thirteen',
              14:'fourteen',
              15:'fifteen',
              16:'sixteen',
              17:'seventeen',
              18:'eighteen',
              19:'nineteen',
              20:'twenty',
              30:'thirty',
              40:'forty',
              50:'fifty',
              60:'sixty',
              70:'seventy',
              80:'eighty',
              90:'ninety',
              100:'hundred',
              1000:'thousand'}

  if n == 1000:
    return num_word[1] + num_word[1000]

  if n % 100 == 0:
    return num_word[n // 100] + num_word[100]

  result = ''

  num = n % 10
  n //= 10
  if num == 0:
    num = 10 * (n % 10)
  elif n % 10 == 1:
    num += 10 * (n % 10)
  elif n % 10 > 1:
    result = num_word[num]
    num = 10 * (n % 10)
  result = num_word[num] + result

  n //= 10
  num = n % 10
  if num > 0:
    result = num_word[num] + num_word[100] + 'and' + result

  return result

if __name__ == '__main__':
  sum = 0
  for n in range(1, 1000 + 1):
    sum += len(genWordFromNum(n))
  print(sum)
