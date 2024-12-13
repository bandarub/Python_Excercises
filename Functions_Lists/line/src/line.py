def line(times, str):
    if str == "":
      print("*"*times)
    else:
      print(str[0]*times)

if __name__ == "__main__":
   line(7, "%")
   line(10, "LOL")
   line(3, "")
   