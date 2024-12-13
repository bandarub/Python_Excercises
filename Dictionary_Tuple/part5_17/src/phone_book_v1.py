# Initialize the dictionary outside the loop so it persists
obj = {}

while True:
    n = int(input("command (1 search, 2 add, 3 quit): "))
    
    if n == 3:
        print("quitting...")
        break
        
    elif n == 2:
        # Add a new contact
        name = input("name: ")
        number = input("number: ")
        obj[name] = number
        print("ok!")
        
    elif n == 1:
        # Search for a contact
        name = input("name: ")
        if name in obj:
            print(obj[name])  # Print the number if the name exists
        else:
            print("no number")  # Print if the name doesn't exist in the dictionary
