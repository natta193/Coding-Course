string s = "  Hello, World!  ";

Console.WriteLine(s.Trim());               // "Hello, World!"
Console.WriteLine(s.ToUpper());
Console.WriteLine(s.Replace("World", "C#"));
Console.WriteLine(s.Contains("World"));    // True
Console.WriteLine(s.IndexOf("World"));     // 9
Console.WriteLine(s.Trim().Substring(0, 5)); // Hello (start, length)
Console.WriteLine(s.Trim()[7..12]);        // World (range, like slicing)
Console.WriteLine(s.Length);
string[] words = "a,b,c".Split(',');
Console.WriteLine(string.Join(" | ", words));
