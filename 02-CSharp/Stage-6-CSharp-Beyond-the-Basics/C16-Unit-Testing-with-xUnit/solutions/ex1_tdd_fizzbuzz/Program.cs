static string FizzBuzz(int n) => (n % 3, n % 5) switch
{
    (0, 0) => "FizzBuzz",
    (0, _) => "Fizz",
    (_, 0) => "Buzz",
    _ => n.ToString(),
};

int passed = 0, failed = 0;
void Check(string name, bool ok)
{
    if (ok) passed++; else { failed++; Console.WriteLine($"FAIL: {name}"); }
}

Check("1 -> 1", FizzBuzz(1) == "1");
Check("3 -> Fizz", FizzBuzz(3) == "Fizz");
Check("5 -> Buzz", FizzBuzz(5) == "Buzz");
Check("15 -> FizzBuzz", FizzBuzz(15) == "FizzBuzz");
Check("30 -> FizzBuzz", FizzBuzz(30) == "FizzBuzz");
Check("98 -> 98", FizzBuzz(98) == "98");
Check("99 -> Fizz", FizzBuzz(99) == "Fizz");
Check("100 -> Buzz", FizzBuzz(100) == "Buzz");

Console.WriteLine($"{passed} passed, {failed} failed");

// xUnit version (in a test project):
// [Theory]
// [InlineData(1, "1")] [InlineData(3, "Fizz")] [InlineData(5, "Buzz")] [InlineData(15, "FizzBuzz")]
// public void FizzBuzzWorks(int n, string expected) => Assert.Equal(expected, Game.FizzBuzz(n));
