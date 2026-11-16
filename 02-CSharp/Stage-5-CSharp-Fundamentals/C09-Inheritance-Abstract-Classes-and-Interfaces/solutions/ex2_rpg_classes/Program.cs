var party = new List<Character> { new Warrior("Brakka"), new Mage("Ilsa"), new Rogue("Vex") };
var monster = new Warrior("Troll");
monster.Restore(60);       // a beefy troll: 180 HP
int round = 1;
while (monster.IsAlive && party.Any(c => c.IsAlive))
{
    Console.WriteLine($"--- Round {round++} ---");
    foreach (var hero in party.Where(c => c.IsAlive))
    {
        if (hero is IHealer healer)
        {
            var weakest = party.Where(c => c.IsAlive).MinBy(c => c.Health)!;
            if (weakest.Health < 50) { healer.Heal(weakest); continue; }
        }
        int dmg = hero.Attack();
        monster.TakeDamage(dmg);
        Console.WriteLine($"{hero.Name} hits the Troll for {dmg} ({monster.Health} left)");
    }
    var alive = party.Where(c => c.IsAlive).ToList();
    if (monster.IsAlive && alive.Count > 0)
    {
        var target = alive[Random.Shared.Next(alive.Count)];
        target.TakeDamage(monster.Attack() + 5);
        Console.WriteLine($"Troll smashes {target.Name} ({target.Health} left)");
    }
}
Console.WriteLine(monster.IsAlive ? "The Troll wins..." : "The party wins!");

public interface IHealer
{
    void Heal(Character target);
}

public abstract class Character
{
    public string Name { get; }
    public int Health { get; protected set; }
    public bool IsAlive => Health > 0;

    protected Character(string name, int health) { Name = name; Health = health; }

    public abstract int Attack();

    public virtual void TakeDamage(int amount) => Health = Math.Max(0, Health - amount);

    public void Restore(int amount) => Health += amount;
}

public class Warrior : Character
{
    public Warrior(string name) : base(name, 120) { }
    public override int Attack() => 12;
}

public class Mage : Character, IHealer
{
    public Mage(string name) : base(name, 70) { }
    public override int Attack() => Random.Shared.Next(5, 30);
    public void Heal(Character target)
    {
        target.Restore(25);
        Console.WriteLine($"{Name} heals {target.Name} to {target.Health}");
    }
}

public class Rogue : Character
{
    public Rogue(string name) : base(name, 85) { }
    public override int Attack() => Random.Shared.Next(8, 18);
    public override void TakeDamage(int amount)
    {
        if (Random.Shared.NextDouble() < 0.3)
        {
            Console.WriteLine($"{Name} dodges!");
            return;
        }
        base.TakeDamage(amount);
    }
}
