def is_valid(board, row, col, num):
    # Check if the number is already used in the row
    if num in board[row]:
        return False

    # Check if the number is already used in the column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number is already used in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


def solve_sudoku(board):
    empty_cell = find_empty_cell(board)

    if not empty_cell:
        return True  # Puzzle solved

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True  # Puzzle solved

            board[row][col] = 0  # Backtrack if the current configuration doesn't work

    return False  # No solution found


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))


# Example Sudoku puzzle
example_board = [
    [0, 0, 2, 0, 0, 0, 8, 0, 0],
    [0, 5, 9, 0, 0, 1, 6, 0, 7],
    [0, 0, 0, 4, 0, 3, 0, 0, 0],
    [0, 0, 4, 0, 5, 0, 2, 6, 9],
    [0, 0, 0, 6, 3, 7, 0, 5, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 6, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 9, 0, 0, 1]
]

print("Sudoku puzzle:")
print_board(example_board)
print("\nSolving...\n")

if solve_sudoku(example_board):
    print("Solution:")
    print_board(example_board)
else:
    print("No solution exists.")
