def line(times, str):
    if str == "":
      print("*"*times)
    else:
      print(str[0]*times)

def square_of_hashes(len):
  times = len
  while True:
    line(len, "#")
    times -= 1
    if times == 0:
      break


if __name__ == "__main__":
      square_of_hashes(5)
      print()
      square_of_hashes(3)
