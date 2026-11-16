static Light Next(Light l) => l switch
{
    Light.Red => Light.RedAmber,
    Light.RedAmber => Light.Green,
    Light.Green => Light.Amber,
    _ => Light.Red,
};

static ConsoleColor ColourOf(Light l) => l switch
{
    Light.Red => ConsoleColor.Red,
    Light.Green => ConsoleColor.Green,
    _ => ConsoleColor.Yellow,
};

var north = new Junction("North road", Light.Green);
var east = new Junction("East road", Light.Red);
bool northActive = true;

for (int tick = 0; tick < 8; tick++)
{
    foreach (var j in new[] { north, east })
    {
        Console.ForegroundColor = ColourOf(j.State);
        Console.Write($"{j.Name}: {j.State,-9} ");
    }
    Console.ResetColor();
    Console.WriteLine();
    if (north.State == Light.Green && east.State == Light.Green)
        throw new InvalidOperationException("CRASH! Both green.");

    // only the "active" junction changes; when it reaches Red, the other one takes over
    if (northActive)
    {
        north = north with { State = Next(north.State) };
        if (north.State == Light.Red) northActive = false;
    }
    else
    {
        east = east with { State = Next(east.State) };
        if (east.State == Light.Red) northActive = true;
    }
    Thread.Sleep(200);
}

public enum Light { Red, RedAmber, Green, Amber }
public record Junction(string Name, Light State);
