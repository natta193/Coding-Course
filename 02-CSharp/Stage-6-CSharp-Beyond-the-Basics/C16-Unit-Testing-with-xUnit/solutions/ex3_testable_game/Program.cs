int passed = 0, failed = 0;
void Check(string name, bool ok) { if (ok) passed++; else { failed++; Console.WriteLine("FAIL " + name); } }

var expected = new Dictionary<(Move, Move), Result>
{
    [(Move.Rock, Move.Rock)] = Result.Draw,
    [(Move.Rock, Move.Paper)] = Result.PlayerTwo,
    [(Move.Rock, Move.Scissors)] = Result.PlayerOne,
    [(Move.Paper, Move.Rock)] = Result.PlayerOne,
    [(Move.Paper, Move.Paper)] = Result.Draw,
    [(Move.Paper, Move.Scissors)] = Result.PlayerTwo,
    [(Move.Scissors, Move.Rock)] = Result.PlayerTwo,
    [(Move.Scissors, Move.Paper)] = Result.PlayerOne,
    [(Move.Scissors, Move.Scissors)] = Result.Draw,
};
foreach (var ((a, b), r) in expected) Check($"{a} v {b}", Rps.Winner(a, b) == r);

var r1 = new Random(42);
var r2 = new Random(42);
Check("seeded AI is repeatable", Enumerable.Range(0, 20).All(_ => Rps.AiMove(r1) == Rps.AiMove(r2)));
Console.WriteLine($"{passed} passed, {failed} failed");

public enum Move { Rock, Paper, Scissors }
public enum Result { Draw, PlayerOne, PlayerTwo }

public static class Rps
{
    public static Result Winner(Move a, Move b)
    {
        if (a == b) return Result.Draw;
        return (int)b == ((int)a + 2) % 3 ? Result.PlayerOne : Result.PlayerTwo;
    }

    public static Move AiMove(Random rng) => (Move)rng.Next(3);
}
