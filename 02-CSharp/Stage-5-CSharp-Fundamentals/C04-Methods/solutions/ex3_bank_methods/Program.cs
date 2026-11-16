static bool CheckPin(string correct)
{
    for (int i = 0; i < 3; i++)
    {
        Console.Write("PIN: ");
        if (Console.ReadLine() == correct) return true;
        Console.WriteLine("Incorrect");
    }
    return false;
}

static decimal ReadAmount(string prompt)
{
    Console.Write(prompt);
    return decimal.TryParse(Console.ReadLine(), out decimal a) && a > 0 ? a : 0;
}

static void Deposit(ref decimal balance) => balance += ReadAmount("Deposit: £");

static (bool ok, decimal newBalance) Withdraw(decimal balance)
{
    decimal amount = ReadAmount("Withdraw: £");
    if (amount > balance) return (false, balance);
    return (true, balance - amount);
}

decimal balance = 100m;
if (!CheckPin("1234"))
{
    Console.WriteLine("Card retained.");
    return;
}
while (true)
{
    Console.Write("1) Balance 2) Deposit 3) Withdraw 4) Quit: ");
    string c = Console.ReadLine() ?? "4";
    if (c == "1") Console.WriteLine($"£{balance:F2}");
    else if (c == "2") Deposit(ref balance);
    else if (c == "3")
    {
        var (ok, nb) = Withdraw(balance);
        if (!ok) Console.WriteLine("Insufficient funds");
        balance = nb;
    }
    else break;
}
