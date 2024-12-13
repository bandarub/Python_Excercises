def longest_series_of_neighbours(list):
    max_length = 0
    current_length = 0

    for i in range(1, len(list)):
        if abs(list[i] - list[i - 1]) == 1:
            current_length += 1
        else:
            max_length = max(max_length, current_length + 1) 
            current_length = 0

    max_length = max(max_length, current_length + 1)

    return max_length


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))