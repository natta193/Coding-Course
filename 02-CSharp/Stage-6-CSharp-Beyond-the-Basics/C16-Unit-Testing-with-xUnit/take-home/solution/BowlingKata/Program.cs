static int Score(int[] rolls)
{
    int score = 0, i = 0;
    for (int frame = 0; frame < 10; frame++)
    {
        if (rolls[i] == 10)                       // strike
        {
            score += 10 + rolls[i + 1] + rolls[i + 2];
            i += 1;
        }
        else if (rolls[i] + rolls[i + 1] == 10)   // spare
        {
            score += 10 + rolls[i + 2];
            i += 2;
        }
        else
        {
            score += rolls[i] + rolls[i + 1];
            i += 2;
        }
    }
    return score;
}

static int[] Repeat(int pins, int times) => Enumerable.Repeat(pins, times).ToArray();

int passed = 0, failed = 0;
void Check(string name, bool ok)
{
    if (ok) passed++; else { failed++; Console.WriteLine($"FAIL: {name}"); }
}

Check("gutter game", Score(new int[20]) == 0);
Check("all ones", Score(Repeat(1, 20)) == 20);
Check("one spare", Score(new[] { 5, 5, 3 }.Concat(new int[17]).ToArray()) == 16);
Check("one strike", Score(new[] { 10, 3, 4 }.Concat(new int[16]).ToArray()) == 24);
Check("perfect game", Score(Repeat(10, 12)) == 300);
Check("all spares of 5", Score(Repeat(5, 21)) == 150);
Check("strike in frame 10", Score(new int[18].Concat(new[] { 10, 10, 10 }).ToArray()) == 30);
Check("spare in frame 10", Score(new int[18].Concat(new[] { 7, 3, 5 }).ToArray()) == 15);
Check("nines and misses", Score(Enumerable.Range(0, 10).SelectMany(_ => new[] { 9, 0 }).ToArray()) == 90);

Console.WriteLine($"{passed} passed, {failed} failed");
