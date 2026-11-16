using System.Diagnostics;

string[] horses = { "Thunder", "Biscuit", "Comet", "Pickle", "Shadow" };
const int Track = 30;
var positions = horses.ToDictionary(h => h, _ => 0);
var finishOrder = new List<(string Name, double Secs)>();
var sw = Stopwatch.StartNew();
object drawLock = new();

Console.WriteLine("Horses: " + string.Join(", ", horses.Select((h, i) => $"{i + 1}) {h}")));
Console.Write("Bet on a horse (1-5): ");
int.TryParse(Console.ReadLine(), out int bet);

void Draw()
{
    lock (drawLock)
    {
        if (!Console.IsOutputRedirected) Console.Clear();
        foreach (var h in horses)
            Console.WriteLine($"{h,-8}|{new string('-', positions[h])}🐎{new string(' ', Track - positions[h])}|");
    }
}

var progress = new Progress<(string Name, int Pos)>(p => { lock (drawLock) { positions[p.Name] = p.Pos; Draw(); } });

async Task<string> RunHorse(string name, IProgress<(string, int)> prog)
{
    for (int pos = 1; pos <= Track; pos++)
    {
        await Task.Delay(Random.Shared.Next(50, 250));
        prog.Report((name, pos));
    }
    lock (finishOrder) finishOrder.Add((name, sw.Elapsed.TotalSeconds));
    return name;
}

var tasks = horses.Select(h => RunHorse(h, progress)).ToList();
var first = await Task.WhenAny(tasks);
string winner = await first;
await Task.WhenAll(tasks);
await Task.Delay(100);
Draw();
Console.WriteLine($"\n🏆 {winner} wins!");
for (int i = 0; i < finishOrder.Count; i++)
    Console.WriteLine($"  {i + 1}. {finishOrder[i].Name,-8} {finishOrder[i].Secs:F2}s");
if (bet >= 1 && bet <= horses.Length)
    Console.WriteLine(horses[bet - 1] == winner ? "Your bet won! 💰" : "Your horse lost. Better luck next time.");
