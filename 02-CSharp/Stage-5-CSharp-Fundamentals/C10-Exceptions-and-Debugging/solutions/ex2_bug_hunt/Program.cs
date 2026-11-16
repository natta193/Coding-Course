int[] scores = new int[5];                          // 1 LOGIC/RUNTIME: array was size 4
for (int i = 0; i < 5; i++)                         // 2 RUNTIME: index 5 out of range; arrays start at 0
{
    Console.Write($"Score {i + 1}: ");              // 3 COMPILE: missing semicolon
    scores[i] = int.TryParse(Console.ReadLine(), out int v) ? v : 0;   // 4 RUNTIME: Parse crashed on bad input/null
}

int total = 0;
foreach (int s in scores)
    total += s;                                     // 5 LOGIC: =+ assigned +s
double average = (double)total / scores.Length;     // 6 LOGIC: int division lost the decimals

string grade;
if (average >= 80) grade = "Distinction";           // 7 LOGIC: higher band must be checked first
else if (average >= 50) grade = "Pass";
else grade = "Fail";

Console.WriteLine($"Average {average:F1}, top {scores.Max()}, grade {grade}");   // 8 COMPILE: Max is a method – Max()
