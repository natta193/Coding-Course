var ages = new Dictionary<string, int>
{
    ["Ana"] = 13,
    ["Ben"] = 15,
};
ages["Cai"] = 12;                 // add or update
Console.WriteLine(ages["Ben"]);   // 15

if (ages.TryGetValue("Zoe", out int zoeAge))
    Console.WriteLine(zoeAge);
else
    Console.WriteLine("No Zoe");  // ages["Zoe"] would throw!

foreach (var (name, age) in ages)
    Console.WriteLine($"{name}: {age}");
