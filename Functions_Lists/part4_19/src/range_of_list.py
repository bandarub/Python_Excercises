def range_of_list(values):
    if not values:
        return 0
    return max(values) - min(values)



if __name__ == "__main__":
  result = range_of_list([1, 2, 3, 4, 15])
  print("The range of the list is", result)


  