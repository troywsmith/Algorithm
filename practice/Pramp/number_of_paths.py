def num_of_paths_to_dest(n):

    if n <= 1:
        return n

    # Create a 2D table to store results of subproblems
    grid = [[0 for x in range(n)] for y in range(n)]

    # Set bottom row to 1
    for i in range(n):
        grid[n-1][i] = 1

    # Traverse from bottom left to top right
    for i in range(n-2, -1, -1):
        for j in range(1, n):

            # If i + j == n-1, only add bottom
            if i + j == n-1:
                grid[i][j] = grid[i+1][j]

            # Add cell under and cell to left
            else:
                grid[i][j] = grid[i+1][j] + grid[i][j-1]

    for row in grid:
        print(row)

    # Return count in end point
    return grid[0][n-1]


if __name__ == '__main__':
    n = 3
    print(num_of_paths_to_dest(n))
