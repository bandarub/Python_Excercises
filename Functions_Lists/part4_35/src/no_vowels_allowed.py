def no_vowels(str):
    vowels = 'aeiou'
    return ''.join(char for char in str if char not in vowels)


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))