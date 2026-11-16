using System.Diagnostics;

var sw = Stopwatch.StartNew();
long count = 0;
for (int i = 0; i < 50_000_000; i++)
{
    if (i % 7 == 0 || i % 11 == 0)
    {
        count++;
    }
}
sw.Stop();
Console.WriteLine($"{count} in {sw.ElapsedMilliseconds} ms");

// Python version for comparison:
// import time
// start = time.time()
// count = sum(1 for i in range(50_000_000) if i % 7 == 0 or i % 11 == 0)
// print(count, time.time() - start)
// Typically C# is 20-50x faster for loops like this.
