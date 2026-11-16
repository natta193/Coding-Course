public enum Direction { North, East, South, West }
public enum Difficulty { Easy = 1, Normal = 2, Hard = 3 }

Direction d = Direction.East;
if (d == Direction.East) Console.WriteLine("Heading east");

string msg = d switch
{
    Direction.North => "Up",
    Direction.South => "Down",
    _ => "Sideways",
};

foreach (var level in Enum.GetValues<Difficulty>())
    Console.WriteLine($"{level} = {(int)level}");
