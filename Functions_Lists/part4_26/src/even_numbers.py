def even_numbers(vals):
  new = []
  for num in vals:
    if num % 2 == 0:
      new.append(num)
  return new

if __name__ == "__main__":
  my_list = [1, 2, 3, 4, 5]
  new_list = even_numbers(my_list)
  print("original",my_list)
  print("new",new_list)
