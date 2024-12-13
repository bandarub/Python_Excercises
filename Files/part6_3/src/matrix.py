def read_matrix_from_file():
   with open("matrix.txt", "r") as file:
      matrix = [list(map(int, line.strip().split(','))) for line in file]
      return matrix

def matrix_sum():
  matrix = read_matrix_from_file()
  total_sum = sum(sum(row) for row in matrix)  # Sum of all elements in the matrix
  return total_sum

def matrix_max():
  matrix = read_matrix_from_file()
  max_value = max(max(row) for row in matrix)  # Maximum value in all rows
  return max_value

def row_sums():
    matrix = read_matrix_from_file()
    return [sum(row) for row in matrix]  # List of sums, one per row
   
  

if __name__ == "__main__":
   print(matrix_sum())
   print(matrix_max())
   print(row_sums())
