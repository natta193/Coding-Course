var acc = new Account("1234");
while (true)
{
    Console.Write("\n1) balance 2) deposit 3) withdraw 4) quit: ");
    string c = Console.ReadLine() ?? "4";
    if (c == "4" || c == "") break;
    try
    {
        acc.Unlock(() => { Console.Write("PIN: "); return Console.ReadLine() ?? ""; });
        if (c == "1") Console.WriteLine($"Balance: £{acc.Balance:F2}");
        else
        {
            Console.Write("Amount: £");
            if (!decimal.TryParse(Console.ReadLine(), out decimal amt)) { Console.WriteLine("Not a number."); continue; }
            if (c == "2") acc.Deposit(amt); else acc.Withdraw(amt);
            Console.WriteLine($"Done. Balance £{acc.Balance:F2}");
        }
    }
    catch (InsufficientFundsException ex) { Console.WriteLine($"Declined: you're short by £{ex.Shortfall:F2}"); }
    catch (ArgumentOutOfRangeException) { Console.WriteLine("Amounts must be more than zero."); }
    catch (AccountLockedException) { Console.WriteLine("Account locked – call the bank!"); break; }
}

public class InsufficientFundsException : Exception
{
    public decimal Shortfall { get; }
    public InsufficientFundsException(decimal s) : base($"Short by {s}") => Shortfall = s;
}

public class AccountLockedException : Exception
{
    public AccountLockedException() : base("Too many wrong PINs") { }
}

public class Account
{
    private const string LogFile = "transactions.log";
    private readonly string pin;
    private bool locked, unlocked;
    public decimal Balance { get; private set; } = 50m;

    public Account(string pin) => this.pin = pin;

    public void Unlock(Func<string> askPin)
    {
        if (locked) throw new AccountLockedException();
        if (unlocked) return;
        for (int i = 0; i < 3; i++)
        {
            if (askPin() == pin) { unlocked = true; return; }
            Console.WriteLine("Wrong PIN");
        }
        locked = true;
        Log("LOCKED", 0);
        throw new AccountLockedException();
    }

    public void Deposit(decimal amount)
    {
        if (amount <= 0) throw new ArgumentOutOfRangeException(nameof(amount));
        Balance += amount;
        Log("DEPOSIT", amount);
    }

    public void Withdraw(decimal amount)
    {
        if (amount <= 0) throw new ArgumentOutOfRangeException(nameof(amount));
        if (amount > Balance) throw new InsufficientFundsException(amount - Balance);
        Balance -= amount;
        Log("WITHDRAW", amount);
    }

    private void Log(string kind, decimal amount)
    {
        try { File.AppendAllText(LogFile, $"{DateTime.Now:yyyy-MM-dd HH:mm:ss},{kind},{amount},{Balance}{Environment.NewLine}"); }
        catch (IOException ex) { Console.WriteLine("(couldn't write log: " + ex.Message + ")"); }
    }
}
