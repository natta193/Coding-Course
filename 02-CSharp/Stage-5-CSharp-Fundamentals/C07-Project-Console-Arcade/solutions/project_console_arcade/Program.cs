using System.Diagnostics;

const string ScoreFile = "scores.txt";

Dictionary<string, int> LoadScores()
{
    var s = new Dictionary<string, int>();
    if (File.Exists(ScoreFile))
        foreach (string line in File.ReadAllLines(ScoreFile))
        {
            string[] p = line.Split(',');
            if (p.Length == 2 && int.TryParse(p[1], out int v)) s[p[0]] = v;
        }
    return s;
}

void SaveScores(Dictionary<string, int> s) =>
    File.WriteAllLines(ScoreFile, s.Select(kv => $"{kv.Key},{kv.Value}"));

int ReadInt(string prompt)
{
    while (true)
    {
        Console.Write(prompt);
        if (int.TryParse(Console.ReadLine(), out int v)) return v;
        Console.WriteLine("Whole numbers only.");
    }
}

int HigherLower()
{
    int secret = Random.Shared.Next(1, 101), guesses = 0, guess;
    do
    {
        guess = ReadInt("Guess 1-100: ");
        guesses++;
        Console.WriteLine(guess > secret ? "Too high" : guess < secret ? "Too low" : "Correct!");
    } while (guess != secret);
    return Math.Max(0, 100 - guesses * 10);        // fewer guesses = higher score
}

int MathsSprint()
{
    Console.WriteLine("As many sums as you can in 30 seconds!");
    var sw = Stopwatch.StartNew();
    int score = 0;
    while (sw.Elapsed.TotalSeconds < 30)
    {
        int a = Random.Shared.Next(2, 13), b = Random.Shared.Next(2, 13);
        int ans = ReadInt($"{a} x {b} = ");
        if (sw.Elapsed.TotalSeconds >= 30) break;
        if (ans == a * b) score++;
        else Console.WriteLine($"  It's {a * b}");
    }
    Console.WriteLine($"Time! {score} correct.");
    return score;
}

int Catch()
{
    if (Console.IsInputRedirected)
    {
        Console.WriteLine("Catch needs a real terminal.");
        return 0;
    }
    const int W = 30, H = 15;
    int basket = W / 2, starX = Random.Shared.Next(W), starY = 0, score = 0, lives = 3;
    Console.CursorVisible = false;
    while (lives > 0)
    {
        while (Console.KeyAvailable)
        {
            var k = Console.ReadKey(true).Key;
            if (k == ConsoleKey.LeftArrow) basket = Math.Max(1, basket - 1);
            if (k == ConsoleKey.RightArrow) basket = Math.Min(W - 2, basket + 1);
        }
        starY++;
        if (starY == H - 1)
        {
            if (Math.Abs(starX - basket) <= 1) score++; else lives--;
            starX = Random.Shared.Next(W);
            starY = 0;
        }
        Console.Clear();
        Console.WriteLine($"Score {score}  Lives {lives}   (← →)");
        for (int y = 0; y < H; y++)
        {
            char[] row = new string(' ', W).ToCharArray();
            if (y == starY) row[starX] = '*';
            if (y == H - 1) { row[basket - 1] = '\\'; row[basket] = '_'; row[basket + 1] = '/'; }
            Console.WriteLine("|" + new string(row) + "|");
        }
        Thread.Sleep(Math.Max(40, 120 - score * 5));
    }
    Console.CursorVisible = true;
    return score;
}

var games = new (string Name, Func<int> Play)[]
{
    ("Higher or Lower", HigherLower),
    ("Maths Sprint", MathsSprint),
    ("Catch the Stars", Catch),
};
var best = LoadScores();

while (true)
{
    if (!Console.IsInputRedirected) Console.Clear();
    Console.ForegroundColor = ConsoleColor.Cyan;
    Console.WriteLine("╔══════════════════════╗\n║    CONSOLE  ARCADE   ║\n╚══════════════════════╝");
    Console.ResetColor();
    for (int i = 0; i < games.Length; i++)
        Console.WriteLine($"{i + 1}) {games[i].Name,-18} best: {best.GetValueOrDefault(games[i].Name)}");
    Console.WriteLine("0) Quit");
    int choice = ReadInt("> ");
    if (choice == 0 || choice > games.Length || choice < 0) break;
    var game = games[choice - 1];
    int score = game.Play();
    if (score > best.GetValueOrDefault(game.Name))
    {
        best[game.Name] = score;
        SaveScores(best);
        Console.WriteLine("NEW HIGH SCORE!");
    }
    Console.WriteLine("Press Enter for the menu...");
    Console.ReadLine();
}
