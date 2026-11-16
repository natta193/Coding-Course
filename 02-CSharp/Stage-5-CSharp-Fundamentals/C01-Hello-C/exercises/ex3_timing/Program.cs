using System.Diagnostics;

var sw = Stopwatch.StartNew();
long count = 0;
// loop here

sw.Stop();
Console.WriteLine($"{count} in {sw.ElapsedMilliseconds} ms");
