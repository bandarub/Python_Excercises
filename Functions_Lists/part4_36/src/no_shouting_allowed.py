def no_shouting(list):
    updatedList = []
    for str in list:
        if not str.isupper():
            updatedList.append(str)

    return updatedList


if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)