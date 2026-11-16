// MathsLib/Calc.cs
public static class Calc
{
    public static bool IsLeap(int y) =>
        (y % 4 == 0 && y % 100 != 0) || y % 400 == 0;
}

// MathsLib.Tests/CalcTests.cs
public class CalcTests
{
    [Fact]
    public void Year2024IsLeap() => Assert.True(Calc.IsLeap(2024));

    [Fact]
    public void Year1900IsNotLeap() => Assert.False(Calc.IsLeap(1900));
}
