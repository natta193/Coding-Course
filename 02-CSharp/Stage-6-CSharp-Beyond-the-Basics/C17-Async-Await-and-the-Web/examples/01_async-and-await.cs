static async Task<string> MakeTea()
{
    Console.WriteLine("Kettle on...");
    await Task.Delay(2000);   // wait 2s, not blocking
    return "Tea ☕";
}

static async Task<string> MakeToast()
{
    Console.WriteLine("Toast in...");
    await Task.Delay(1500);
    return "Toast 🍞";
}

var tea = MakeTea();       // both start now
var toast = MakeToast();
// ~2s total, not 3.5s:
Console.WriteLine($"{await tea} and {await toast}");
