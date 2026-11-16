const int Size = 8;
var seen = new char[Size, Size];
var fleet = new List<List<(int R, int C)>>();
var occupied = new HashSet<(int, int)>();

for (int r = 0; r < Size; r++)
    for (int c = 0; c < Size; c++)
        seen[r, c] = '.';

foreach (int len in new[] { 4, 3, 2 })
{
    while (true)
    {
        bool horiz = Random.Shared.Next(2) == 0;
        int r = Random.Shared.Next(horiz ? Size : Size - len + 1);
        int c = Random.Shared.Next(horiz ? Size - len + 1 : Size);
        var cells = Enumerable.Range(0, len).Select(i => horiz ? (r, c + i) : (r + i, c)).ToList();
        if (cells.Any(occupied.Contains)) continue;
        cells.ForEach(x => occupied.Add(x));
        fleet.Add(cells.Select(x => (x.Item1, x.Item2)).ToList());
        break;
    }
}

void Draw()
{
    Console.WriteLine("   " + string.Join(" ", Enumerable.Range(1, Size)));
    for (int r = 0; r < Size; r++)
    {
        Console.Write($" {(char)('A' + r)} ");
        for (int c = 0; c < Size; c++) Console.Write(seen[r, c] + " ");
        Console.WriteLine();
    }
}

int shots = 25;
while (shots > 0 && fleet.Any(s => s.Count > 0))
{
    Draw();
    Console.Write($"{shots} shots left. Target (e.g. C5): ");
    string t = (Console.ReadLine() ?? "").Trim().ToUpper();
    if (t.Length < 2 || t[0] < 'A' || t[0] >= 'A' + Size || !int.TryParse(t[1..], out int col) || col < 1 || col > Size)
    {
        Console.WriteLine("Invalid coordinate.");
        if (Console.IsInputRedirected && t == "") break;
        continue;
    }
    int row = t[0] - 'A';
    col--;
    if (seen[row, col] != '.') { Console.WriteLine("Already fired there!"); continue; }
    shots--;
    var hitShip = fleet.FirstOrDefault(s => s.Contains((row, col)));
    if (hitShip != null)
    {
        seen[row, col] = 'X';
        hitShip.Remove((row, col));
        Console.WriteLine(hitShip.Count == 0 ? "💥 Hit – and SUNK!" : "💥 Hit!");
    }
    else
    {
        seen[row, col] = 'o';
        Console.WriteLine("Splash – miss.");
    }
}
Draw();
Console.WriteLine(fleet.All(s => s.Count == 0) ? "🏆 You sank the whole fleet!" : "Out of shots – the fleet survives.");
