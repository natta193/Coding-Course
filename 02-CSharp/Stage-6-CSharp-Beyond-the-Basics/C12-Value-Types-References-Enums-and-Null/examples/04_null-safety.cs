string? nickname = null;           // ? = allowed to be null
string name = "Ana";               // not allowed to be null

Console.WriteLine(nickname?.Length);       // null, no crash
int len = nickname?.Length ?? 0;           // 0
nickname ??= "Ace";                        // assign if null
Console.WriteLine(nickname);               // Ace

Player? found = null;
Console.WriteLine(found?.Name ?? "Not found");

public record Player(string Name);
