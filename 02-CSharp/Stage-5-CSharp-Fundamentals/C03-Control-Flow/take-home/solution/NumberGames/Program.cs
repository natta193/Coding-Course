using System.Diagnostics;

static bool IsPrime(int n)
{
    if (n < 2) return false;
    for (int d = 2; d * d <= n; d++)
        if (n % d == 0) return false;
    return true;
}

int total = 0;
string choice;
do
{
    Console.Write("\n1) times-table sprint  2) prime or not  3) fizzbuzz  0) quit: ");
    choice = Console.ReadLine() ?? "0";
    int score = choice switch
    {
        "1" => TimesSprint(),
        "2" => PrimeOrNot(),
        "3" => FizzGame(),
        _ => 0,
    };
    total += score;
    Console.WriteLine($"Scored {score}. Session total: {total}");
} while (choice != "0");

int TimesSprint()
{
    var sw = Stopwatch.StartNew();
    int correct = 0;
    for (int i = 0; i < 10; i++)
    {
        int a = Random.Shared.Next(2, 13), b = Random.Shared.Next(2, 13);
        Console.Write($"{a} x {b} = ");
        if (int.TryParse(Console.ReadLine(), out int ans) && ans == a * b) correct++;
    }
    Console.WriteLine($"{correct}/10 in {sw.Elapsed.TotalSeconds:F1}s");
    return correct;
}

int PrimeOrNot()
{
    int correct = 0, round = 0;
    while (round < 10)
    {
        int n = Random.Shared.Next(2, 101);
        Console.Write($"Is {n} prime? (y/n) ");
        bool said = (Console.ReadLine() ?? "").Trim().ToLower() == "y";
        if (said == IsPrime(n)) correct++; else Console.WriteLine("  Nope!");
        round++;
    }
    return correct;
}

int FizzGame()
{
    int correct = 0;
    for (int i = 1; i <= 15; i++)
    {
        string expected = (i % 3, i % 5) switch { (0, 0) => "fizzbuzz", (0, _) => "fizz", (_, 0) => "buzz", _ => i.ToString() };
        Console.Write($"{i}? ");
        if ((Console.ReadLine() ?? "").Trim().ToLower() == expected) correct++;
        else { Console.WriteLine($"  It was {expected}. Game over!"); break; }
    }
    return correct;
}
