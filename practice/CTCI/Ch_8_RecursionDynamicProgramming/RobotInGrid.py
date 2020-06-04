def printGrid(grid):
    for row in grid:
        print(row)
    print(' ')


# def guideRobot(grid):

#     grid = [['O' for x in range(n)] for c in range(m)]
#     grid[0][0] = 'R'
#     grid[0][2] = 'X'
#     grid[1][0] = 'X'
#     grid[2][0] = 'X'
#     grid[3][3] = 'X'
#     grid[4][2] = 'X'

#     printGrid(grid)

#     r = 0
#     c = 0
#     while r+1 < n and c+1 < m:
#         grid[r][c] = 'R'

#         if grid[-1][-1] == 'R':
#             print('robot has reached end')
#             return

#         down = grid[r+1][c]
#         right = grid[r][c+1]

#         # Check down
#         if down == 'O' and down:
#             grid[r][c] == 'O'
#             r += 1

#             if right == 'O' and right:
#                 grid[r][c] == 'O'
#                 c += 1

#         # Check Right
#         elif right == 'O' and right:
#             grid[r][c] == 'O'
#             c += 1

#             if down == 'O' and down:
#                 grid[r][c] == 'O'
#                 r += 1

#         # If down and right are not possible, move robot right
#         else:
#             grid[r][c] == 'O'
#             r -= 1

#         printGrid(grid)

#     grid[r][c] = 'R'
#     printGrid(grid)


def getPath(grid):
    r = len(grid) - 1
    c = len(grid[0]) - 1

    if not grid or len(grid) == 0:
        return None

    path = []
    failed_points = set()

    if getPathHelper(grid, r, c, path, failed_points):
        return path

    return False


def getPathHelper(grid, r, c, path, failed_points):

    # Boundaries, etc
    if r < 0 or c < 0 or not grid[r][c]:
        return False

    p = grid[r][c]

    if p in failed_points:
        return False

    isAtOrigin = ((r, c) == (0, 0))

    if isAtOrigin or getPathHelper(grid, r, c-1, path, failed_points) or getPathHelper(grid, r-1, c, path, failed_points):
        path.append((r, c))
        return True

    return False


if __name__ == '__main__':

    n = 5
    m = 5

    grid = [[True for x in range(n)] for c in range(m)]
    grid[0][0] = True
    grid[0][2] = False
    grid[1][0] = False
    grid[2][0] = False
    grid[3][3] = False
    grid[4][2] = False

    print(getPath(grid))

else:
    print('Importing: Robot in Grid Algorithm')