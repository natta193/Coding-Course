using System.Text;

static string Normalise(string s) => new string(s.ToLower().Where(char.IsLetter).OrderBy(c => c).ToArray());
static bool IsAnagram(string a, string b) => Normalise(a) == Normalise(b);

static string Acronym(string s)
{
    var sb = new StringBuilder();
    foreach (string w in s.Split(' ', StringSplitOptions.RemoveEmptyEntries))
        sb.Append(char.ToUpper(w[0]));
    return sb.ToString();
}

static string PigLatin(string sentence)
{
    var sb = new StringBuilder();
    foreach (string word in sentence.Split(' ', StringSplitOptions.RemoveEmptyEntries))
    {
        int end = word.Length;
        while (end > 0 && !char.IsLetter(word[end - 1])) end--;
        string core = word[..end], punct = word[end..];
        if (core.Length > 0) sb.Append(core[1..] + core[0] + "ay" + punct + " ");
        else sb.Append(word + " ");
    }
    return sb.ToString().TrimEnd();
}

static string Scramble(string w)
{
    char[] a = w.ToCharArray();
    do { Random.Shared.Shuffle(a); } while (new string(a) == w);
    return new string(a);
}

string[] words = { "python", "keyboard", "galaxy", "puzzle", "dragon", "planet" };
while (true)
{
    Console.Write("\n1) anagram 2) scramble game 3) acronym 4) pig latin 0) quit: ");
    string c = Console.ReadLine() ?? "0";
    if (c == "0") break;
    if (c == "1")
    {
        Console.Write("Word 1: "); string a = Console.ReadLine() ?? "";
        Console.Write("Word 2: "); string b = Console.ReadLine() ?? "";
        Console.WriteLine(IsAnagram(a, b) ? "Anagrams!" : "Not anagrams.");
    }
    else if (c == "2")
    {
        string w = words[Random.Shared.Next(words.Length)];
        Console.WriteLine($"Unscramble: {Scramble(w)}");
        bool won = false;
        for (int t = 0; t < 3 && !won; t++)
        {
            Console.Write("> ");
            won = (Console.ReadLine() ?? "").Trim().ToLower() == w;
        }
        Console.WriteLine(won ? "Correct!" : $"It was {w}");
    }
    else if (c == "3") { Console.Write("Phrase: "); Console.WriteLine(Acronym(Console.ReadLine() ?? "")); }
    else if (c == "4") { Console.Write("Sentence: "); Console.WriteLine(PigLatin(Console.ReadLine() ?? "")); }
}
