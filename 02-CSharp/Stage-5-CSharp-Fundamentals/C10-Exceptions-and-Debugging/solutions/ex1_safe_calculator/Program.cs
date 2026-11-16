static decimal Calculate(decimal a, string op, decimal b) => op switch
{
    "+" => a + b,
    "-" => a - b,
    "*" => a * b,
    "/" => a / b,
    _ => throw new InvalidOperationException($"Unknown operator '{op}'"),
};

while (true)
{
    Console.Write("First number (or quit): ");
    string first = Console.ReadLine() ?? "quit";
    if (first == "quit") break;
    try
    {
        decimal a = decimal.Parse(first);
        Console.Write("Operator: ");
        string op = Console.ReadLine() ?? "";
        Console.Write("Second number: ");
        decimal b = decimal.Parse(Console.ReadLine() ?? "");
        Console.WriteLine($"= {Calculate(a, op, b)}");
    }
    catch (FormatException) { Console.WriteLine("Numbers only please."); }
    catch (DivideByZeroException) { Console.WriteLine("Can't divide by zero!"); }
    catch (InvalidOperationException ex) { Console.WriteLine(ex.Message); }
}
