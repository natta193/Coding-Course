static int[] MergeSort(int[] a)
{
    if (a.Length <= 1) return a.ToArray();
    int mid = a.Length / 2;
    int[] l = MergeSort(a[..mid]), r = MergeSort(a[mid..]);
    var res = new int[a.Length];
    int i = 0, j = 0, k = 0;
    while (i < l.Length && j < r.Length) res[k++] = l[i] <= r[j] ? l[i++] : r[j++];
    while (i < l.Length) res[k++] = l[i++];
    while (j < r.Length) res[k++] = r[j++];
    return res;
}

static int BinarySearch(int[] a, int target)
{
    int lo = 0, hi = a.Length - 1;
    while (lo <= hi)
    {
        int mid = (lo + hi) / 2;
        if (a[mid] == target) return mid;
        if (a[mid] < target) lo = mid + 1; else hi = mid - 1;
    }
    return -1;
}

int passed = 0, failed = 0;
void Check(string name, bool ok) { if (ok) passed++; else { failed++; Console.WriteLine("FAIL " + name); } }

Check("empty", MergeSort(Array.Empty<int>()).Length == 0);
Check("single", MergeSort(new[] { 5 }).SequenceEqual(new[] { 5 }));
Check("duplicates", MergeSort(new[] { 3, 1, 3, 1 }).SequenceEqual(new[] { 1, 1, 3, 3 }));
Check("negatives", MergeSort(new[] { 0, -5, 3 }).SequenceEqual(new[] { -5, 0, 3 }));
Check("reversed", MergeSort(Enumerable.Range(1, 10).Reverse().ToArray()).SequenceEqual(Enumerable.Range(1, 10)));
for (int t = 0; t < 200; t++)
{
    int[] data = Enumerable.Range(0, Random.Shared.Next(30)).Select(_ => Random.Shared.Next(-50, 50)).ToArray();
    int[] expected = data.ToArray();
    Array.Sort(expected);
    Check($"random {t}", MergeSort(data).SequenceEqual(expected));
}
int[] s = { 1, 3, 5, 7, 9 };
Check("bs found", BinarySearch(s, 7) == 3);
Check("bs first", BinarySearch(s, 1) == 0);
Check("bs missing", BinarySearch(s, 4) == -1);
Check("bs empty", BinarySearch(Array.Empty<int>(), 1) == -1);
Console.WriteLine($"{passed} passed, {failed} failed");
