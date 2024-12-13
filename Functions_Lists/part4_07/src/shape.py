def line(times, str):
    if str == "":
      print("*"*times)
    else:
      print(str[0]*times)

def shape(tri, char, height, rect):
    times = 1
    times2 = height

    while True:
      line(times, char)
      times += 1
      if times > tri:
        break
    while True:
      if height == 0:
         break
      line(tri, rect)
      times2 -= 1
      if times2 <= 0:
        break
    



if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")