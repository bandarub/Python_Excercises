def histogram(s: str):
    letter_count = {}
    for char in s.lower():
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    for letter in letter_count:
        print(f"{letter} {'*' * letter_count[letter]}")
    

if __name__ == "__main__":
    histogram("statistically")
