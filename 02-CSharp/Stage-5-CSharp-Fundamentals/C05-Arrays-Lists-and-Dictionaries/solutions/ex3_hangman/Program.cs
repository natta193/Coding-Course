string[] words = { "python", "csharp", "variable", "keyboard", "galaxy" };
string secret = words[Random.Shared.Next(words.Length)];
var guessed = new List<char>();
var secretLetters = new HashSet<char>(secret);
int lives = 6;

string MaskWord() => string.Join(" ", secret.Select(ch => guessed.Contains(ch) ? ch : '_'));
bool HasWon() => secretLetters.All(guessed.Contains);

char ReadGuess()
{
    while (true)
    {
        Console.Write($"Guess a letter ({lives} lives): ");
        string s = (Console.ReadLine() ?? "").Trim().ToLower();
        if (s.Length == 1 && char.IsLetter(s[0]) && !guessed.Contains(s[0])) return s[0];
        Console.WriteLine("One new letter please.");
    }
}

while (lives > 0 && !HasWon())
{
    Console.WriteLine(MaskWord());
    char g = ReadGuess();
    guessed.Add(g);
    if (!secretLetters.Contains(g))
    {
        lives--;
        Console.WriteLine($"No {g}!");
    }
}
Console.WriteLine(HasWon() ? $"You win! It was {secret}" : $"Out of lives – it was {secret}");
