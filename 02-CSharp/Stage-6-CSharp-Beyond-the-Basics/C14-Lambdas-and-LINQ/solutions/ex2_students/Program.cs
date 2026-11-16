var students = new List<Student>
{
    new("Ana", 13, 9, new[] { 78, 85, 92 }),
    new("Ben", 14, 9, new[] { 65, 70, 58 }),
    new("Cai", 13, 9, new[] { 88, 91, 100 }),
    new("Dev", 15, 10, new[] { 55, 61, 72 }),
    new("Eli", 15, 10, new[] { 90, 84, 95 }),
    new("Fay", 16, 11, new[] { 73, 77, 81 }),
    new("Gus", 16, 11, new[] { 100, 62, 70 }),
    new("Hal", 12, 8, new[] { 81, 79, 88 }),
};

Console.WriteLine("Over 13: " + string.Join(", ", students.Where(s => s.Age > 13).Select(s => s.Name)));
Console.WriteLine("By average: " + string.Join(", ", students.OrderByDescending(s => s.Scores.Average()).Select(s => s.Name)));
Console.WriteLine("Top: " + students.MaxBy(s => s.Scores.Average())!.Name);
Console.WriteLine("Got 100: " + string.Join(", ", students.Where(s => s.Scores.Contains(100)).Select(s => s.Name)));

foreach (var g in students.GroupBy(s => s.Year).OrderBy(g => g.Key))
{
    var top = g.MaxBy(s => s.Scores.Average())!;
    Console.WriteLine($"Year {g.Key}: avg {g.Average(s => s.Scores.Average()):F1}, top {top.Name}");
}

static string Grade(double avg) => avg switch { >= 85 => "A", >= 70 => "B", >= 55 => "C", _ => "D" };
foreach (var s in students)
    Console.WriteLine($"{s.Name,-4} {s.Scores.Average(),6:F1} {Grade(s.Scores.Average())}");

record Student(string Name, int Age, int Year, int[] Scores);
