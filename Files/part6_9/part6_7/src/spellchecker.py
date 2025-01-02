def load_dictionary(filename="wordlist.txt"):
  with open(filename, "r") as file:
    word_list = {line.strip().lower() for line in file}  # Lowercase for case-insensitive check
  return word_list

def spell_check(text, dictionary):
  words = text.split()
  corrected_text = []

  for word in words:
    clean_word = ''.join(char for char in word if char.isalnum())
    if clean_word.lower() not in dictionary:  # Case-insensitive check
      corrected_text.append(f"*{word}*")  # Add word with asterisks if misspelled
    else:
      corrected_text.append(word)

  return " ".join(corrected_text)


dictionary = load_dictionary("wordlist.txt")
text = input("Write text: ")
corrected_text = spell_check(text, dictionary)
print(corrected_text)