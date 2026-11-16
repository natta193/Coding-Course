static bool IsPalindrome(string s)
{
    var clean = new System.Text.StringBuilder();
    foreach (char ch in s)
        if (char.IsLetterOrDigit(ch)) clean.Append(char.ToLower(ch));
    string t = clean.ToString();
    for (int i = 0; i < t.Length / 2; i++)
        if (t[i] != t[t.Length - 1 - i]) return false;
    return true;
}

foreach (string test in new[] { "Racecar", "Never odd or even", "A man, a plan, a canal: Panama", "C#" })
    Console.WriteLine($"{test,-35} {IsPalindrome(test)}");
