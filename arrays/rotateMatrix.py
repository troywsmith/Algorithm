class Image:

    def __init__(self, matrix):
        self.matrix = matrix

    def swapPixels(self, r1, c1, r2, c2):
        self.matrix[r1][c1], self.matrix[r2][c2] = self.matrix[r2][c2], self.matrix[r1][c1]

    def printImage(self):
        print('\nImage:')
        for row in self.matrix:
            print(row)
        print('\n')

    def rotateImage(self):
        n = len(self.matrix)
        for layer in range(n//2):
            first = layer
            last = n - 1 - first
            for i in range(first, last):
                offset = i - first
                top = self.matrix[first][i]

                # Left -> Top
                self.matrix[first][i] = self.matrix[last-offset][first]

                # Bottom -> Left
                self.matrix[last-offset][first] = self.matrix[last][last-offset]

                # Right -> Bottom
                self.matrix[last][last-offset] = matrix[i][last]

                # Top -> Right
                matrix[i][last] = top


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    img = Image(matrix)
    img.printImage()
    img.rotateImage()
    img.printImage()