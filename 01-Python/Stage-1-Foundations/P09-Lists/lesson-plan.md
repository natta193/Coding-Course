# P09 · Lists

**Stage:** Foundations  
**Session type:** Lesson (≈60 min)  
**Slides:** `P09-Lists.pptx`

_Storing many values in one variable – Python's version of an array_

## Learning goals
- Create lists, index them and change items
- Add and remove items with append, insert, pop, remove
- Loop through lists and use len, sum, min, max, sorted
- Build 2D lists (lists of lists) for grids

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What's `"PYTHON"[1:4]`?  
   **Answer:** "YTH"
2. How do you reverse a string?  
   **Answer:** s[::-1]
3. Why doesn't `name.upper()` change name?  
   **Answer:** Strings are immutable – methods return a new string, you must store it

## Slide outline & tutor notes

**3. Making and using a list**  
GCSE calls these arrays. Strictly, an array has a fixed size and one type – a Python list is more flexible. C# has both arrays and Lists (C05).

**4. Adding and removing**

**5. Looping through lists**

**6. Lists hold references – a classic trap**  
Draw two labels with arrows pointing to one box. This idea (references) is huge in C# later – classes are reference types.

**7. 2D lists: grids**

**8. Shopping list manager**

**9. Predict it**
- `x = [3, 1, 2]` then `x.append(5)`. What's `len(x)`? → **4**
- `[1, 2, 3][ → **-1]`**
- `nums = [4, 8]` then `nums[1] = 0` – nums is? → **[4, 0]**
- `a = [1]`, `b = a`, `b.append(2)`. What's a? → **[1, 2] – same list!**
- `grid = [[1, 2], [3, 4]]`. What's `grid[1][0]`? → **3**

## 🏠 Take-home project: Playlist Manager
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Build a music playlist manager using lists. (Songs are just text – no actual music!)

**Milestones**
1. Start with a list of 5 favourite songs. Menu: show, add, remove, move a song up, shuffle, play next, quit
2. Show: number the songs from 1
3. Remove by number – check the number is valid first
4. Move up: swap a song with the one above it (`a[i], a[i-1] = a[i-1], a[i]`)
5. Play next: `pop(0)` the first song, print "Now playing…" and add it to a separate "recently played" list

**Stretch:** Store each song as a small list `[title, artist, minutes]` and show the playlist's total length in minutes.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Class test stats  (★☆☆ warm-up)
File: `exercises/ex1_class_stats.py`

Ask how many students, then each one's mark. Store them in a list. Print the highest, lowest, average and how many scored above average.

### Do it without built-ins  (★★☆ core)
File: `exercises/ex2_no_builtins.py`

Write your own code to find the max, the total and whether a value is in a list – **without** using max(), sum() or `in`. This is exactly what GCSE exams ask for.

### Noughts and crosses board  (★★★ stretch)
File: `exercises/ex3_noughts_crosses.py`

Make a 3×3 grid of spaces. Players X and O take turns entering row and column (0–2). Redraw the board each turn. Don't allow taking a filled square. Stop after 9 moves (checking for a winner is a bonus).

## Optional extras (if he wants more)
- Make a "random team picker": enter names into a list, shuffle with `random.shuffle()`, split into two teams
- Find out what a **list comprehension** is (e.g. `[x * 2 for x in nums]`) and bring one example
