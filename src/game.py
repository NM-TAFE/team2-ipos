ROWS = 3
COLS = 3
P1 = "X"
P2 = "O"


def new_board():
    """Create a 2D board filled with numbers 1-9.
    Each number represents an empty, selectable cell.
    Returns a list of lists where each inner list is a row.
    """
    two_dim_list = []
    num = 1

    for _i in range(ROWS):
        row = []
        for _j in range(COLS):
            row.append(num)
            num += 1
        two_dim_list.append(row)

    return two_dim_list


def all_same_player(values):
    """Return the winning player if all values belong to the same player, else None."""
    if not values:
        return None

    first = values[0]

    if first not in {P1, P2}:
        return None

    for v in values:
        if v != first:
            return None

    return first


def check_winner(board):
    """Return the winning player (X or O) or None. Logic is dynamic — works for any n×n board."""
    b = board
    n = len(b)

    # Check rows
    for r in range(n):
        winner = all_same_player(b[r])
        if winner:
            return winner

    # Check columns
    for c in range(n):
        column_values = []
        for r in range(n):
            column_values.append(b[r][c])
        winner = all_same_player(column_values)
        if winner:
            return winner

    # Check main diagonal (top-left to bottom-right)
    main_diagonal = []
    for i in range(n):
        main_diagonal.append(b[i][i])
    winner = all_same_player(main_diagonal)
    if winner:
        return winner

    # Check anti-diagonal (top-right to bottom-left)
    anti_diagonal = []
    for r in range(n):
        anti_diagonal.append(b[r][n - 1 - r])
    winner = all_same_player(anti_diagonal)
    if winner:
        return winner

    return None


def check_draw(board):
    """Return True if no empty cells remain (no number left on the board)."""
    for row in board:
        for cell in row:
            # If we find a number, the game is NOT a tie
            if cell not in {P1, P2}:
                return False
    # If we never found a number, it is a tie
    return True


def to_row_col(target):
    """Convert a 1-based flat cell number (1-9) to (row, col) for the 2D board."""
    row = (target - 1) // COLS
    col = (target - 1) % COLS
    return row, col
