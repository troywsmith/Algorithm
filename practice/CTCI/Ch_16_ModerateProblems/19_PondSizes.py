"""
You have an integer matrix representing a plot of land, where the value at that location represents the height above sea level.
A value of zero indicates water.
A pond is a region of water connected horizontally, vertically, or diagonally.
The size of the pond is the total number of connected water cells.
Write a method to compute the sizes of ALL ponds in the matrix

Thoughts:
- Strongly connected components
- BFS
"""

from collections import deque


def find_pond_size(matrix, start):

    size = 0
    q = deque()
    q.append(start)

    while q:

        size += 1

        cell = q.pop()
        r = cell[0]
        c = cell[1]

        # Checking adjacent cells and adding them to q if they are water and inbounds and havent been seen
        adj_cells = [(r-1, c), (r+1, c),
                     (r, c-1), (r, c+1),
                     (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]

        for adj_cell in adj_cells:
            r, c = adj_cell[0], adj_cell[1]
            if r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[r]) and matrix[r][c] == 0:
                q.append(adj_cell)

        # Add current cell to seen
        matrix[cell[0]][cell[1]] = -1

    print(start, size)
    return size


def main(matrix):
    """
    Time Complexity: O(WH) where W is the width and H is the height of the matrix
    Space Complexity: O(1)
    """
    sizes = []

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                size = find_pond_size(matrix, (r, c))
                sizes.append(size)

    return sizes


if __name__ == '__main__':

    matrix = [
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1],
    ]
    print(main(matrix))
