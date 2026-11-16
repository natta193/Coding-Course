var grades = new Dictionary<string, List<int>>
{
    ["Ana"] = new List<int> { 78, 85, 92 },
    ["Ben"] = new List<int> { 65, 70, 58 },
    ["Cai"] = new List<int> { 88, 91, 95 },
    ["Dev"] = new List<int> { 55, 61, 72 },
};

string top = "";
double best = -1;
foreach (var (name, scores) in grades)
{
    double avg = scores.Average();
    Console.WriteLine($"{name,-5} {avg,6:F1}");
    if (avg > best)
    {
        best = avg;
        top = name;
    }
}
Console.WriteLine($"Top student: {top} ({best:F1})");
