import re

def getNames():
  pattern = re.compile(r'"([^,"]+)"')
  with open('names.txt', encoding='utf-8') as file:
      str = file.readline()
      names = re.split('\W+', str)
      return sorted(names[1:-1]) # [1:-1] is to eliminate the empty strings added by split.


def nameValue(name):
  sum = 0
  for ch in name:
    sum += ord(ch) - ord('A') + 1
  return sum


if __name__ == '__main__':
  sum = 0
  names = getNames()
  for i in range(len(names)):
    value = nameValue(names[i]) * (i + 1)
    sum += value
  print(sum)
