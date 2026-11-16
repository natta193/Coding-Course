# C13 · Generics and Collections

**Stage:** CSharp Beyond the Basics  
**Session type:** Lesson (≈60 min)  
**Slides:** `C13-Generics-and-Collections.pptx`

_Writing code that works for any type – plus Stack, Queue, HashSet and friends_

## Learning goals
- Explain what <T> means and why generics exist
- Write generic methods and generic classes
- Use Stack<T>, Queue<T>, HashSet<T>, LinkedList<T> and PriorityQueue
- Choose collections by their Big-O

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. Value type or reference type: List<int>?  
   **Answer:** Reference type (it's a class)
2. What does `x ??= 5` do?  
   **Answer:** Sets x to 5 only if x is null
3. When would you use a struct?  
   **Answer:** Small, simple data where copying is fine – points, colours, vectors

## Slide outline & tutor notes

**3. Why generics?**

**4. Generic methods**

**5. A generic class**

**6. Stack, Queue, HashSet**

**7. Choosing a collection by Big-O**

**8. Undo/redo editor**

**9. Generics quiz**
- In `List<T>`, what is T? → **A type parameter – the element type, filled in when used**
- What does `where T : IComparable<T>` mean? → **T must be a type that can be compared with CompareTo**
- Which collection: is this username taken? → **HashSet<string>**
- Which collection: process jobs in order of arrival? → **Queue<T>**
- What does `default` give for an int? A reference type? → **0; null**

## 🏠 Take-home project: Generic Leaderboard
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Write a reusable, generic leaderboard class that works for any kind of entry – then use it for two different games.

**Milestones**
1. `class Leaderboard<T> where T : IComparable<T>` holding at most N entries (N set in the constructor)
2. `Add(T entry)` keeps it sorted best-first and drops the worst if it's over N; returns the position (or -1 if it didn't make it)
3. Implement `IEnumerable<T>` (or just expose `IReadOnlyList<T> Entries`) so you can foreach over it
4. Two record types implementing `IComparable<T>`: `TimeEntry` (fastest wins) and `ScoreEntry` (highest wins, ties by name)
5. Fill one board with 20 random race times and one with 20 random scores; print the top 5 of each

**Stretch:** Add a generic `Top<T>(IEnumerable<T> items, int n, Func<T, double> score)` method that doesn't need IComparable at all.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Generic helpers  (★☆☆ warm-up)
File: `exercises/ex1_generic_stats/Program.cs`

Write generic methods: `Largest<T>`, `Smallest<T>`, `CountWhere<T>(List<T> items, Func<T, bool> test)` and `Shuffle<T>(List<T> items)` (Fisher–Yates). Test with ints, strings and doubles.

### Your own generic Stack<T>  (★★☆ core)
File: `exercises/ex2_generic_stack/Program.cs`

Implement `MyStack<T>` using an array that doubles in size when full (that's how List<T> works inside!). Push, Pop (throw InvalidOperationException when empty), Peek, Count, IsEmpty. Test it with ints and strings, and use it for the bracket checker.

### Shortest route with PriorityQueue  (★★★ stretch)
File: `exercises/ex3_dijkstra/Program.cs`

Store a weighted graph of towns (Dictionary<string, List<(string To, int Km)>>). Implement Dijkstra's algorithm with `PriorityQueue<string, int>` to find the shortest distance and route between two towns.

## Optional extras (if he wants more)
- Use `SortedDictionary<int, string>` to make a leaderboard that stays sorted as you add scores
- Read the source code of List<T> on source.dot.net – find the line where it doubles its array
