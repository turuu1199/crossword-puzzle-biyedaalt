
# Asuudal
problem_puzzle = [
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
def solve_puzzle(puzzle):
    empty_cells  = find_empty_cell(puzzle)
    for i in range(len(empty_cells)):
        for num in range(1, 9):
            row, col = empty_cells[i]
            puzzle[row][col] = num


def find_empty_cell(puzzle):
    empty_cells = []
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                empty_cells.append((i,j))
    return empty_cells

def is_valid(row,col,board,num):
    return None

solve_puzzle(problem_puzzle)