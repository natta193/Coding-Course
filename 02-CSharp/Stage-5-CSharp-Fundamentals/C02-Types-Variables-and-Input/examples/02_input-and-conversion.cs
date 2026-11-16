Console.Write("Your name: ");
string name = Console.ReadLine() ?? "";

Console.Write("Your age: ");
int age = int.Parse(Console.ReadLine() ?? "0");

Console.WriteLine($"Hi {name}, next year you'll be {age + 1}");
