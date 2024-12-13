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
        if name in obj:
            obj[name].append(number)  # Append the number if name exists
        else:
            obj[name] = [number] 
        
        print("ok!")
        
    elif n == 1:
        # Search for a contact
        name = input("name: ")
        if name in obj:
            for num in obj[name]:
                print(num)
        else:
            print("no number")  # Print if the name doesn't exist in the dictionary
