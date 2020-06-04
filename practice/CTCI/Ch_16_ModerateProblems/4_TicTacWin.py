"""
Design an algorithm to figure out if someone has won a game of tic tac toe.
"""


def check_win(grid):

    for i in range(len(grid)):

        # Check rows
        if hasWinner(grid[i][0], grid[i][1], grid[i][2]):
            return True

        # Check columns
        if hasWinner(grid[0][i], grid[1][i], grid[2][i]):
            return True

        # Check topleft to bottomright diag
        if hasWinner(grid[0][0], grid[1][1], grid[2][2]):
            return True

        # Check bottomleft to topright diag
        if hasWinner(grid[2][0], grid[1][1], grid[0][2]):
            return True

    return False


def hasWinner(a, b, c):
    return a == b and b == c


grid = [
    ['X', 'X', 'O'],
    ['O', 'X', 'X'],
    ['X', 'O', 'O']
]
print(check_win(grid))
