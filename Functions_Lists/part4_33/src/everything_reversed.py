def everything_reversed(list):
    return [s[::-1] for s in reversed(list)]


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)     