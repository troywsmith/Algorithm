GRID_SIZE = 8


def place_queens(positions, row):
    global solutions

    # Base Case
    if row >= GRID_SIZE:
        print(positions)

    else:

        # Try to place a queen for all N columns positions
        for col in range(GRID_SIZE):

            # Reject invalid positions
            if is_valid(positions, row, col):

                # If it is a valid placement, add it to the list
                positions[row] = col

                # Do the same for the next row
                place_queens(positions, row + 1)


def is_valid(positions, occupied_rows, column):
    """ 
    Check if a given position is elible (w/ row, col, diag conditions)
    """
    # Try all possible rows smaller than curr_row
    for i in range(occupied_rows):

        if positions[i] == column:
            return False

        if positions[i] - i == column - occupied_rows:
            return False

        if positions[i] + i == column + occupied_rows:
            return False

    return True


if __name__ == '__main__':

    # # For each queens starting row, we will store the col positions for all the queens
    # results = []

    # We will store the column of each queens positions for the current row
    # index is row, element is col
    positions = [-1] * GRID_SIZE

    # We will start at the first row (and finish after row 7)
    place_queens(positions, 0)
