char[,] board = new char[3, 3];
for (int r = 0; r < 3; r++)
    for (int c = 0; c < 3; c++)
        board[r, c] = '.';

board[1, 1] = 'X';

for (int r = 0; r < board.GetLength(0); r++)
{
    for (int c = 0; c < board.GetLength(1); c++)
        Console.Write(board[r, c] + " ");
    Console.WriteLine();
}
