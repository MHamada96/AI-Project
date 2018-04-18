import copy





def get_board(size=8):
    """Returns an n by n board"""
    board = [0] * size
    for ix in range(size):
        board[ix] = [0] * size
    return board


def print_solutions(solutions ,size=8):
    """Prints all the solutions in user friendly way"""
    for sol in solutions:
        for row in sol:
            print(row)
        print()


def is_safe(board ,row ,col ,size=8):
    """Check if it's safe to place a queen at board[x][y]"""

    # check row on left side
    for iy in range(col):
        if board[row][iy] == 1:
            return False

    ix = row
    iy = col
    while ix >= 0 and iy >= 0:
        if board[ix][iy] == 1:
            return False
        ix -= 1
        iy -= 1

    jx ,jy = row ,col
    while jx < size and jy >= 0:
        if board[jx][jy] == 1:
            return False
        jx += 1
        jy -= 1

    return True


def solve(board ,col ,size):
    """Use backtracking to find all solutions"""
    # base case
    if col >= size:
        return

    for i in range(size):
        if is_safe(board ,i ,col ,size):
            board[i][col] = 1
            if col == size - 1:
                add_solution(board)
                board[i][col] = 0
                return
            solve(board ,col + 1 ,size)
            # backtrack
            board[i][col] = 0


def add_solution(board):
    """Saves the board state to the global variable 'solutions'"""
    global solutions

    solutions.append( copy.deepcopy(board))




board = get_board(8)

solutions = []

solve(board ,0 ,8)

print_solutions(solutions ,8)

print("Total solutions = {}".format(len(solutions)))