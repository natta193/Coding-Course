var accounts = new List<BankAccount> { new("Ana"), new("Ben"), new("Cai") };
accounts[0].Deposit(100);
accounts[1].Deposit(50);
accounts[1].Withdraw(80);
accounts[2].Deposit(1000);
accounts[2].Withdraw(250);
BankAccount.InterestRate = 0.05m;
foreach (var a in accounts)
{
    a.AddInterest();
    a.PrintStatement();
}

public class BankAccount
{
    private decimal balance;
    private readonly List<string> history = new();

    public static decimal InterestRate { get; set; } = 0.02m;
    public string Owner { get; }
    public decimal Balance => balance;

    public BankAccount(string owner) => Owner = owner;

    public void Deposit(decimal amount)
    {
        if (amount <= 0) throw new ArgumentException("Deposit must be positive");
        balance += amount;
        history.Add($"Deposit  {amount,8:F2}  -> {balance,8:F2}");
    }

    public bool Withdraw(decimal amount)
    {
        if (amount > balance)
        {
            history.Add($"DECLINED {amount,8:F2}");
            return false;
        }
        balance -= amount;
        history.Add($"Withdraw {amount,8:F2}  -> {balance,8:F2}");
        return true;
    }

    public void AddInterest()
    {
        decimal interest = Math.Round(balance * InterestRate, 2);
        balance += interest;
        history.Add($"Interest {interest,8:F2}  -> {balance,8:F2}");
    }

    public void PrintStatement()
    {
        Console.WriteLine($"--- {this} ---");
        history.ForEach(Console.WriteLine);
    }

    public override string ToString() => $"{Owner}: £{Balance:F2}";
}
