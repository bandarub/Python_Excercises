def most_common_character(list):
    char_count = {}
    
    for char in list:
        char_count[char] = char_count.get(char, 0) + 1
    most_common = max(char_count, key=lambda k: (char_count[k], -list.index(k)))
    return most_common


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementaryxxxxx"
    print(most_common_character(second_string)) 