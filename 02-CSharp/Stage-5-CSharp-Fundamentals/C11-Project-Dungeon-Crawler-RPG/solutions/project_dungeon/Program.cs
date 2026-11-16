var game = new Game();
game.Run();

public abstract class Character
{
    public string Name { get; }
    public int MaxHp { get; protected set; }
    public int Hp { get; protected set; }
    public int Power { get; protected set; }
    public bool IsAlive => Hp > 0;
    protected bool defending;

    protected Character(string name, int hp, int power)
    {
        Name = name;
        MaxHp = Hp = hp;
        Power = power;
    }

    public virtual void TakeDamage(int amount)
    {
        if (defending) amount /= 2;
        Hp = Math.Max(0, Hp - amount);
        defending = false;
    }

    public void Heal(int amount) => Hp = Math.Min(MaxHp, Hp + amount);

    public virtual void Attack(Character target)
    {
        int dmg = Power + Random.Shared.Next(-2, 3);
        target.TakeDamage(dmg);
        Console.WriteLine($"{Name} hits {target.Name} for {dmg}.");
    }

    public void Defend()
    {
        defending = true;
        Console.WriteLine($"{Name} raises their guard.");
    }

    public override string ToString() => $"{Name} [{Hp}/{MaxHp}]";
}

public abstract class Hero : Character
{
    public int Xp { get; private set; }
    public int Level { get; private set; } = 1;
    public List<IItem> Inventory { get; } = new();

    protected Hero(string name, int hp, int power) : base(name, hp, power) { }

    public abstract void Special(Character target);

    public void GainXp(int xp)
    {
        Xp += xp;
        while (Xp >= Level * 20)
        {
            Xp -= Level * 20;
            Level++;
            MaxHp += 10;
            Power += 2;
            Hp = MaxHp;
            Console.WriteLine($"*** LEVEL UP! {Name} is now level {Level} ***");
        }
    }
}

public class Warrior : Hero
{
    public Warrior() : base("Warrior", 60, 8) { }
    public override void Special(Character t)
    {
        Console.WriteLine("Mighty cleave!");
        t.TakeDamage(Power * 2);
        TakeDamage(5);
    }
}

public class Mage : Hero
{
    public Mage() : base("Mage", 40, 6) { }
    public override void Special(Character t)
    {
        int dmg = Random.Shared.Next(10, 26);
        Console.WriteLine($"Fireball for {dmg}!");
        t.TakeDamage(dmg);
    }
}

public class Rogue : Hero
{
    public Rogue() : base("Rogue", 48, 7) { }
    public override void TakeDamage(int amount)
    {
        if (Random.Shared.NextDouble() < 0.25) { Console.WriteLine("Rogue dodges!"); return; }
        base.TakeDamage(amount);
    }
    public override void Special(Character t)
    {
        Console.WriteLine("Backstab x2!");
        Attack(t);
        Attack(t);
    }
}

public class Enemy : Character
{
    public int XpReward { get; }
    public Enemy(string name, int hp, int power, int xp) : base(name, hp, power) => XpReward = xp;

    public static Enemy Random(int floor) => System.Random.Shared.Next(3) switch
    {
        0 => new Enemy("Goblin", 18 + floor * 6, 4 + floor, 8 + floor * 2),
        1 => new Enemy("Skeleton", 25 + floor * 6, 5 + floor, 12 + floor * 2),
        _ => new Enemy("Slime", 12 + floor * 4, 3 + floor, 5 + floor * 2),
    };
}

public interface IItem
{
    string Name { get; }
    void Use(Hero hero, Character? enemy);
}

public class Potion : IItem
{
    public string Name => "Potion";
    public void Use(Hero hero, Character? enemy) { hero.Heal(25); Console.WriteLine($"{hero.Name} heals to {hero.Hp}."); }
}

public class Bomb : IItem
{
    public string Name => "Bomb";
    public void Use(Hero hero, Character? enemy)
    {
        if (enemy is null) { Console.WriteLine("Nothing to blow up!"); return; }
        enemy.TakeDamage(20);
        Console.WriteLine($"BOOM! {enemy.Name} takes 20.");
    }
}

public class Room
{
    public Enemy? Enemy { get; set; }
    public IItem? Item { get; set; }
    public bool Stairs { get; set; }
    public bool Visited { get; set; }
}

public class Game
{
    private Hero hero = new Warrior();
    private Room[,] rooms = new Room[4, 4];
    private int x, y, floor = 1;

