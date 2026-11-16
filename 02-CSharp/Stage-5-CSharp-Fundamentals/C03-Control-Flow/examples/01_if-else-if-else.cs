int mark = 73;

if (mark >= 90)
{
    Console.WriteLine("Grade 9");
}
else if (mark >= 70 && mark < 90)
{
    Console.WriteLine("Grade 7-8");
}
else if (!(mark < 50))
{
    Console.WriteLine("Pass");
}
else
{
    Console.WriteLine("Try again");
}
