using System.Diagnostics;

static async Task<string> Cook(string item, int seconds)
{
    Console.WriteLine($"  start {item}");
    await Task.Delay(seconds * 300);   // scaled down so it runs quickly
    Console.WriteLine($"  done  {item}");
    return item;
}

var menu = new (string Item, int Secs)[] { ("eggs", 3), ("toast", 2), ("juice", 1), ("coffee", 4) };

var sw = Stopwatch.StartNew();
Console.WriteLine("One at a time:");
foreach (var (item, secs) in menu) await Cook(item, secs);
Console.WriteLine($"Sequential: {sw.ElapsedMilliseconds} ms");

sw.Restart();
Console.WriteLine("All at once:");
string[] done = await Task.WhenAll(menu.Select(m => Cook(m.Item, m.Secs)));
Console.WriteLine($"Concurrent: {sw.ElapsedMilliseconds} ms – {string.Join(", ", done)} ready!");
