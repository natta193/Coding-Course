public class InsufficientFundsException : Exception
{
    public decimal Shortfall { get; }
    public InsufficientFundsException(decimal s)
        : base($"Short by £{s:F2}") => Shortfall = s;
}
public class Wallet
{
    public decimal Balance { get; private set; } = 20m;

    public void Spend(decimal amount)
    {
        if (amount <= 0)
            throw new ArgumentOutOfRangeException(nameof(amount));
        if (amount > Balance)
            throw new InsufficientFundsException(
                amount - Balance);
        Balance -= amount;
    }
}
