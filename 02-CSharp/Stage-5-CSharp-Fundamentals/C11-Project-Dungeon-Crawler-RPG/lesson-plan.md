# C11 · Project – Dungeon Crawler RPG

**Stage:** CSharp Fundamentals  
**Session type:** Project session (≈60 min)  
**Slides:** `C11-Project-Dungeon-Crawler-RPG.pptx`

_A turn-based console RPG built from classes, interfaces and collections (2–3 sessions)_

## Learning goals
- Design a class hierarchy before coding (class diagram)
- Use inheritance, interfaces and polymorphism in a real program
- Manage game state with collections
- Build in milestones and keep the program compiling at every step

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 10 min — brief + plan this project together on paper
- 30 min — build milestone 1–2 together (he drives the keyboard)
- 5 min — agree which milestones he'll do at home (the take-home)

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What's the difference between throw and catch?  
   **Answer:** throw raises an exception; catch handles one
2. When should you use TryParse instead of try/catch?  
   **Answer:** When failure is expected, like user input
3. What's F10 vs F11 in the debugger?  
   **Answer:** F10 steps over a line; F11 steps into a method call

## Slide outline & tutor notes

**3. The brief**

**4. Design: classes**  
Get him to draw the class diagram on paper before any code. Interfaces as dashed arrows, inheritance as solid arrows.

**5. Core of the battle loop**

**6. Milestones**

## 🏠 Take-home project: Dungeon Crawler Sprints
**Time:** 2 hours per gap (2–3 gaps) over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Push your dungeon crawler forward one milestone per gap, then add your own twist.

**Milestones**
1. Gap 1: M1–M2 (characters, hero classes, items via IItem)
2. Gap 2: M3–M4 (rooms, map, XP, floors, boss)
3. Gap 3: your twist – a shop, poison, a new hero class – and the Stage 5 checkpoint

**Stretch:** Save and load the game (a simple text format now, JSON after C15).

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Dungeon Crawler – reference game  (★★★ stretch)
File: `exercises/project_dungeon/Program.cs`

A compact but complete reference version: 3 hero classes, enemies, items via an interface, a 4×4 room grid per floor, XP and levels, and a boss. Use it for ideas – your version should have your own twist.

### Stage 5 checkpoint  (★★☆ core)
File: `exercises/stage5_checkpoint/Program.cs`

Eight C# questions covering types, control flow, methods, collections, strings, classes and exceptions. Compiles = half the battle!

## Optional extras (if he wants more)
- Add your own twist to the dungeon crawler (a shop? a new hero class? poison?)
- Finish the Stage 5 checkpoint
