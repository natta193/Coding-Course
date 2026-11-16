public class CalcTests
{
    [Theory]
    [InlineData(2024, true)]
    [InlineData(2023, false)]
    [InlineData(1900, false)]   // boundary: century
    [InlineData(2000, true)]    // boundary: 400 rule
    public void IsLeapWorks(int year, bool expected)
    {
        Assert.Equal(expected, Calc.IsLeap(year));
    }

    [Fact]
    public void DivideByZeroThrows() =>
        Assert.Throws<DivideByZeroException>(() => Calc.Divide(1, 0));
}
