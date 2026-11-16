const string FilePath = "scores.txt";

static Dictionary<string, int> LoadScores()
{
    var scores = new Dictionary<string, int>();
    if (!File.Exists(FilePath)) return scores;
    foreach (string line in File.ReadAllLines(FilePath))
    {
        string[] p = line.Split(',');
        scores[p[0]] = int.Parse(p[1]);
    }
    return scores;
}

static void SaveScores(Dictionary<string, int> s) =>
    File.WriteAllLines(FilePath,
        s.Select(kv => $"{kv.Key},{kv.Value}"));
