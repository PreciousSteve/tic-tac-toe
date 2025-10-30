def play(board):
    turn = "x" if board.count("x") == board.count("o") else "o"
    print(f"Turn: {turn.upper()}")

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
            move = [a, b, c][line.index("")]
            print(f"Chosen move: {move}")
            return move

    opponent = "o" if turn == "x" else "x"
    for a, b, c in lines:
        line = [board[a], board[b], board[c]]
        if line.count(opponent) == 2 and line.count("") == 1:
            move = [a, b, c][line.index("")]
            print(f"Chosen move: {move}")
            return move

    if board[4] == "":
        print("Chosen move: 4")
        return 4

    for i, cell in enumerate(board):
        if cell == "":
            print(f"Chosen move: {i}")
            return i

    print("No vacant squares left. Cannot make a move.")
    return None
