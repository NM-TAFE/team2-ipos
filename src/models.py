from src.game import new_board, P1

class TicTacToe:
    def __init__(self):
        # Initialise game board and current player
        self.board = new_board()
        self.current_player = P1
        self.score_x = 0
        self.score_o = 0
