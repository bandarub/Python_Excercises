listVals = [1, 2, 3, 4, 5]

while True:
  i = int(input("Index:"))
  if i == -1 or i < 0 or i > len(listVals) - 1:
    break
  newVal = int(input("New value:"))
  listVals[i] = newVal
  print(listVals)


