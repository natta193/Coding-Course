using System.Text.Json;

const string FilePath = "habits.json";
var opts = new JsonSerializerOptions { WriteIndented = true };

TrackerData Load()
{
    if (!File.Exists(FilePath)) return new TrackerData(1, new List<Habit>());
    try
    {
        return JsonSerializer.Deserialize<TrackerData>(File.ReadAllText(FilePath)) ?? new TrackerData(1, new());
    }
    catch (JsonException)
    {
        File.Copy(FilePath, FilePath + ".corrupt", overwrite: true);
        Console.WriteLine("Save file was corrupt – backed it up and started fresh.");
        return new TrackerData(1, new());
    }
}

void Save(TrackerData d) => File.WriteAllText(FilePath, JsonSerializer.Serialize(d, opts));

int Streak(Habit h, DateOnly today)
{
    int s = 0;
    while (h.DoneOn.Contains(today.AddDays(-s))) s++;
    return s;
}

var data = Load();
var today = DateOnly.FromDateTime(DateTime.Today);
while (true)
{
    Console.Write("\n(a)dd habit (t)ick today (r)eport (q)uit: ");
    string c = (Console.ReadLine() ?? "q").Trim().ToLower();
    if (c == "q" || c == "") break;
    if (c == "a")
    {
        Console.Write("Habit name: ");
        string name = (Console.ReadLine() ?? "").Trim();
        if (name != "" && data.Habits.All(h => h.Name != name)) data.Habits.Add(new Habit(name, new List<DateOnly>()));
        Save(data);
    }
    else if (c == "t")
    {
        foreach (var h in data.Habits.Where(h => !h.DoneOn.Contains(today)))
        {
            Console.Write($"Did you {h.Name} today? (y/n) ");
            if ((Console.ReadLine() ?? "").Trim().ToLower() == "y") h.DoneOn.Add(today);
        }
        Save(data);
    }
    else if (c == "r")
    {
        foreach (var h in data.Habits)
        {
            string last14 = string.Concat(Enumerable.Range(0, 14).Reverse().Select(i => h.DoneOn.Contains(today.AddDays(-i)) ? "✓" : "·"));
            Console.WriteLine($"{h.Name,-10} total {h.DoneOn.Count,3}  streak {Streak(h, today),2}  {last14}");
        }
    }
}

public record Habit(string Name, List<DateOnly> DoneOn);
public record TrackerData(int Version, List<Habit> Habits);
