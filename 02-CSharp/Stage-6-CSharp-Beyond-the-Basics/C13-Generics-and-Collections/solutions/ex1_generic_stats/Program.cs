static T Largest<T>(List<T> items) where T : IComparable<T>
{
    T best = items[0];
    foreach (var x in items) if (x.CompareTo(best) > 0) best = x;
    return best;
}

static T Smallest<T>(List<T> items) where T : IComparable<T>
{
    T best = items[0];
    foreach (var x in items) if (x.CompareTo(best) < 0) best = x;
    return best;
}

static int CountWhere<T>(List<T> items, Func<T, bool> test)
{
    int n = 0;
    foreach (var x in items) if (test(x)) n++;
    return n;
}

static void Shuffle<T>(List<T> items)
{
    for (int i = items.Count - 1; i > 0; i--)
    {
        int j = Random.Shared.Next(i + 1);
        (items[i], items[j]) = (items[j], items[i]);
    }
}

var nums = new List<int> { 4, 8, 15, 16, 23, 42 };
var words = new List<string> { "kiwi", "apple", "mango" };
Console.WriteLine($"{Largest(nums)} {Smallest(nums)} {CountWhere(nums, n => n % 2 == 0)}");
Console.WriteLine($"{Largest(words)} {Smallest(words)} {CountWhere(words, w => w.Length > 4)}");
Shuffle(nums);
Console.WriteLine(string.Join(" ", nums));
