using System.Diagnostics;

static async Task<int> Download(int id)
{
    await Task.Delay(Random.Shared.Next(500, 1500));
    Console.WriteLine($"File {id} done");
    return id * 100;
}

var sw = Stopwatch.StartNew();
var jobs = Enumerable.Range(1, 5).Select(Download);
int[] sizes = await Task.WhenAll(jobs);
Console.WriteLine($"{sizes.Sum()} KB in {sw.ElapsedMilliseconds} ms");
