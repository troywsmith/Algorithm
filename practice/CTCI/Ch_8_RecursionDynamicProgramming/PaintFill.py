from collections import deque


def findComponentCells(grid, r, c, color):
    cells = set()

    # Traverse grid cells that are equal to color
    queue = deque()
    queue.append((r, c))

    # Do not visit same cell twice
    visited = set()

    while queue:
        cell = queue.pop()
        row = cell[0]
        col = cell[1]

        # Find cells adjacent cells
        if col > -1:
            leftPos = (row, col-1)
            left = grid[row][col-1]
            if left and left == color and leftPos not in visited:
                cells.add(leftPos)
                visited.add(leftPos)
                queue.append(leftPos)

        if row > -1:
            abovePos = (row-1, col)
            above = grid[row-1][col]
            if grid[abovePos[0]][abovePos[1]] and above == color and abovePos not in visited:
                cells.add(abovePos)
                visited.add(abovePos)
                queue.append(abovePos)

        if col <= len(grid)-2:
            rightPos = (row, col+1)
            right = grid[row][col+1]
            if right and right == color and rightPos not in visited:
                cells.add(rightPos)
                visited.add(rightPos)
                queue.append(rightPos)

        if row <= len(grid[0]):
            belowPos = (row+1, col)
            below = grid[row+1][col]
            if grid[belowPos[0]][belowPos[1]] and below == color and belowPos not in visited:
                cells.add(belowPos)
                visited.add(belowPos)
                queue.append(belowPos)

    return cells


def changeCellColor(grid, point, color):
    init_color = grid[point[0]][point[1]]
    component_cells = findComponentCells(grid, point[0], point[1], init_color)

    for cell in component_cells:
        grid[cell[0]][cell[1]] = color


if __name__ == '__main__':
    grid = [[0 for x in range(5)] for x in range(5)]
    colored_cells = [(0, 4), (1, 2), (1, 3), (1, 4),
                     (2, 3), (3, 1), (3, 2), (3, 3)]

    for cell in colored_cells:
        grid[cell[0]][cell[1]] = 2

    print('Image BEFORE Paint Fill')
    for row in grid:
        print(row)

    point = (2, 3)
    color = 3
    changeCellColor(grid, point, color)

    print('Image AFTER Paint Fill')
    for row in grid:
        print(row)

else:
    print('Importing: Path Fill Algorithm')