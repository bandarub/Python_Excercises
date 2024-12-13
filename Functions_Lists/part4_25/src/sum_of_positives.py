def sum_of_positives(vals):
  sum = 0
  for num in vals:
    if(num>0):
      sum = sum + num
  return sum

if __name__ == "__main__":
  result = sum_of_positives([1, -2, 3, -4, 5])
  print("The result is", result)
