string word = "Python3";
foreach (char ch in word)
{
    if (char.IsUpper(ch)) Console.WriteLine($"{ch} is upper");
    if (char.IsDigit(ch)) Console.WriteLine($"{ch} is a digit");
}

char c = 'A';
int code = c;               // 65 – like ord()
char next = (char)(c + 1);  // 'B' – like chr()
Console.WriteLine(next);
