const decimal GbpToEur = 1.17m;
const decimal GbpToUsd = 1.27m;

double ReadDouble(string prompt)
{
    while (true)
    {
        Console.Write(prompt);
        if (double.TryParse(Console.ReadLine(), out double v)) return v;
        Console.WriteLine("Please type a number.");
    }
}

// decimal for money: it stores 0.1 exactly. double for measurements: fast, and tiny errors don't matter.
Console.WriteLine($"Integer trap: 7 / 2 = {7 / 2}, but 7 / 2.0 = {7 / 2.0}");
string[] history = new string[5];
int count = 0;

while (true)
{
    Console.WriteLine("\n1) °C→°F 2) °F→°C 3) km→miles 4) miles→km 5) kg→stone 6) £→€ 7) £→$ 8) history 0) quit");
    Console.Write("> ");
    string c = Console.ReadLine() ?? "0";
    if (c == "0") break;
    if (c == "8")
    {
        foreach (string? h in history) if (h != null) Console.WriteLine("  " + h);
        continue;
    }
    double v = ReadDouble("Value: ");
    string result = c switch
    {
        "1" => $"{v}°C = {v * 9 / 5 + 32:F1}°F",
        "2" => $"{v}°F = {(v - 32) * 5 / 9:F1}°C",
        "3" => $"{v} km = {v * 0.621371:F2} miles",
        "4" => $"{v} miles = {v / 0.621371:F2} km",
        "5" => $"{v} kg = {v / 6.35029:F2} stone",
        "6" => $"£{v:F2} = €{(decimal)v * GbpToEur:F2}",
        "7" => $"£{v:F2} = ${(decimal)v * GbpToUsd:F2}",
        _ => "Unknown option",
    };
    Console.WriteLine(result);
    history[count % 5] = result;
    count++;
}
