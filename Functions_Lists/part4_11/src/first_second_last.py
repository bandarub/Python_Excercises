def first_word(sen):
    return sen.split()[0]
def second_word(sen):
    return sen.split()[1]
def last_word(sen):
    return sen.split()[-1]


if __name__ == "__main__":
    sentence = "it was"
    print(second_word(sentence)) # was
    print(last_word(sentence)) # python