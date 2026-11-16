int size = 5;

for (int r = 1; r <= size; r++)
    Console.WriteLine(new string('*', r));

for (int r = 1; r <= size; r++)
    Console.WriteLine(new string(' ', size - r) + new string('*', 2 * r - 1));

for (int r = 0; r < size; r++)
{
    for (int c = 0; c < size; c++)
    {
        bool edge = r == 0 || r == size - 1 || c == 0 || c == size - 1;
        Console.Write(edge ? "* " : "  ");
    }
    Console.WriteLine();
}

for (int r = 1; r <= 10; r++)
{
    for (int c = 1; c <= 10; c++)
        Console.Write($"{r * c,4}");
    Console.WriteLine();
}
