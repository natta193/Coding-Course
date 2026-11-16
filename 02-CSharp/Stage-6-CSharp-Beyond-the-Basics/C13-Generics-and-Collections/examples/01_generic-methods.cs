static T Largest<T>(List<T> items) where T : IComparable<T>
{
    T best = items[0];
    foreach (T item in items)
        if (item.CompareTo(best) > 0) best = item;
    return best;
}

static void Swap<T>(ref T a, ref T b) => (a, b) = (b, a);

Console.WriteLine(Largest(new List<int> { 3, 9, 2 }));
Console.WriteLine(Largest(new List<string> { "pear", "fig" }));

int x = 1, y = 2;
Swap(ref x, ref y);
