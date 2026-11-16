static int Add(int a, int b)
{
    return a + b;
}

static void Greet(string name)
{
    Console.WriteLine($"Hello, {name}!");
}

static bool IsEven(int n) => n % 2 == 0;   // one-liner

Console.WriteLine(Add(3, 4));    // 7
Greet("Ana");
Console.WriteLine(IsEven(10));   // True
