// TAKE-HOME PROJECT: TDD Kata: Bowling Scores
// After lesson C16 (Unit Testing with xUnit) - about 1–2 hours, in chunks over the next few days.
//
// A famous programming "kata" (practice exercise): score a game of ten-pin bowling –
// strictly test-first.
//
// Milestones (make each one work before starting the next):
//   [ ] 1. Rules: 10 frames; a strike (all 10 with the first ball) scores 10 + the next two
//          balls; a spare (10 with two balls) scores 10 + the next ball; frame 10 can have
//          bonus balls
//   [ ] 2. Write the tests FIRST with the mini runner: all gutters (0), all ones (20), one
//          spare, one strike, a perfect game (300), all spares of 5 (150)
//   [ ] 3. Then write static int Score(int[] rolls) – only enough code to make the next test
//          pass each time
//   [ ] 4. Refactor once all tests are green
//   [ ] 5. Add 3 tests of your own for weird cases (e.g. a strike in frame 10)
//
// Stretch: Move it into a real xUnit project with [Theory] + [InlineData] for each case.
//
// Bring it to the next session - working or stuck, both are fine.

static int Score(int[] rolls) => 0;

int passed = 0, failed = 0;
void Check(string name, bool ok)
{
    if (ok) passed++; else { failed++; Console.WriteLine($"FAIL: {name}"); }
}

Check("gutter game", Score(new int[20]) == 0);

Console.WriteLine($"{passed} passed, {failed} failed");
