def same_chars(str,i1,i2):
    if i1 >= len(str) or i1<0 or i2 >= len(str) or i2<0 :
        return False
    return str[i1] == str[i2]

if __name__ == "__main__":
    # same characters m and m
    print(same_chars("programmer", 6, 7)) # True

    # different characters p and r
    print(same_chars("programmer", 0, 4)) # False

    # the second index is not within the string
    print(same_chars("programmer", 0, 12)) # False