Console.Write("Pick a number: ");
string text = Console.ReadLine() ?? "";

if (int.TryParse(text, out int number))
{
    Console.WriteLine($"Double that is {number * 2}");
}
else
{
    Console.WriteLine("That's not a whole number!");
}
