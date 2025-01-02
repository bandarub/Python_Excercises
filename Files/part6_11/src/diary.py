def save_entry(entry: str):
    with open("diary.txt", "a") as my_file:
        my_file.write(f"{entry}\n")

def read_entries():
    try:
        with open("diary.txt", "r") as my_file:
            return my_file.readlines()
    except FileNotFoundError:
        return []


while True:
    entries = read_entries()
    print("1 - add an entry, 2 - read entries, 0 - quit")
    choice = int(input("Function: "))
    if choice == 0:
        print("Bye now!")
        break
    elif choice == 1:
        entry = input("Diary entry: ")
        save_entry(entry) 
        print("Diary saved")
    elif choice == 2:
        print("Entries:")
        for line in entries:
            print(line.strip())