static long Factorial(int n) => n <= 1 ? 1 : n * Factorial(n - 1);

var memo = new Dictionary<int, long>();
long Fib(int n)
{
    if (n < 2) return n;
    if (memo.TryGetValue(n, out long cached)) return cached;
    long value = Fib(n - 1) + Fib(n - 2);
    memo[n] = value;
    return value;
}

int moves = 0;
void Hanoi(int n, char from, char to, char spare)
{
    if (n == 0) return;
    Hanoi(n - 1, from, spare, to);
    moves++;
    Hanoi(n - 1, spare, to, from);
}

for (int i = 18; i <= 22; i++)
    Console.WriteLine($"{i}! = {Factorial(i)}");   // 21! overflows a long
Console.WriteLine($"Fib(90) = {Fib(90)}");
Hanoi(10, 'A', 'C', 'B');
Console.WriteLine($"Hanoi(10) took {moves} moves");
