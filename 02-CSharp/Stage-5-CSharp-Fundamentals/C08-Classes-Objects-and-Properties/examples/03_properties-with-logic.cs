public class Player
{
    private int health = 100;

    public int Health
    {
        get => health;
        set => health = Math.Clamp(value, 0, MaxHealth);
    }

    public int MaxHealth { get; init; } = 100;  // init-only
    public bool IsAlive => Health > 0;           // computed

    public override string ToString() =>
        $"Player ({Health}/{MaxHealth} HP)";
}

var p = new Player { MaxHealth = 150 };
p.Health -= 500;
Console.WriteLine(p);              // Player (0/150 HP)
Console.WriteLine(p.IsAlive);      // False
