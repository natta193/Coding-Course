Console.WriteLine("Paste a paragraph:");
string text = Console.ReadLine() ?? "";
if (string.IsNullOrWhiteSpace(text))
    text = "The quick brown fox jumps over the lazy dog. The dog sleeps. A fox is quick!";

char[] seps = { ' ', '.', ',', '!', '?', ';', ':' };
string[] words = text.Split(seps, StringSplitOptions.RemoveEmptyEntries);
int sentences = text.Count(ch => ch is '.' or '!' or '?');
double avgLen = words.Average(w => w.Length);

var counts = new Dictionary<string, int>();
foreach (string w in words)
{
    string key = w.ToLower();
    counts[key] = counts.GetValueOrDefault(key) + 1;
}

Console.WriteLine($"Words: {words.Length}, sentences: {sentences}, average length: {avgLen:F1}");
Console.WriteLine("Top words:");
foreach (var kv in counts.OrderByDescending(kv => kv.Value).Take(5))
    Console.WriteLine($"  {kv.Key}: {kv.Value}");

var title = new System.Text.StringBuilder();
foreach (string w in text.Split(' '))
    title.Append(w.Length > 0 ? char.ToUpper(w[0]) + w[1..].ToLower() + " " : " ");
Console.WriteLine(title.ToString().TrimEnd());
