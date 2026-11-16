string[] moves = { "rock", "paper", "scissors" };
int you = 0, cpu = 0;

while (you < 3 && cpu < 3)
{
    string player;
    do
    {
        Console.Write("rock, paper or scissors? ");
        player = (Console.ReadLine() ?? "").Trim().ToLower();
    } while (Array.IndexOf(moves, player) == -1);

    string comp = moves[Random.Shared.Next(3)];
    string result = (player, comp) switch
    {
        _ when player == comp => "draw",
        ("rock", "scissors") or ("paper", "rock") or ("scissors", "paper") => "win",
        _ => "lose",
    };

    if (result == "win") you++;
    else if (result == "lose") cpu++;
    Console.WriteLine($"Computer chose {comp} – you {result}! ({you}-{cpu})");
}
Console.WriteLine(you == 3 ? "🏆 You win the tournament!" : "💻 The computer wins this time.");
