int day = 6;
string name = day switch
{
    1 => "Monday",
    6 or 7 => "Weekend!",
    > 7 => "Not a day",
    _ => "A weekday",
};

int score = 85;
string grade = score >= 70 ? "Pass" : "Fail";   // ternary
