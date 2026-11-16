Func<int, int> square = x => x * x;
Func<int, int, int> add = (a, b) => a + b;
Func<string, bool> isLong = s => s.Length > 5;
Action<string> shout = msg => Console.WriteLine(msg.ToUpper());

Console.WriteLine(square(7));       // 49
Console.WriteLine(add(2, 3));       // 5
shout("hello");                     // HELLO

static int ApplyTwice(Func<int, int> f, int x) => f(f(x));
Console.WriteLine(ApplyTwice(square, 3));   // 81
