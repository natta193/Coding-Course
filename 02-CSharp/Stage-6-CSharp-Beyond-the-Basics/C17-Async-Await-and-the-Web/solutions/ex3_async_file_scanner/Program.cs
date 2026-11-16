string root = args.Length > 0 ? args[0] : Directory.GetCurrentDirectory();
var cts = new CancellationTokenSource(TimeSpan.FromSeconds(5));
var progress = new Progress<int>(pct => Console.Write($"\rScanning... {pct}%   "));

async Task<List<(string File, int Words)>> ScanAsync(string folder, IProgress<int> prog, CancellationToken token)
{
    var files = Directory.EnumerateFiles(folder, "*.*", SearchOption.AllDirectories)
                         .Where(f => f.EndsWith(".cs") || f.EndsWith(".txt") || f.EndsWith(".md") || f.EndsWith(".json"))
                         .ToList();
    var results = new List<(string, int)>();
    for (int i = 0; i < files.Count; i++)
    {
        token.ThrowIfCancellationRequested();
        string text = await File.ReadAllTextAsync(files[i], token);
        results.Add((files[i], text.Split((char[]?)null, StringSplitOptions.RemoveEmptyEntries).Length));
        prog.Report((i + 1) * 100 / files.Count);
    }
    return results;
}

try
{
    var results = await ScanAsync(root, progress, cts.Token);
    Console.WriteLine();
    foreach (var (file, words) in results.OrderByDescending(r => r.Words).Take(5))
        Console.WriteLine($"{words,8:N0}  {Path.GetRelativePath(root, file)}");
}
catch (OperationCanceledException)
{
    Console.WriteLine("\nScan cancelled – took too long.");
}
