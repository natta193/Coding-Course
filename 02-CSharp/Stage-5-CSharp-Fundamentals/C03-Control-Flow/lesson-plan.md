# C03 · Control Flow

**Stage:** CSharp Fundamentals  
**Session type:** Lesson (≈60 min)  
**Slides:** `C03-Control-Flow.pptx`

_if, switch, and four kinds of loop_

## Learning goals
- Write if / else if / else with &&, || and !
- Use switch statements and switch expressions
- Write for, while, do-while and foreach loops
- Use break, continue and the ternary operator

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What's `7 / 2` in C#?  
   **Answer:** 3 (integer division)
2. How do you safely convert "42" to an int?  
   **Answer:** int.TryParse(text, out int n)
3. What's the difference between var and dynamic typing?  
   **Answer:** var is still statically typed – the compiler infers the type once and it never changes

## Slide outline & tutor notes

**3. if / else if / else**

**4. switch**

**5. Switch expressions (modern C#)**

**6. Loops**

**7. FizzBuzz, C# style**  
Tuple patterns in switch expressions are neat C# – he'll like it.

**8. Control flow quiz**
- C# for Python's `for i in range(1, 11):` → **for (int i = 1; i <= 10; i++)**
- When does a do-while check its condition? → **After running the body, so it always runs at least once**
- What does `_` mean in a switch expression? → **Default – any other value**
- What's `x > 5 ? "big" : "small"` when x = 3? → **"small"**
- What happens if you forget `break` in a switch case? → **Compile error – C# doesn't allow falling through to the next case**

## 🏠 Take-home project: Number Games Pack
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

A pack of maths mini-games, each in its own loop, chosen from a menu with a switch.

**Milestones**
1. Times-table sprint: 10 random questions, count correct, time it with `Stopwatch`
2. Prime or not? The computer shows a number 2–100; you type y/n; 10 rounds
3. Countdown: pick a target and 3 numbers; the player types an answer with + and * only (just check the result is right)
4. Use `for`, `while` and `do-while` at least once each, plus a switch expression for the menu
5. Keep a total score across all games for the session

**Stretch:** Add FizzBuzz as a game: the computer counts and you must type the right word for each number.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Higher or Lower in C#  (★☆☆ warm-up)
File: `exercises/ex1_higher_lower/Program.cs`

Port your P07 Higher or Lower game: `Random.Shared.Next(1, 101)` gives 1–100. Count guesses, use do-while, and ask to play again.

### Pattern printer  (★★☆ core)
File: `exercises/ex2_patterns/Program.cs`

Using nested for loops, print: a right triangle of *, a centred pyramid, a hollow square (stars only on the edges) and a multiplication grid with columns lined up using `{x,4}`.

### Rock-paper-scissors tournament  (★★★ stretch)
File: `exercises/ex3_rps/Program.cs`

Best of 5 against the computer. Use a switch expression to decide the winner from a tuple `(player, computer)`, keep score, validate input with do-while, and print a final summary.

## Optional extras (if he wants more)
- Port the Collatz program (P05) to C# – and time it for every start number up to 1,000,000
- Read about `goto` in C# and why nobody uses it
