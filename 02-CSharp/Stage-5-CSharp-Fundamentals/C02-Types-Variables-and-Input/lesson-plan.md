# C02 · Types, Variables and Input

**Stage:** CSharp Fundamentals  
**Session type:** Lesson (≈60 min)  
**Slides:** `C02-Types-Variables-and-Input.pptx`

_Static typing – telling the compiler exactly what kind of data you mean_

## Learning goals
- Declare variables with int, double, decimal, bool, char, string and var
- Explain static vs dynamic typing
- Read input with Console.ReadLine and convert with int.Parse / int.TryParse
- Use string interpolation, formatting and constants

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does a compiler do?  
   **Answer:** Translates the whole program into another form (IL/machine code) before it runs
2. What ends a C# statement?  
   **Answer:** A semicolon
3. C# for `f"Hi {name}"`?  
   **Answer:** $"Hi {name}"

## Slide outline & tutor notes

**3. Dynamic vs static typing**

**4. The main types**  
Link to P21: int is 32 bits, long 64 bits. Overflow is real – int.MaxValue + 1 wraps to a huge negative number. Show it!

**5. Input and conversion**  
The `string?` / null warnings come from Nullable being enabled. Don't go deep – just say ReadLine might return null and ?? gives a fallback.

**6. TryParse: conversion that can't crash**

**7. Formatting output**

**8. Casting between types**  
This is the #1 Python→C# bug. In Python 3, / always gives a float; in C#, int/int truncates. Make him predict `int avg = 7 / 2;` and `double avg = 7 / 2;` (both 3!).

**9. Port P02**

**10. Types quiz**
- Type for 3.14? → **double**
- Type for 'x'? → **char**
- What is `7 / 2` in C#? → **3 – integer division**
- What does `int.TryParse` return? → **A bool – true if it worked; the number goes in the out variable**
- Why use decimal for money? → **It stores decimal fractions exactly, so no 0.1 + 0.2 rounding errors**
- Can you do `var x = 5; x = "five";`? → **No – var x is an int, fixed at compile time**

## 🏠 Take-home project: Unit Converter Pro
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

A converter that can't be crashed by bad input, using C#'s types properly.

**Milestones**
1. A menu loop with at least 6 conversions: °C↔°F, km↔miles, kg↔stone, GBP→EUR/USD (make up rates as `const decimal`)
2. Read every number with `TryParse` – re-ask on bad input, never crash
3. Use `decimal` for money and `double` for everything else – comment why
4. Format output with `:F2`, `:N0` or `:C` as appropriate
5. Show the integer-division trap: print `7 / 2` and `7 / 2.0` with a comment explaining

**Stretch:** Keep a history of the last 5 conversions in an array and add a "history" menu option.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Bill splitter in C#  (★☆☆ warm-up)
File: `exercises/ex1_bill_splitter/Program.cs`

Port the P02 bill splitter: total, tip %, number of people. Use decimal for money and format with `:C` or `:F2`.

### ReadInt helper  (★★☆ core)
File: `exercises/ex2_safe_input/Program.cs`

Write a reusable method `ReadInt(string prompt, int min, int max)` that keeps asking until the user types a valid whole number in range. Use it to ask for age (1–120) and favourite number (1–100). (Methods properly in C04 – copy the shape for now.)

### Explore the limits  (★★★ stretch)
File: `exercises/ex3_overflow/Program.cs`

Print int.MinValue, int.MaxValue, long.MaxValue, double.MaxValue. Then show int overflow by adding 1 to int.MaxValue. Wrap it in `checked { }` and see what changes. Finally show why `0.1 + 0.2 == 0.3` is false for double but true for decimal.

## Optional extras (if he wants more)
- Port your P03 time converter (seconds → days/hours/minutes/seconds) to C#
- Find out the difference between `float` and `double`
