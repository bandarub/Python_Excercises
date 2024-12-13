def read_fruits():
  fruits_dict = {}
  with open("fruits.csv", 'r') as file:
    for line in file:
      fruit, price = line.strip().split(';')
      fruits_dict[fruit] = float(price)
    
  return fruits_dict
  

if __name__ == "__main__":
  fruits = read_fruits()
  print(fruits)