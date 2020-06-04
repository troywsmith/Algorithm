# Question 1.8
def zeroMatrix(matrix):
    """
    Time Complexity: O(mn)
    Space Complexity: O(rc)
    """
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            cell = matrix[x][y]
            if cell == 0:
                matrix[x][0] = 0
                matrix[0][y] = 0

    # Iterate through elements in first row 
    for i in range(1, len(matrix[0])):
        if matrix[0][i] == 0:
          for j in range(1,len(matrix)):
            matrix[j][i] = 0

    # # Iterate through elements in first column 
    for i in range(len(matrix)):
      if matrix[i][0] == 0:
        for j in range(len(matrix[i])):
          matrix[i][j] = 0


matrix = [
    [1, 2, 3, 4, 5],
    [1, 2, 0, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 0, 5]
]
for row in matrix:
    print(row)
print('\n')
zeroMatrix(matrix)
for row in matrix:
    print(row)
