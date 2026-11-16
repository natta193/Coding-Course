public class Enemy
{
    public static int Count { get; private set; }
    public const int MaxEnemies = 50;

    public string Kind { get; }

    public Enemy(string kind)
    {
        Kind = kind;
        Count++;
    }

    private static readonly string[] Kinds = { "Goblin", "Orc" };
    public static Enemy Random() =>
        new Enemy(Kinds[System.Random.Shared.Next(2)]);
}

var e1 = new Enemy("Goblin");
var e2 = Enemy.Random();
Console.WriteLine(Enemy.Count);   // 2
