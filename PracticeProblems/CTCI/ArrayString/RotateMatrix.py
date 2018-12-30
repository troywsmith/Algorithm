# Question 1.7
def rotateMatrix(pic):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(pic)

    for layer in range(0, n//2):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first

            top = pic[first][i]

            # top = left
            pic[first][i] = pic[last-offset][first]

            # left = bottom
            pic[last-offset][first] = pic[last][last-offset]

            # bottom = right
            pic[last][last-offset] = pic[i][last]

            # right = top
            pic[i][last] = top


pic = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]
rotateMatrix(pic)
for row in pic:
    print(row)
