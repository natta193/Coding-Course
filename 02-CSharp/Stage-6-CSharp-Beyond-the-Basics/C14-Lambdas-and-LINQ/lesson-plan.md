# C14 · Lambdas and LINQ

**Stage:** CSharp Beyond the Basics  
**Session type:** Lesson (≈60 min)  
**Slides:** `C14-Lambdas-and-LINQ.pptx`

_Functions as values, and querying collections like a database_

## Learning goals
- Write lambda expressions and use Func and Action
- Query collections with Where, Select, OrderBy, GroupBy, Sum, Any, First
- Chain LINQ methods into readable pipelines
- Understand deferred execution

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does `<T>` mean in `List<T>`?  
   **Answer:** A type parameter – the element type
2. Stack or queue for undo?  
   **Answer:** Stack
3. What does HashSet.Add return if the item is already there?  
   **Answer:** false

## Slide outline & tutor notes

**3. Lambdas: functions as values**

**4. LINQ basics**

**5. LINQ on objects**  
SQL is a GCSE/A-level topic. Show the SQL equivalent: SELECT Team, SUM(Score) FROM Players GROUP BY Team.

**6. Query syntax and more operators**

**7. Deferred execution**

**8. LINQ the class**

**9. LINQ quiz**
- `new[] {1,2,3,4}.Where(n => n > 2).Sum()` → **7**
- Which LINQ method transforms each item? → **Select**
- Python's `any(x > 5 for x in nums)` in LINQ? → **nums.Any(x => x > 5)**
- What does `Take(3)` do? → **Keeps only the first 3 items**
- What's the difference between Func and Action? → **Func returns a value; Action returns void**

## 🏠 Take-home project: Creature Data Analyst
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Answer questions about a dataset of made-up creatures using nothing but LINQ.

**Milestones**
1. The starter has a CSV string of 20 creatures: name, type, hp, attack, speed, legendary (true/false)
2. Parse it into a `List<Creature>` record with `Split` and `Select`
3. Answer 8 questions, one LINQ query each: strongest attacker; average hp per type; all legendaries sorted by speed; types with more than 3 creatures; the fastest of each type; anyone whose attack > hp; total hp of the top 5 by attack; is there any creature with speed over 100?
4. Print each answer neatly with the question above it
5. Invent 2 questions of your own and answer them

**Stretch:** Write the same queries in "query syntax" (`from c in creatures where … select …`) and compare readability.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### LINQ drills  (★☆☆ warm-up)
File: `exercises/ex1_linq_drills/Program.cs`

Ten one-liners on a list of numbers and a list of words – starter has the questions.

### Student database  (★★☆ core)
File: `exercises/ex2_students/Program.cs`

Do the "LINQ the class" task fully, then add: a report card per student (name, average, letter grade via a switch expression), and the top student in each year group using GroupBy + MaxBy.

### Word frequency pipeline  (★★★ stretch)
File: `exercises/ex3_text_stats/Program.cs`

Use only LINQ (no explicit loops!) to: split a long text into words, normalise case and punctuation, remove common "stop words", count frequencies, and print the top 10 as a bar chart. Then find all words that appear exactly once and the average word length per starting letter.

## Optional extras (if he wants more)
- Rewrite 3 loops in your old C# programs as LINQ queries
- Learn the SQL equivalents of Where, Select, OrderBy and GroupBy (W3Schools SQL tutorial)
