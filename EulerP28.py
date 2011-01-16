N = 1001 

if __name__ == "__main__":
  # Start with center already considered.
  sum = 1 # total sum
  val = 1 # value of current location
  step = 2 # step size betwen locations

  for _ in range((N-1)//2):
    for _ in range(4):
      val += step
      sum += val
    step += 2

  print(sum)
