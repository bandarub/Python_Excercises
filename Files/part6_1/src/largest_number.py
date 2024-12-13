def largest():
  with open("numbers.txt") as new_file:
    numbers = []
    for line in new_file:
      numbers.append(int(line.strip()))
    
    return max(numbers) if numbers else None
  

if __name__ == "__main__":
   print(largest())