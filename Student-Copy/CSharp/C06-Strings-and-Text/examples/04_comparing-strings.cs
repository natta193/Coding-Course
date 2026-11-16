string a = "Hello", b = "hello";

Console.WriteLine(a == b);                       // False
Console.WriteLine(a.Equals(b, StringComparison.OrdinalIgnoreCase)); // True
Console.WriteLine(string.Compare("apple", "banana"));               // -1 (comes before)
Console.WriteLine(string.IsNullOrWhiteSpace("   "));                // True

string name = "Ana";
string verbatim = @"C:\Users\Ana\code";          // no escapes
string multi = """
    Multi-line
    raw string
    """;
