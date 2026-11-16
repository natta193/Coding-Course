board = [[" "] * 3 for _ in range(3)]
player = "X"

for turn in range(9):
    for row in board:
        print("|".join(row))
        print("-+-+-")
    while True:
        r = int(input(f"{player} row (0-2): "))
        c = int(input(f"{player} col (0-2): "))
        if 0 <= r <= 2 and 0 <= c <= 2 and board[r][c] == " ":
            break
        print("Invalid move, try again")
    board[r][c] = player

    lines = board + [list(col) for col in zip(*board)]
    lines += [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]
    if [player] * 3 in lines:
        print(f"{player} wins!")
        break
    player = "O" if player == "X" else "X"
else:
    print("It's a draw!")

for row in board:
    print("|".join(row))
