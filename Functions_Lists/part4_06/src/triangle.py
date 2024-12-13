def line(times, str):
    if str == "":
      print("*"*times)
    else:
      print(str[0]*times)

def triangle(len):
  times = 1
  while True:
    line(times, "#")
    times += 1
    if times > len:
      break


if __name__ == "__main__":
    triangle(6)
    print()
    triangle(3)
