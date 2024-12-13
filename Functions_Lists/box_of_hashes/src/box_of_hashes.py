def line(times, str):
    if str == "":
      print("*"*times)
    else:
      print(str[0]*times)

def box_of_hashes(count):
   times = count
   while True:
      line(10, "#")
      times -= 1
      if times == 0:
         break

if __name__ == "__main__":
   box_of_hashes(5)
   print()
   box_of_hashes(2)
