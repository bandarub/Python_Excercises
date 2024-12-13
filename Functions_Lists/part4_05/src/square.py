def line(times, str):
    if str == "":
      print("*"*times)
    else:
      print(str[0]*times)

def square(len, str):
  times = len
  while True:
    line(len, str)
    times -= 1
    if times == 0:
      break


if __name__ == "__main__":
    square(5, "*")
    print()
    square(3, "o")
