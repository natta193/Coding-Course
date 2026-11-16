Console.WriteLine($"int:    {int.MinValue} to {int.MaxValue}");
Console.WriteLine($"long:   up to {long.MaxValue}");
Console.WriteLine($"double: up to {double.MaxValue}");

int big = int.MaxValue;
big = big + 1;
Console.WriteLine($"int.MaxValue + 1 = {big}   (overflow wrapped around!)");

try
{
    int x = int.MaxValue;
    x = checked(x + 1);
}
catch (OverflowException)
{
    Console.WriteLine("checked{} turned the silent overflow into an exception");
}

Console.WriteLine($"double:  0.1 + 0.2 == 0.3 ? {0.1 + 0.2 == 0.3}");
Console.WriteLine($"decimal: 0.1 + 0.2 == 0.3 ? {0.1m + 0.2m == 0.3m}");
