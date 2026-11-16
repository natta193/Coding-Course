File.WriteAllLines("scores.txt", new[] { "Ana,120", "garbage line", "Ben,abc", "Cai,95", ",50" });
var hs = new HighScores("scores.txt");
Console.WriteLine($"Loaded {hs.Entries.Count}, skipped {hs.Skipped} bad lines");
hs.Add("Dev", 130);
hs.Save();
foreach (var (name, score) in hs.Entries.OrderByDescending(e => e.Score))
    Console.WriteLine($"{name,-6}{score,5}");

public class HighScores
{
    private readonly string path;
    public List<(string Name, int Score)> Entries { get; } = new();
    public int Skipped { get; private set; }

    public HighScores(string path)
    {
        this.path = path;
        if (!File.Exists(path)) return;
        foreach (string line in File.ReadAllLines(path))
        {
            string[] parts = line.Split(',');
            if (parts.Length == 2 && parts[0].Trim() != "" && int.TryParse(parts[1], out int score))
                Entries.Add((parts[0].Trim(), score));
            else
                Skipped++;
        }
    }

    public void Add(string name, int score) => Entries.Add((name, score));

    public void Save()
    {
        string temp = path + ".tmp";
        try
        {
            File.WriteAllLines(temp, Entries.Select(e => $"{e.Name},{e.Score}"));
            File.Move(temp, path, overwrite: true);
        }
        catch (IOException ex)
        {
            Console.WriteLine($"Couldn't save scores: {ex.Message}");
        }
    }
}
