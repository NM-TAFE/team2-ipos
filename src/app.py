import os
from flask import Flask, redirect, render_template, request, session, url_for
from src.game import check_winner, check_draw, to_row_col, new_board, P1, P2
from src.models import TicTacToe

# Set up template and static folders relative to the project root
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = "ipos-secret-key"

# Initialise game instance
game = TicTacToe()


def get_player_name():
    """
    Get p1_name and p2_name from the session variable. If not, return default name.
    """
    p1 = session.get("p1_name", "Player 1")
    p2 = session.get("p2_name", "Player 2")
    return p1, p2


@app.route("/set_name", methods=["GET", "POST"])
def set_name():
    """
    Save p1_name and p2_name to session variable. Redirect to index.
    """
    if request.method == "POST":
        p1 = request.form.get("p1_name", " ").strip()
        p2 = request.form.get("p2_name", " ").strip()
        session["p1_name"] = p1 if p1 else "Player 1"
        session["p2_name"] = p2 if p2 else "Player 2"
        return redirect(url_for("index"))
    return redirect(url_for("index"))


@app.route("/")
def index():
    winner = check_winner(game.board)
    draw = check_draw(game.board)
    p1_name, p2_name = get_player_name()
    return render_template(
        "index.html",
        board=game.board,
        current_player=game.current_player,
        winner=winner,
        draw=draw,
        score_x=game.score_x,
        score_o=game.score_o,
        p1_name=p1_name,
        p2_name=p2_name,
    )


@app.route("/play/<int:cell>")
def play(cell):
    row, col = to_row_col(cell)
    current_value = game.board[row][col]
    if current_value not in {P1, P2}:
        game.board[row][col] = game.current_player
        winner = check_winner(game.board)
        if winner == P1:
            game.score_x += 1
        elif winner == P2:
            game.score_o += 1
        if not winner:
            game.current_player = P2 if game.current_player == P1 else P1
    return redirect(url_for("index"))


@app.route("/reset")
def reset():
    game.board = new_board()
    game.current_player = P1
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
