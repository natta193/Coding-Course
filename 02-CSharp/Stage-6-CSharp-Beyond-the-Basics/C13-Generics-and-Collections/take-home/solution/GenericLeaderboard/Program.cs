var races = new Leaderboard<TimeEntry>(5);
var scores = new Leaderboard<ScoreEntry>(5);
string[] names = { "Ana", "Ben", "Cai", "Dev", "Eli", "Fay", "Gus", "Hal" };
for (int i = 0; i < 20; i++)
{
    string n = names[Random.Shared.Next(names.Length)];
    int pos = races.Add(new TimeEntry(n, Math.Round(10 + Random.Shared.NextDouble() * 5, 2)));
    scores.Add(new ScoreEntry(n, Random.Shared.Next(50, 200)));
    if (pos == 1) Console.WriteLine($"New race record by {n}!");
}
Console.WriteLine("🏃 Fastest times:");
foreach (var e in races) Console.WriteLine($"  {e.Name,-4} {e.Seconds:F2}s");
Console.WriteLine("🎯 Top scores:");
foreach (var e in scores) Console.WriteLine($"  {e.Name,-4} {e.Points}");

public record TimeEntry(string Name, double Seconds) : IComparable<TimeEntry>
{
    public int CompareTo(TimeEntry? other) => other is null ? -1 : Seconds.CompareTo(other.Seconds);
}

public record ScoreEntry(string Name, int Points) : IComparable<ScoreEntry>
{
    public int CompareTo(ScoreEntry? other)
    {
        if (other is null) return -1;
        int c = other.Points.CompareTo(Points);          // higher first
        return c != 0 ? c : string.Compare(Name, other.Name, StringComparison.Ordinal);
    }
}

public class Leaderboard<T> : IEnumerable<T> where T : IComparable<T>
{
    private readonly List<T> entries = new();
    private readonly int capacity;

    public Leaderboard(int capacity) => this.capacity = capacity;

    public int Add(T entry)
    {
        int i = 0;
        while (i < entries.Count && entries[i].CompareTo(entry) <= 0) i++;
        if (i >= capacity) return -1;
        entries.Insert(i, entry);
        if (entries.Count > capacity) entries.RemoveAt(entries.Count - 1);
        return i + 1;
    }

    public IEnumerator<T> GetEnumerator() => entries.GetEnumerator();
    System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator() => GetEnumerator();
}
