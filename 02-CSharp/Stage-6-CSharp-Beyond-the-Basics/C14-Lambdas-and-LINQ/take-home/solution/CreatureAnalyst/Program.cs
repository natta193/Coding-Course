const string Data = """
name,type,hp,attack,speed,legendary
Emberfox,fire,45,60,90,false
Tidalon,water,80,55,40,false
Mossback,grass,95,40,25,false
Voltwing,electric,50,75,110,false
Pyrosaur,fire,85,95,60,true
Glacio,ice,70,65,55,false
Sparkit,electric,35,45,95,false
Leaflet,grass,40,35,70,false
Aquaroo,water,60,70,80,false
Cindermaw,fire,75,85,50,false
Frostfang,ice,65,80,85,true
Thornix,grass,70,75,45,false
Stormcaller,electric,90,100,105,true
Reefkin,water,55,50,65,false
Blazepup,fire,40,55,75,false
Snowdrift,ice,45,40,60,false
Bramblebeast,grass,110,70,30,false
Leviathorn,water,120,110,70,true
Zapling,electric,30,40,100,false
Magmora,fire,100,90,40,false
""";

var creatures = Data.Trim().Split('\n').Skip(1)
    .Select(line => line.Trim().Split(','))
    .Select(p => new Creature(p[0], p[1], int.Parse(p[2]), int.Parse(p[3]), int.Parse(p[4]), bool.Parse(p[5])))
    .ToList();

void Q(string question, object answer) => Console.WriteLine($"\n{question}\n  {answer}");

Q("Strongest attacker?", creatures.MaxBy(c => c.Attack)!.Name);
Q("Average hp per type?", string.Join(", ", creatures.GroupBy(c => c.Type).Select(g => $"{g.Key} {g.Average(c => c.Hp):F0}")));
Q("Legendaries by speed?", string.Join(", ", creatures.Where(c => c.Legendary).OrderByDescending(c => c.Speed).Select(c => c.Name)));
Q("Types with more than 3?", string.Join(", ", creatures.GroupBy(c => c.Type).Where(g => g.Count() > 3).Select(g => g.Key)));
Q("Fastest of each type?", string.Join(", ", creatures.GroupBy(c => c.Type).Select(g => g.MaxBy(c => c.Speed)!.Name)));
Q("Attack higher than hp?", string.Join(", ", creatures.Where(c => c.Attack > c.Hp).Select(c => c.Name)));
Q("Total hp of top 5 attackers?", creatures.OrderByDescending(c => c.Attack).Take(5).Sum(c => c.Hp));
Q("Any speed over 100?", creatures.Any(c => c.Speed > 100));

var querySyntax = from c in creatures where c.Type == "water" orderby c.Hp descending select c.Name;
Q("(query syntax) water types by hp:", string.Join(", ", querySyntax));

public record Creature(string Name, string Type, int Hp, int Attack, int Speed, bool Legendary);
