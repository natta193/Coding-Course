# C01 · Hello, C#

**Stage:** CSharp Fundamentals  
**Session type:** Lesson (≈60 min)  
**Slides:** `C01-Hello-C.pptx`

_A new language – compiled, statically typed, and the language of Unity_

## Learning goals
- Install the .NET SDK and the C# Dev Kit for VS Code
- Create, build and run a console app with the dotnet command
- Explain compiled vs interpreted languages
- Write output with Console.WriteLine and spot C#'s syntax rules

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does Git's `commit` do?  
   **Answer:** Saves a snapshot of the staged changes with a message
2. Name the five stages of the software development lifecycle  
   **Answer:** Analysis, design, implementation, testing, evaluation
3. What's the difference between a class and an object?  
   **Answer:** A class is a blueprint; an object is an instance made from it

## Slide outline & tutor notes

**3. Why C#?**  
Reassure him: every concept from Python carries over. This stage is mostly "same idea, new syntax" plus types and stricter OOP.

**4. Interpreted vs compiled**  
GCSE: translators = compilers, interpreters, assemblers. Strictly, C# compiles to Intermediate Language and the .NET runtime JIT-compiles that to machine code. Python also compiles to bytecode – the line is blurrier than exams suggest.

**5. Getting set up**

**6. Hello, World**

**7. Blocks use braces, not indentation**

**8. Python → C# cheat sheet**

**9. Port it**  
C# compiler errors have codes like CS1002 (; expected). Teach him to read the line number and the code – googling "CS1002" is a legit strategy.

**10. C# basics quiz**
- What ends every C# statement? → **A semicolon ;**
- What marks a block of code in C#? → **Curly braces { }**
- What command builds and runs a project? → **dotnet run**
- What's C#'s version of Python's `and`? → **&&**
- Is C# compiled or interpreted? → **Compiled (to IL, then JIT-compiled to machine code)**

## 🏠 Take-home project: Port Your Greatest Hits
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Rewrite three of your favourite Stage 1 Python programs in C#. Notice every difference the compiler makes you deal with.

**Milestones**
1. Port your P01 "All About Me" poster (Console.WriteLine, colours with Console.ForegroundColor)
2. Port your P02 character creator (int.Parse for numbers, $"..." strings)
3. Port your P05 dice race (`Random.Shared.Next(1, 7)`, a while loop)
4. Keep a list (in comments at the top) of every compiler error you hit and what it meant
5. Time how long each port took compared with writing it in Python the first time

**Stretch:** Make the dice race use `Console.ReadKey()` so players just tap a key to roll.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Banner  (★☆☆ warm-up)
File: `exercises/ex1_banner/Program.cs`

Print a banner for your favourite game or team using Console.WriteLine, at least 6 lines tall. Use `Console.ForegroundColor = ConsoleColor.Cyan;` to add colour, and `Console.ResetColor();` at the end.

### Fix the compiler errors  (★★☆ core)
File: `exercises/ex2_spot_errors/Program.cs`

This program has 5 compile errors. Run `dotnet build`, read each error (line number + CS code), and fix them one by one.

### Python vs C# speed test  (★★★ stretch)
File: `exercises/ex3_timing/Program.cs`

Count how many numbers below 50,000,000 are divisible by 7 or 11, timing it with `System.Diagnostics.Stopwatch`. Then write the same loop in Python and time that. How many times faster is C#?

## Optional extras (if he wants more)
- Install .NET + C# Dev Kit on your own laptop and get Hello World running
- Rewrite your P01 name card program in C#
