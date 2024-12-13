def longest(strings: list):
    return max(strings, key=len)


if __name__ == "__main__":
  my_list = ["first", "second", "fourth", "el"]
  result = longest(my_list)
  print(result)