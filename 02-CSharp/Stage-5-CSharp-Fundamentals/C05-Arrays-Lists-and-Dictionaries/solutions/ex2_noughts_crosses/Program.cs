static bool CheckWin(char[,] b, char p)
{
    for (int i = 0; i < 3; i++)
    {
        if (b[i, 0] == p && b[i, 1] == p && b[i, 2] == p) return true;
        if (b[0, i] == p && b[1, i] == p && b[2, i] == p) return true;
    }
    return (b[0, 0] == p && b[1, 1] == p && b[2, 2] == p)
        || (b[0, 2] == p && b[1, 1] == p && b[2, 0] == p);
}

static void Draw(char[,] b)
{
    for (int r = 0; r < 3; r++)
    {
        Console.WriteLine($" {b[r, 0]} | {b[r, 1]} | {b[r, 2]}");
        if (r < 2) Console.WriteLine("---+---+---");
    }
}

char[,] board = new char[3, 3];
for (int r = 0; r < 3; r++)
    for (int c = 0; c < 3; c++)
        board[r, c] = ' ';

char player = 'X';
for (int turn = 0; turn < 9; turn++)
{
    Draw(board);
    int row, col;
    while (true)
    {
        Console.Write($"{player} – row and column (e.g. 1 2): ");
        string[] parts = (Console.ReadLine() ?? "").Split(' ', StringSplitOptions.RemoveEmptyEntries);
        if (parts.Length == 2 && int.TryParse(parts[0], out row) && int.TryParse(parts[1], out col)
            && row is >= 0 and <= 2 && col is >= 0 and <= 2 && board[row, col] == ' ')
            break;
        Console.WriteLine("Invalid move.");
    }
    board[row, col] = player;
    if (CheckWin(board, player))
    {
        Draw(board);
        Console.WriteLine($"{player} wins!");
        return;
    }
    player = player == 'X' ? 'O' : 'X';
}
Draw(board);
Console.WriteLine("Draw!");
