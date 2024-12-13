while True:
    mystring = input("Editor: ")

    if mystring.lower() == "visual studio code":
        print("an excellent choice!")
        break
    elif mystring.lower() in ["word", "notepad"]:
        print("awful")
    else:
        print("not good")
