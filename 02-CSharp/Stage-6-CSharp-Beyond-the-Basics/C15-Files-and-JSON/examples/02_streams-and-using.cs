using (var writer = new StreamWriter("big.csv"))
{
    writer.WriteLine("id,value");
    for (int i = 0; i < 100_000; i++)
        writer.WriteLine($"{i},{i * i}");
}   // file closed here automatically

using var reader = new StreamReader("big.csv");
string? line;
int count = 0;
while ((line = reader.ReadLine()) != null)
    count++;
Console.WriteLine($"{count} lines");
