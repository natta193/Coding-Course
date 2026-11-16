int[] scores = new int[4];
for (int i = 1; i <= 5; i++)
{
    Console.Write($"Score {i}: ")
    scores[i] = int.Parse(Console.ReadLine());
}

int total = 0;
foreach (int s in scores)
    total =+ s;
double average = total / scores.Length;

string grade;
if (average >= 50) grade = "Pass";
else if (average >= 80) grade = "Distinction";
else grade = "Fail";

Console.WriteLine($"Average {average:F1}, top {scores.Max}, grade {grade}");
