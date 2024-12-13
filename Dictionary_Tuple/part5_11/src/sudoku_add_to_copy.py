def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = [row[:] for row in sudoku]  # This copies each row of the grid
    new_sudoku[row_no][column_no] = number
    return new_sudoku

def print_sudoku(sudoku: list):
    # Loop through each row of the sudoku grid
    for i, row in enumerate(sudoku):
        # Print a blank line between every third row (after rows 2, 5)
        if i % 3 == 0 and i != 0:
            print()  # Print a blank line
        
        # For each row, print the elements with a space between them
        row_str = " ".join(str(cell) if cell != 0 else '_' for cell in row)
        
        # Add vertical lines to separate the 3x3 blocks
        row_str = row_str[:6] + " " + row_str[6:12] + " " + row_str[12:]

        print(row_str)


if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)