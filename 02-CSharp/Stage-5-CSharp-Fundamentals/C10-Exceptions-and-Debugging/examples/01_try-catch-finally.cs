try
{
    Console.Write("Number: ");
    int n = int.Parse(Console.ReadLine() ?? "");
    Console.WriteLine(100 / n);
}
catch (FormatException)
{
    Console.WriteLine("That's not a number");
}
catch (DivideByZeroException)
{
    Console.WriteLine("Can't divide by zero");
}
catch (Exception ex)
{
    Console.WriteLine($"Other: {ex.Message}");
}
finally { Console.WriteLine("Always runs"); }
