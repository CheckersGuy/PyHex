import random
from Union import Union


class Board:
    RED = 1
    BLUE = 2

    def __init__(self):
        self.board = [0 for i in range(169)]
        self.mover = -1
        self.move_counter = 0

    def make_move(self, move):
        self.board[move] = self.mover
        self.move_counter += 1
        self.mover = -self.mover

    def undo_move(self, move):
        self.board[move] = 0
        self.move_counter -= 1
        self.mover = -self.mover


def play_out(board: Board, union: Union):
    empty_squares = [i for i in range(169) if board.board[i] != 0]
    random.shuffle(empty_squares)
    for sq in empty_squares:
        board.make_move(sq)

    for sq in empty_squares:
        board.undo_move(sq)

    return 0
