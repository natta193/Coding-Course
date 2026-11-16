static void MinMax(int[] nums, out int min, out int max)
{
    min = nums.Min();
    max = nums.Max();
}

static void Double(ref int x)
{
    x *= 2;
}

MinMax(new[] { 4, 9, 1 }, out int lo, out int hi);
Console.WriteLine($"{lo} {hi}");   // 1 9

int score = 10;
Double(ref score);
Console.WriteLine(score);          // 20 – changed!
