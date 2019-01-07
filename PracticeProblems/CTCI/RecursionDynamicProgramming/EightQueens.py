class Board():

    def __init__(self, rows, cols):
        self.grid = [[Square() for _ in range(cols)] for _ in range(rows)]

    def eliminate_squares(self, q_square):
        r = q_square[0]
        c = q_square[1]

        # Eliminate all squares in row
        for square in self.grid[r]:
            square.eliminate()

        # Eliminate all squares in col
        for row in self.grid:
            row[c].eliminate()

        # Eliminate all squares in diag
        for x in range(1, len(self.grid)):
            row = r + x
            col = c + x
            if row >= 0 and col >= 0 and row < len(self.grid) and col < len(self.grid):
                self.grid[row][col].eliminate()
            row = r - x
            col = c - x
            if row >= 0 and col >= 0 and row < len(self.grid) and col < len(self.grid):
                self.grid[row][col].eliminate()
            row = r - x
            col = c + x
            if row >= 0 and col >= 0 and row < len(self.grid) and col < len(self.grid):
                self.grid[row][col].eliminate()
            row = r + x
            col = c - x
            if row >= 0 and col >= 0 and row < len(self.grid) and col < len(self.grid):
                self.grid[row][col].eliminate()

    def add_queen(self, square):
        square.add_queen()


class Square():

    def __init__(self):
        self.status = '_'

    def add_queen(self):
        self.status = 'Q'

    def eliminate(self):
        self.status = '.'

    def isAvailable(self):
        return self.status == '_'


def main(queens):

    board_layouts = []

    for x in range(queens):
        board = Board(8, 8)
        origin = (0, x)
        layout = get_board_combos(board, queens, origin)
        board_layouts.append(layout)

    return board_layouts


def get_board_combos(board, queens, origin):

    # Eliminate the squares on origins row, col, diag
    board.eliminate_squares(origin)

    # Add queen to origin square
    board.grid[origin[0]][origin[1]].add_queen()

    # Add rest of queens to board
    for r, row in enumerate(board.grid):

        # Find available column
        for c, col in enumerate(row):
            if col.status == '_':

                # Eliminate squares for r, c
                board.eliminate_squares((r, c))
                board.grid[r][c].add_queen()
                break

    # for row in board.grid:
    #     print([sq.status for sq in row])

    return board


if __name__ == '__main__':
    queens = 8
    board_layouts = main(queens)

    for i, b in enumerate(board_layouts):
        print('Board {}: '.format(i+1))
        for r in b.grid:
            print([sq.status for sq in r])
