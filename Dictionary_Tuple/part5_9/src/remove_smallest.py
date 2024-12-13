def remove_smallest(numbers: list):
    smallest_index = numbers.index(min(numbers));
    numbers.pop(smallest_index)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5, 0, -9]
    remove_smallest(numbers)
    print(numbers)