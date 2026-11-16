static string Power(double x, int exp = 2)
{
    return $"{x}^{exp} = {Math.Pow(x, exp)}";
}

Console.WriteLine(Power(5));            // 5^2 = 25
Console.WriteLine(Power(2, 10));        // 2^10 = 1024
Console.WriteLine(Power(exp: 3, x: 4)); // 4^3 = 64
