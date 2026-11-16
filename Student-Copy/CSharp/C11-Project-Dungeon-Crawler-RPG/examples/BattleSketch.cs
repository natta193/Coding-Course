while (hero.IsAlive && enemy.IsAlive)
{
    Console.WriteLine($"{hero} vs {enemy}");
    Console.Write("[A]ttack [D]efend [I]tem [F]lee: ");
    var key = Console.ReadKey(true).Key;
    switch (key)
    {
        case ConsoleKey.A: hero.Attack(enemy); break;
        case ConsoleKey.D: hero.Defend(); break;
        case ConsoleKey.I: UseItem(hero); break;
        case ConsoleKey.F when Random.Shared.NextDouble() < 0.5:
            Console.WriteLine("You escaped!");
            return;
    }
    if (enemy.IsAlive) enemy.Attack(hero);
}
