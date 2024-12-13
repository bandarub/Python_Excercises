def palindromes(word):
    normalized_word = word.replace(" ", "").lower()
    return normalized_word == normalized_word[::-1]
    

while True:
  user_input = input("Please type in a palindrome: ")
  if palindromes(user_input):
    print(f"{user_input} is a palindrome!")
    break
  else:
    print("that wasn't a palindrome")
