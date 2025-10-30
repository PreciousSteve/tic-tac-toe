def play(board):
    turn = "x" if board.count("x") == board.count("o") else "o"

    lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in lines:
        line = [board[a], board[b], board[c]]
        if line.count(turn) == 2 and line.count("") == 1:
            return [a, b, c][line.index("")]

    opponent = "o" if turn == "x" else "x"
    for a, b, c in lines:
        line = [board[a], board[b], board[c]]
        if line.count(opponent) == 2 and line.count("") == 1:
            return [a, b, c][line.index("")]

    if board[4] == "":
        return 4

    for i, cell in enumerate(board):
        if cell == "":
            return i

    return None
