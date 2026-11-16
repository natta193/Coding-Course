public class Pair<TFirst, TSecond>
{
    public TFirst First { get; }
    public TSecond Second { get; }
    public Pair(TFirst f, TSecond s) { First = f; Second = s; }
    public override string ToString() => $"({First}, {Second})";
}

public class Box<T>
{
    private readonly List<T> items = new();
    public void Add(T item) => items.Add(item);
    public T? TakeRandom() =>
        items.Count == 0 ? default : items[Random.Shared.Next(items.Count)];
}

var p = new Pair<string, int>("Ana", 13);
var loot = new Box<string>();
loot.Add("sword"); loot.Add("gem");
