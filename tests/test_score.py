import unittest

import src.app as game_app
from src.game import P1, check_winner, new_board


class TestScoreCounter(unittest.TestCase):
    def setUp(self):
        game_app.game.board = new_board()

    def test_x_wins(self):
        game_app.game.board[0][0] = P1
        game_app.game.board[0][1] = P1
        game_app.game.board[0][2] = P1
        result = check_winner(game_app.game.board)
        self.assertEqual(result, P1)


if __name__ == "__main__":
    unittest.main()
