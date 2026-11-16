// Compiler errors I hit: CS1002 (; expected), CS0103 (name doesn't exist – typo), CS0029 (can't convert string to int)
Console.Write("1) poster  2) character  3) dice race: ");
string choice = Console.ReadLine() ?? "";

if (choice == "1")
{
    Console.ForegroundColor = ConsoleColor.Cyan;
    Console.WriteLine("========================================");
    Console.WriteLine("   A L L   A B O U T   A L E X");
    Console.WriteLine("========================================");
    Console.ResetColor();
    Console.WriteLine("Age: 13 | Year 9 | Favourite game: Minecraft");
    Console.WriteLine("Why do programmers prefer dark mode?");
    Console.ReadLine();
    Console.WriteLine("Because light attracts bugs!");
}
else if (choice == "2")
{
    Console.Write("Name: ");
    string name = Console.ReadLine() ?? "Hero";
    Console.Write("Strength (1-10): ");
    int strength = int.Parse(Console.ReadLine() ?? "5");
    Console.Write("Smarts (1-10): ");
    int smarts = int.Parse(Console.ReadLine() ?? "5");
    int health = strength * 10 + 50;
    int mana = smarts * 8;
    Console.WriteLine($"╔═══════════════════╗\n  {name.ToUpper()}\n  Health: {health}\n  Mana:   {mana}\n╚═══════════════════╝");
}
else if (choice == "3")
{
    int[] scores = { 0, 0 };
    int player = 0;
    while (scores[0] < 50 && scores[1] < 50)
    {
        Console.Write($"Player {player + 1}, press Enter to roll...");
        Console.ReadLine();
        int roll = Random.Shared.Next(1, 7);
        scores[player] += roll;
        if (scores[player] == 13) scores[player] = 0;
        Console.WriteLine($"Rolled {roll}. Scores: {scores[0]} - {scores[1]}");
        if (scores[player] >= 50) break;
        player = 1 - player;
    }
    Console.WriteLine($"Player {player + 1} wins!");
}
