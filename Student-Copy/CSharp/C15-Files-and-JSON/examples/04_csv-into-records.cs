var players = File.ReadLines("players.csv")
    .Skip(1)                                  // header row
    .Select(line => line.Split(','))
    .Select(p => new Player(p[0], int.Parse(p[1])))
    .ToList();

Console.WriteLine(players.MaxBy(p => p.Score));

record Player(string Name, int Score);
