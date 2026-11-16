var players = new List<Player>
{
    new("Ana", "Red", 120), new("Ben", "Blue", 95),
    new("Cai", "Red", 150), new("Dev", "Blue", 130),
};

var redNames = players.Where(p => p.Team == "Red").Select(p => p.Name);
var best = players.MaxBy(p => p.Score);

foreach (var g in players.GroupBy(p => p.Team))
    Console.WriteLine($"{g.Key}: total {g.Sum(p => p.Score)}, avg {g.Average(p => p.Score)}");

record Player(string Name, string Team, int Score);
