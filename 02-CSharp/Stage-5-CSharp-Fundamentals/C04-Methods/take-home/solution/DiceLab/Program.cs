static int Roll(int sides = 6) => Random.Shared.Next(1, sides + 1);

static int RollDice(int count, int sides)
{
    int total = 0;
    for (int i = 0; i < count; i++) total += Roll(sides);
    return total;
}

static int[] RollMany(int count, int sides = 6)
{
    int[] r = new int[count];
    for (int i = 0; i < count; i++) r[i] = Roll(sides);
    return r;
}

static (double mean, int min, int max) Stats(int[] rolls) => (rolls.Average(), rolls.Min(), rolls.Max());

static void Histogram(int[] rolls, int lowest, int highest)
{
    for (int v = lowest; v <= highest; v++)
    {
        int n = rolls.Count(r => r == v);
        Console.WriteLine($"{v,3}: {new string('█', n * 200 / rolls.Length)} {100.0 * n / rolls.Length:F1}%");
    }
}

var single = RollMany(10_000);
var (mean, min, max) = Stats(single);
Console.WriteLine($"1d6 x10000: mean {mean:F2}, min {min}, max {max}");
Histogram(single, 1, 6);

int[] pairs = new int[100_000];
for (int i = 0; i < pairs.Length; i++) pairs[i] = RollDice(2, 6);
Console.WriteLine("\n2d6 totals:");
Histogram(pairs, 2, 12);

int[] threeD6 = new int[10_000];
for (int i = 0; i < threeD6.Length; i++) threeD6[i] = RollDice(3, 6);
Console.WriteLine($"\n3d6 mean: {threeD6.Average():F2}");
