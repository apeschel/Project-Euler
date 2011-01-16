if __name__ == "__main__":
  a_range = range(2, 100 + 1)
  b_range = range(2, 100 + 1)

  terms = set([a**b for a in a_range for b in b_range])
  print(len(terms))
