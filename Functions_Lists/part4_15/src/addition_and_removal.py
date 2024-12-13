listVals = []

print(f"The list is now {listVals}")

while True:
  val = input("a(d)d, (r)emove or e(x)it:")
  if val == "d":
    if listVals:
      listVals.append(listVals[-1] + 1)
    else:
      listVals.append(1)
    print(f"The list is now {listVals}")
  elif val == "r":
    listVals.pop()
    print(f"The list is now {listVals}")
  else:
    print("Bye!")
    break
