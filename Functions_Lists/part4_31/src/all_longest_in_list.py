def all_the_longest(list):
    max_length = max(len(s) for s in list)
    longest_strings = [s for s in list if len(s) == max_length]
    
    return longest_strings


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)       