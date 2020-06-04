def maxIncreaseKeepingSkyline(grid):
    num_rows = len(grid)
    num_columns = len(grid[0])

    side_view = []
    for i in range(num_rows):
        side_view.append(max(grid[i]))
    print(side_view)

    top_view = []
    for j in range(num_columns):
        max0 = 0
        for i in range(num_rows):
            if grid[i][j] > max0:
                max0 = grid[i][j]
        top_view += [max0]

    total = 0
    for i in range(num_rows):
        for j in range(num_columns):
            total += min(side_view[i], top_view[j])-grid[i][j]
    
    return total


grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
print(maxIncreaseKeepingSkyline(grid))