public record Player(string Name, int Score);

var a = new Player("Ana", 120);
var b = new Player("Ana", 120);
Console.WriteLine(a == b);          // True – compares values!
Console.WriteLine(a);               // Player { Name = Ana, Score = 120 }

var c = a with { Score = 150 };     // copy with a change
Console.WriteLine(c.Score);         // 150
