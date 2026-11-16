Console.Write("How was your day? ");
string entry = Console.ReadLine() ?? "";
File.AppendAllText("journal.txt", $"{DateTime.Today:yyyy-MM-dd}: {entry}{Environment.NewLine}");

Console.WriteLine("Recent entries:");
foreach (string line in File.ReadAllLines("journal.txt").TakeLast(3))
    Console.WriteLine("  " + line);
