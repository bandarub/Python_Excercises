def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    seen = set()
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            if i < len(sudoku) and j < len(sudoku[i]):
                num = sudoku[i][j]
                if num != 0:
                    if num in seen:
                        return False
                    seen.add(num)
    return True

def sudoku_grid_correct(sudoku: list) -> bool:
    # Check all rows
    for row in sudoku:
        seen = set()
        for num in row:
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)

    # Check all columns
    for col in range(9):
        seen = set()
        for row in range(9):
            num = sudoku[row][col]
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)

    # Check all 3x3 blocks
    block_starts = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for (start_row, start_col) in block_starts:
        if not block_correct(sudoku, start_row, start_col):
            return False

    # If all checks pass
    return True

if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))