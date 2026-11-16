var students = new List<Student>
{
    new("Ana", 13, 9, new[] { 78, 85, 92 }),
};

record Student(string Name, int Age, int Year, int[] Scores);
