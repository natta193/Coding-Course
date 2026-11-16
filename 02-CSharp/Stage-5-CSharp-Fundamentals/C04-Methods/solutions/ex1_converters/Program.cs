static double CToF(double c) => c * 9 / 5 + 32;
static double FToC(double f) => (f - 32) * 5 / 9;
static double KmToMiles(double km) => km * 0.621371;
static double KgToStone(double kg) => kg / 6.35029;

Console.WriteLine("1) °C→°F  2) °F→°C  3) km→miles  4) kg→stone");
Console.Write("Choice: ");
string choice = Console.ReadLine() ?? "";
Console.Write("Value: ");
double v = double.Parse(Console.ReadLine() ?? "0");

string answer = choice switch
{
    "1" => $"{CToF(v):F1} °F",
    "2" => $"{FToC(v):F1} °C",
    "3" => $"{KmToMiles(v):F2} miles",
    "4" => $"{KgToStone(v):F2} stone",
    _ => "Unknown choice",
};
Console.WriteLine(answer);
