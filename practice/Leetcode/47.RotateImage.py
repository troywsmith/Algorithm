def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """

    # Reverse rows in place
    for r in range(len(matrix)):
        for c in range(len(matrix[r]) // 2):
            matrix[r][c], matrix[r][len(matrix[r])-1-c] = matrix[r][len(matrix[r])-1-c], matrix[r][c]

    # Swap diaganols
    for r in range(len(matrix)-1):
        for c in range(len(matrix[r])-1):
            matrix[r][c], matrix[len(matrix)-1-c][len(matrix)-1-r] = matrix[len(matrix)-1-c][len(matrix)-1-r], matrix[r][c]

    for row in matrix:
        print(row)


if __name__ == '__main__':
    # matrix = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]
    matrix = [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ]
    for row in matrix:
        print(row)
    print('')
    rotate(matrix)
