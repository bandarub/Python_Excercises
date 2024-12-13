def mean(values):
    if not values:
        return 0
    return sum(values) / len(values)


if __name__ == "__main__":
  result = mean([1, 2, 3, 4, 5])
  print("mean value is", result)