    private void BuildFloor()
    {
        for (int r = 0; r < 4; r++)
            for (int c = 0; c < 4; c++)
            {
                rooms[r, c] = new Room();
                double roll = Random.Shared.NextDouble();
                if (roll < 0.45) rooms[r, c].Enemy = Enemy.Random(floor);
                else if (roll < 0.70) rooms[r, c].Item = Random.Shared.Next(2) == 0 ? new Potion() : new Bomb();
            }
        rooms[0, 0] = new Room { Visited = true };
        var exit = rooms[3, 3];
        exit.Stairs = true;
        exit.Enemy = floor == 3 ? new Enemy("DRAGON", 120, 12, 100) : exit.Enemy;
        x = y = 0;
    }

    private char ReadChoice(string prompt, string allowed)
    {
        while (true)
        {
            Console.Write(prompt);
            string s = (Console.ReadLine() ?? "q").Trim().ToLower();
            if (s.Length > 0 && allowed.Contains(s[0])) return s[0];
        }
    }

    private bool Battle(Enemy enemy)
    {
        Console.WriteLine($"\nA {enemy.Name} appears!");
        while (hero.IsAlive && enemy.IsAlive)
        {
            Console.WriteLine($"{hero}  vs  {enemy}");
            char c = ReadChoice("[a]ttack [s]pecial [d]efend [i]tem [f]lee: ", "asdifq");
            if (c == 'q') return false;
            if (c == 'a') hero.Attack(enemy);
            else if (c == 's') hero.Special(enemy);
            else if (c == 'd') hero.Defend();
            else if (c == 'i') UseItem(enemy);
            else if (c == 'f' && Random.Shared.NextDouble() < 0.5) { Console.WriteLine("You flee!"); return true; }
            if (enemy.IsAlive) enemy.Attack(hero);
        }
        if (hero.IsAlive)
        {
            Console.WriteLine($"{enemy.Name} defeated! +{enemy.XpReward} XP");
            hero.GainXp(enemy.XpReward);
        }
        return hero.IsAlive;
    }

    private void UseItem(Character? enemy)
    {
        if (hero.Inventory.Count == 0) { Console.WriteLine("Your bag is empty."); return; }
        for (int i = 0; i < hero.Inventory.Count; i++) Console.WriteLine($"{i + 1}) {hero.Inventory[i].Name}");
        if (int.TryParse(Console.ReadLine(), out int n) && n >= 1 && n <= hero.Inventory.Count)
        {
            var item = hero.Inventory[n - 1];
            hero.Inventory.RemoveAt(n - 1);
            item.Use(hero, enemy);
        }
    }

    private void DrawMap()
    {
        for (int r = 0; r < 4; r++)
        {
            for (int c = 0; c < 4; c++)
                Console.Write(r == y && c == x ? "[@]" : rooms[r, c].Stairs ? "[>]" : rooms[r, c].Visited ? "[ ]" : "[?]");
            Console.WriteLine();
        }
    }

    public void Run()
    {
        char cls = ReadChoice("Choose: [w]arrior [m]age [r]ogue: ", "wmrq");
        hero = cls switch { 'm' => new Mage(), 'r' => new Rogue(), _ => new Warrior() };
        BuildFloor();
        while (hero.IsAlive)
        {
            Console.WriteLine($"\n== Floor {floor} == {hero} Lv{hero.Level}");
            DrawMap();
            char dir = ReadChoice("Move [n/s/e/w], [i]tem, [q]uit: ", "nsewiq");
            if (dir == 'q') return;
            if (dir == 'i') { UseItem(null); continue; }
            int nx = x + (dir == 'e' ? 1 : dir == 'w' ? -1 : 0);
            int ny = y + (dir == 's' ? 1 : dir == 'n' ? -1 : 0);
            if (nx < 0 || nx > 3 || ny < 0 || ny > 3) { Console.WriteLine("A wall blocks your way."); continue; }
            x = nx; y = ny;
            var room = rooms[y, x];
            room.Visited = true;
            if (room.Enemy is { IsAlive: true } enemy && !Battle(enemy)) break;
            if (room.Item is not null)
            {
                Console.WriteLine($"You found a {room.Item.Name}!");
                hero.Inventory.Add(room.Item);
                room.Item = null;
            }
            if (room.Stairs)
            {
                if (floor == 3) { Console.WriteLine("\n🏆 The dragon is slain. You win!"); return; }
                floor++;
                Console.WriteLine("You descend the stairs...");
                BuildFloor();
            }
        }
        Console.WriteLine("\n💀 You have fallen. Game over.");
    }
}
