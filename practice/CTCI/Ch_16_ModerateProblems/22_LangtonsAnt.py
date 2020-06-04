class Board(list):

    def __str__(self):
        return "\n".join(" ".join(row) for row in self)


class Game(object):

    BLACK = "X"
    WHITE = "O"
    CTRLS = [
        "left",
        None,
        "right",
        "up",
        None,
        "down",
    ]
    EXIT = "stop"
    START = [4, 4]

    def __init__(self, k):
        self.flag = True
        self.arena = Board([["O"] * (2*k) for _ in range((2*k))])
        self.curr_pos = Game.START[:]
        self.prev_pos = Game.START[:]
        self.move_ant()
        self.moves_left = k

    def move_ant(self):
        px, py = self.prev_pos
        cx, cy = self.curr_pos
        if (-1 < cx < 5) and (-1 < cy < 5):
            self.arena[py][px] = Game.WHITE
            self.arena[cy][cx] = Game.BLACK
        else:
            print("Please enter a proper direction.")
            self.curr_pos = self.prev_pos[:]
            self.move_ant()

    def play(self):

        while self.moves_left > 0:
            print(str(self.arena))
            
            ctrl = 'right'
            if ctrl in Game.CTRLS:
                d = Game.CTRLS.index(ctrl)
                self.prev_pos = self.curr_pos[:]
                self.curr_pos[d > 2] += d - (1 if d < 3 else 4)
                self.move_ant()

            elif ctrl == Game.EXIT:
                self.flag = False



def main(k):
    my_game = Game(k)
    my_game.play()


if __name__ == '__main__':
    moves = 5
    main(moves)