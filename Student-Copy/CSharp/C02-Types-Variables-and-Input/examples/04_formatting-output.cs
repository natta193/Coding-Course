double pi = Math.PI;
decimal cost = 1234.5m;
int n = 7;

Console.WriteLine($"{pi:F2}");        // 3.14
Console.WriteLine($"{cost:C}");       // £1,234.50 (your currency)
Console.WriteLine($"{n:D3}");         // 007
Console.WriteLine($"{0.256:P0}");     // 26%
Console.WriteLine($"[{n,5}]");        // [    7] right-aligned
Console.WriteLine($"[{"hi",-5}]");    // [hi   ] left-aligned
