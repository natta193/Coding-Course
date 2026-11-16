Console.Write("Pick a direction (n/e/s/w): ");
string dir = Console.ReadLine() ?? "";

switch (dir)
{
    case "n":
        Console.WriteLine("You go north");
        break;
    case "s":
    case "south":
        Console.WriteLine("You go south");
        break;
    default:
        Console.WriteLine("You can't go that way");
        break;
}
