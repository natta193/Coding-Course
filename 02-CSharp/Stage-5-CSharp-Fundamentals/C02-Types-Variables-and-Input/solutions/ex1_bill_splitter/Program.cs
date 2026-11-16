Console.Write("Total bill: ");
decimal bill = decimal.Parse(Console.ReadLine() ?? "0");
Console.Write("Tip %: ");
decimal tip = decimal.Parse(Console.ReadLine() ?? "0");
Console.Write("People: ");
int people = int.Parse(Console.ReadLine() ?? "1");

decimal total = bill * (1 + tip / 100);
decimal each = total / people;
Console.WriteLine($"Total with tip: £{total:F2}");
Console.WriteLine($"Each pays: £{each:F2}");
