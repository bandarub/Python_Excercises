def distinct_numbers(list):
  new = []
  for num in list:
    if num not in new:
      new.append(num)
  return sorted(new)


if __name__ == "__main__":
  my_list = [3, 2, 2, 1, 3, 3, 1]
  print(distinct_numbers(my_list))
