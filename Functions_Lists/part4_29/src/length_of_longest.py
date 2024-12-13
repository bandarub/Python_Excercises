def length_of_longest(list):
    if not list:
        return 0
    longest = max(len(s) for s in list)
    return longest


if __name__ == "__main__":
  my_list = ["first", "second", "fourth", "eleventh"]
  result = length_of_longest(my_list)
  print(result)