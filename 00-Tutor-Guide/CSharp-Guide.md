# C# Tutor Guide (Stages 5–6, C01–C20)

## Overview
- 20 lessons, same rhythm as Python: 1 h session + 1–2 h take-home.
- Stage 5 Fundamentals (types, methods, collections, classes, interfaces, exceptions) → Stage 6 (records/enums, generics, LINQ, JSON, xUnit, async, Unity).
- Mostly "same idea, new syntax" – slides pair Python with C#. Biggest traps: static types, `int / int`, `{ }` + `;`.
- ⭐ = project lesson (C07, C11, C20); C20 runs 4–6 sessions and ends with a graduation demo.
- ~13 weeks. Every console solution compiles and runs on .NET 8; Unity scripts (C18–C20) need the editor.

```
<stage>/<lesson>/
  <lesson>.pptx      slides – answers + tutor notes in speaker notes
  lesson-plan.md     timings, recap/quiz answers, tutor notes, exercise briefs
  examples/          every code snippet on the slides
  exercises/ + solutions/       in-session practice (★ warm-up, ★★ core, ★★★ stretch)
  take-home/         starter with the brief at the top (for him), solution/ (for you)
```
C# exercises/take-homes are each a mini project (`Program.cs` + `.csproj`): `cd` in, `dotnet run`. Unity ones are plain `.cs` files – drop into `Assets/Scripts`, one MonoBehaviour per file, file name = class name.

## Setup (his laptop)
- .NET 8 SDK, VS Code + C# Dev Kit. His files are in `Student-Copy/CSharp/`.
- C16: first `dotnet new xunit` needs internet (NuGet).
- C18+: Unity Hub + Unity 6 LTS (several GB – install beforehand), Universal 2D template, VS Code as external editor. Scripts use the new Input System (`Keyboard.current`); for old tutorials set Active Input Handling → Both. Unity 6 uses `linearVelocity`, not `velocity`.

## Session format
| Min | What |
|---|---|
| 0–15 | Review take-home (he demos; you code-review) + 3 recap Qs (slide 2) |
| 15–50 | Teach from slides, live-coding. Stop at *Your turn*. One in-session exercise |
| 50–60 | Start the next take-home together: read the brief, get milestone 1 running |

⭐ Project sessions: 15 review · 10 plan on paper · 30 build M1–M2 · 5 agree take-home milestones.

## Tips
- C01 take-home ports his Python programs – the fastest way to feel the differences.
- Teach him to read compiler errors by code (CS1002, CS0103…) – Googling the code is legit.
- Debugger early (C10): breakpoints, watch, conditional breakpoints.
- Stage 5 checkpoint is in C11. Keep game rules out of `Console`/Unity code so they're testable (C16).
- Unity: grey-box first, polish last. A WebGL build on itch.io (parent OK) is a great finale.

## Project bank (extra builds)
- **After Stage 5:** port Battleships / Game of Life / a Sudoku solver from Python (compare speed) · console Snake (`KeyAvailable`, `SetCursorPosition`)
- **After Stage 6:** 48-hour game jam on a theme · physics sandbox (joints, explosions) · tower defence (waypoints, waves, LINQ targeting) · endless runner (procedural chunks)

## Syllabus

**Stage 5 · C# Fundamentals**

| # | Lesson | Covers |
|---|---|---|
| C01 | Hello, C# | compiled vs interpreted, dotnet CLI, syntax |
| C02 | Types, Variables and Input | static types, var, const, TryParse, formatting, int division |
| C03 | Control Flow | if, switch (+expressions), for/while/do/foreach |
| C04 | Methods | methods, void, overloading, ref/out, tuples |
| C05 | Arrays, Lists and Dictionaries | arrays, 2D arrays, List<T>, Dictionary |
| C06 | Strings and Text | string methods, chars, StringBuilder, comparison |
| C07 | ⭐ Project – Console Arcade | Console tricks, files, method structure |
| C08 | Classes, Objects and Properties | classes, access modifiers, properties, static |
| C09 | Inheritance, Abstract Classes and Interfaces | inheritance, virtual/override, abstract, interfaces |
| C10 | Exceptions and Debugging | try/catch/finally, custom exceptions, debugger |
| C11 | ⭐ Project – Dungeon Crawler RPG | class design, interfaces in practice; Stage 5 checkpoint |

