static int Score(string pw, List<string> tips)
{
    int score = 0;
    if (pw.Length >= 8) score++; else tips.Add("Use at least 8 characters");
    if (pw.Length >= 12) score++; else tips.Add("12+ characters is much stronger");
    if (pw.Any(char.IsLower)) score++; else tips.Add("Add a lower-case letter");
    if (pw.Any(char.IsUpper)) score++; else tips.Add("Add an upper-case letter");
    if (pw.Any(char.IsDigit)) score++; else tips.Add("Add a digit");
    if (pw.Any(ch => !char.IsLetterOrDigit(ch))) score++; else tips.Add("Add a symbol like ! or #");
    foreach (string common in new[] { "password", "1234", "qwerty" })
        if (pw.ToLower().Contains(common)) { score--; tips.Add($"Avoid '{common}'"); }
    for (int i = 0; i + 2 < pw.Length; i++)
        if (pw[i] == pw[i + 1] && pw[i] == pw[i + 2]) { score--; tips.Add("Avoid repeated characters"); break; }
    return Math.Max(0, score);
}

Console.Write("Password: ");
string pw = Console.ReadLine() ?? "";
var tips = new List<string>();
int s = Score(pw, tips);
string label = s switch { <= 2 => "Weak", <= 4 => "OK", _ => "Strong" };
Console.WriteLine($"[{new string('█', s)}{new string('░', 6 - s)}] {label}");
foreach (string t in tips) Console.WriteLine($" • {t}");
