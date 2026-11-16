# C16 · Unit Testing with xUnit

**Stage:** CSharp Beyond the Basics  
**Session type:** Lesson (≈60 min)  
**Slides:** `C16-Unit-Testing-with-xUnit.pptx`

_Professional testing – test projects, Facts, Theories and test-driven development_

## Learning goals
- Create a solution with a class library, a console app and an xUnit test project
- Write [Fact] and [Theory] tests with Assert
- Follow the red → green → refactor cycle (TDD)
- Design code so it's easy to test

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does `using` do around a StreamWriter?  
   **Answer:** Closes/disposes it automatically at the end, even on errors
2. How do you turn an object into JSON?  
   **Answer:** JsonSerializer.Serialize(obj)
3. Which test data types did we use in P34?  
   **Answer:** Normal, boundary, invalid, erroneous

## Slide outline & tutor notes

**3. Setting up a solution**  
This needs internet for NuGet the first time (xUnit packages). The exercises in this lesson also include a tiny built-in test runner so they work without setup.

**4. Facts**

**5. Theories: one test, many inputs**

**6. Test-driven development (TDD)**

**7. Designing testable code**  
Arrange-Act-Assert is the standard test layout. Show it: set up objects, call the method, check the result.

**8. Test your bank account**

**9. Testing quiz**
- Fact vs Theory? → **Fact is one fixed test; Theory runs the same test with several sets of data**
- How do you test that code throws? → **Assert.Throws<ExceptionType>(() => ...)**
- What are the three steps of TDD? → **Red (failing test), Green (make it pass), Refactor**
- Why avoid Console.ReadLine inside logic methods? → **It makes them hard to test automatically – keep logic pure**
- What are the three parts of a test (AAA)? → **Arrange, Act, Assert**

## 🏠 Take-home project: TDD Kata: Bowling Scores
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

A famous programming "kata" (practice exercise): score a game of ten-pin bowling – strictly test-first.

**Milestones**
1. Rules: 10 frames; a strike (all 10 with the first ball) scores 10 + the next two balls; a spare (10 with two balls) scores 10 + the next ball; frame 10 can have bonus balls
2. Write the tests FIRST with the mini runner: all gutters (0), all ones (20), one spare, one strike, a perfect game (300), all spares of 5 (150)
3. Then write `static int Score(int[] rolls)` – only enough code to make the next test pass each time
4. Refactor once all tests are green
5. Add 3 tests of your own for weird cases (e.g. a strike in frame 10)

**Stretch:** Move it into a real xUnit project with `[Theory]` + `[InlineData]` for each case.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### TDD FizzBuzz  (★☆☆ warm-up)
File: `exercises/ex1_tdd_fizzbuzz/Program.cs`

Use the mini test runner in the starter (it works without xUnit). Write tests first for FizzBuzz(n) returning a string, watch them fail, then implement it. Then do the same in a real xUnit project.

### Test your algorithms  (★★☆ core)
File: `exercises/ex2_test_sorts/Program.cs`

Port merge sort and binary search to C# as static methods, then test them with the mini runner: empty, single item, duplicates, negatives, sorted, reversed, and 200 random arrays compared with `Array.Sort`.

### Make a game testable  (★★★ stretch)
File: `exercises/ex3_testable_game/Program.cs`

Refactor Rock-Paper-Scissors so the rules live in a pure static class `Rps` with `Winner(Move a, Move b)` (an enum) and the AI takes an injected `Random`. Write tests for all 9 combinations and check the AI is deterministic with a seeded Random. The console UI just calls the tested code.

## Optional extras (if he wants more)
- Set up a real xUnit project with `dotnet new xunit` and move one exercise's tests into it
- Write a test that finds a bug in your dungeon crawler (e.g. can HP go above MaxHp?)