**Stage 6 · C# Beyond the Basics**

| # | Lesson | Covers |
|---|---|---|
| C12 | Value Types, References, Enums and Null | value vs reference, structs, records, enums, null safety |
| C13 | Generics and Collections | generics, constraints, Stack/Queue/HashSet/PriorityQueue |
| C14 | Lambdas and LINQ | lambdas, Func/Action, LINQ, deferred execution |
| C15 | Files and JSON | File, streams, using, System.Text.Json |
| C16 | Unit Testing with xUnit | xUnit, Fact/Theory, TDD, testable design |
| C17 | Async, Await and the Web | async/await, Task.WhenAll, HttpClient |
| C18 | Unity I – GameObjects and Scripts | Unity editor, GameObjects, MonoBehaviour, deltaTime, input |
| C19 | Unity II – Physics, Prefabs and UI | Rigidbody2D, colliders, triggers, prefabs, UI |
| C20 | ⭐ Project – Unity Game and Graduation | events, architecture, polish, build, graduation |

## Lesson plans
Full per-lesson plans are in each folder's `lesson-plan.md`. At a glance:

**Stage 5 · C# Fundamentals**

| # | In-session (pick one) | Take-home |
|---|---|---|
| C01 | ★ Banner · ★★ Fix the compiler errors · ★★★ Python vs C# speed test | Port Your Greatest Hits (1–2 h) |
| C02 | ★ Bill splitter in C# · ★★ ReadInt helper · ★★★ Explore the limits | Unit Converter Pro (1–2 h) |
| C03 | ★ Higher or Lower in C# · ★★ Pattern printer · ★★★ Rock-paper-scissors tournament | Number Games Pack (1–2 h) |
| C04 | ★ Unit converter library · ★★ Recursion in C# · ★★★ ATM with ref | Dice Lab (1–2 h) |
| C05 | ★ Gradebook · ★★ Noughts and crosses · ★★★ Hangman in C# | Battleships (2 h) |
| C06 | ★ Palindrome checker · ★★ Text analyser · ★★★ Password strength meter | Word Games (1–2 h) |
| C07 | ★★ Console Arcade | Arcade Expansion (1–2 h) |
| C08 | ★ Rectangle class · ★★ Bank account · ★★★ Cards and Deck | Library System (1–2 h) |
| C09 | ★ Vehicle hierarchy · ★★ RPG party · ★★★ Shapes with IComparable | ASCII Shape Painter (1–2 h) |
| C10 | ★ Crash-proof calculator · ★★ Bug hunt · ★★★ Robust high-score file | Bulletproof Bank (1–2 h) |
| C11 | ★★★ Dungeon Crawler – reference game · ★★ Stage 5 checkpoint | Dungeon Crawler Sprints (2 h per gap (2–3 gaps)) |

**Stage 6 · C# Beyond the Basics**

| # | In-session (pick one) | Take-home |
|---|---|---|
| C12 | ★ Reference lab · ★★ Traffic light simulator · ★★★ Vector2 struct | The Card Game War (1–2 h) |
| C13 | ★ Generic helpers · ★★ Your own generic Stack<T> · ★★★ Shortest route with PriorityQueue | Generic Leaderboard (1–2 h) |
| C14 | ★ LINQ drills · ★★ Student database · ★★★ Word frequency pipeline | Creature Data Analyst (1–2 h) |
| C15 | ★ Journal app · ★★ Contacts app with JSON · ★★★ Versioned save system | Habit Tracker 2.0 (1–2 h) |
| C16 | ★ TDD FizzBuzz · ★★ Test your algorithms · ★★★ Make a game testable | TDD Kata: Bowling Scores (1–2 h) |
| C17 | ★ Breakfast simulator · ★★ Weather for 5 cities at once · ★★★ Async file scanner with progress | Async Horse Race (1–2 h) |
| C18 | ★ Smooth camera follow · ★★ Screen-bouncing sprite · ★★★ Solar system | Asteroid Drift (1–2 h) |
| C19 | ★ Coin and player scripts · ★★ Patrolling enemy · ★★★ Top-down shooter | Mini Platformer Level (2 h) |
| C20 | ★★★ Unity game starter scripts | Ship Your Game (2 h per gap (4–6 gaps)) |
