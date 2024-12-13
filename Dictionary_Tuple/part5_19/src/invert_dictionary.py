def invert(dictionary: dict):
    obj = {}
    for key in dictionary:
        obj[dictionary[key]] = key

    dictionary.clear()
    dictionary.update(obj)
    

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)