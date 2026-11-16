# C05 · Arrays, Lists and Dictionaries

**Stage:** CSharp Fundamentals  
**Session type:** Lesson (≈60 min)  
**Slides:** `C05-Arrays-Lists-and-Dictionaries.pptx`

_C#'s collections – fixed arrays, growable List<T> and Dictionary<TKey, TValue>_

## Learning goals
- Create and use fixed-size arrays and 2D arrays
- Use List<T>: Add, Remove, Insert, Contains, Count, Sort
- Use Dictionary<TKey, TValue>: add, lookup, TryGetValue, loop
- Choose between array, List and Dictionary

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does `void` mean on a method?  
   **Answer:** It returns nothing
2. What's overloading?  
   **Answer:** Several methods with the same name but different parameters
3. How do you return two values from a method?  
   **Answer:** A tuple, e.g. (int q, int r), or out parameters

## Slide outline & tutor notes

**3. Arrays: fixed size, one type**

**4. 2D arrays: grids**

**5. List<T>: Python's list, with a type**

**6. Dictionary<TKey, TValue>**

**7. Which collection?**

**8. Port Stage 1 programs**

**9. Collections quiz**
- How do you get the number of items in an array? A List? → **array.Length; list.Count**
- How do you add to a List? → **list.Add(item)**
- What's C#'s safe version of `dict.get(key)`? → **TryGetValue (or GetValueOrDefault)**
- What does `names[^1]` give? → **The last item**
- Can you put an int in a List<string>? → **No – compile error, the list only holds strings**

## 🏠 Take-home project: Battleships
**Time:** 2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Single-player Battleships against a hidden computer fleet, using 2D arrays and collections.

**Milestones**
1. An 8×8 `char[,]` board for the hidden ships and another for what the player has seen
2. Place 3 ships (lengths 4, 3, 2) randomly, horizontally or vertically, without overlapping or going off the board
3. The player has 25 shots: type a coordinate like `C5` – parse the letter and number, re-ask on bad input or repeated shots
4. Show `X` for hits, `o` for misses; announce "Sunk!" when a whole ship is hit (track each ship's cells in a `List<(int, int)>`)
5. Win when every ship is sunk; lose when out of shots and reveal the fleet

**Stretch:** Make it two-player against a computer that shoots back, hunting around its hits.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Gradebook  (★☆☆ warm-up)
File: `exercises/ex1_gradebook/Program.cs`

Use a `Dictionary<string, List<int>>` mapping student names to their test scores. Add 4 students with 3 scores each, then print each student's average and the top student.

### Noughts and crosses  (★★☆ core)
File: `exercises/ex2_noughts_crosses/Program.cs`

Port P09's noughts and crosses using `char[,]`. Validate moves with TryParse, detect wins (rows, columns, diagonals) with a `CheckWin(char[,] b, char p)` method, and detect draws.

### Hangman in C#  (★★★ stretch)
File: `exercises/ex3_hangman/Program.cs`

Port your P10 Hangman: a `string[]` word list, `List<char>` of guesses, `HashSet<char>` for fast lookup of the secret's letters, and methods `MaskWord`, `HasWon`, `ReadGuess`.

## Optional extras (if he wants more)
- Port the Morse code translator (P14) using a Dictionary<char, string>
- Find out what `List<T>.BinarySearch` does – and what it needs first
