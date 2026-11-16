int ReadInt(string prompt, int min, int max)
{
    while (true)
    {
        Console.Write(prompt);
        string text = Console.ReadLine() ?? "";
        if (int.TryParse(text, out int value) && value >= min && value <= max)
        {
            return value;
        }
        Console.WriteLine($"Please enter a whole number from {min} to {max}.");
    }
}

int age = ReadInt("Age: ", 1, 120);
int fav = ReadInt("Favourite number: ", 1, 100);
Console.WriteLine($"Age {age}, favourite number {fav}");
