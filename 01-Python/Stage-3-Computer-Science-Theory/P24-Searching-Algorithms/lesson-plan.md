# P24 · Searching Algorithms

**Stage:** Computer Science Theory  
**Session type:** Lesson (≈60 min)  
**Slides:** `P24-Searching-Algorithms.pptx`

_Linear search vs binary search – and why sorted data is so powerful_

## Learning goals
- Code linear search and explain how it works
- Code binary search (iterative) and explain how it works
- Compare their efficiency by counting comparisons
- Know when each one can be used

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. Name the four parts of computational thinking  
   **Answer:** Decomposition, abstraction, pattern recognition, algorithmic thinking
2. What does a diamond mean in a flowchart?  
   **Answer:** A decision (yes/no)
3. What's a trace table for?  
   **Answer:** Dry-running an algorithm by tracking variables line by line

## Slide outline & tutor notes

**3. The search problem**

**4. Linear search**

**5. Binary search: the idea**  
Act it out with a physical deck of sorted numbered cards or a dictionary (the paper kind). Ask: why can't this work on an unsorted list?

**6. Binary search**  
Trace it for target 23: (0,9)->mid 4 (16<23)->low 5; (5,9)->mid 7 (56>23)->high 6; (5,6)->mid 5 -> found.

**7. Linear vs binary**

**8. Python's built-in search tools**

**9. Trace binary search**

**10. Search quiz**
- What must be true of a list for binary search? → **It must be sorted**
- Max comparisons for linear search on 50 items? → **50**
- Max comparisons for binary search on 1000 items? → **10 (2¹⁰ = 1024)**
- In `[3, 6, 9, 12, 15]`, which item does binary search check first? → **9 (index 2)**
- If a list keeps changing and is rarely searched, which is better? → **Linear – sorting it every time costs more than searching**

## 🏠 Take-home project: Search Showdown
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Prove with real data how much faster binary search is – then use it in a game.

**Milestones**
1. Generate a sorted list of 1,000,000 fake usernames (e.g. "user0000001" … with `f"user{i:07d}"`)
2. Write linear and binary search that also count comparisons
3. Search for 20 random usernames with both; print a table: name, linear comparisons, binary comparisons
4. Time both with `time.perf_counter()` and print the total time for each
5. Game: the computer thinks of a word from a sorted word list; you guess words and it says "earlier"/"later" in the alphabet – how many guesses do YOU need?

**Stretch:** Plot comparisons against list size (1,000 → 1,000,000) for both algorithms with matplotlib.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Race them  (★★☆ core)
File: `exercises/ex1_count_comparisons.py`

Modify both searches to also return how many comparisons they made. Make a sorted list of 1,000,000 numbers, search for 200 random targets with each, and print the average comparisons.

### Search variants  (★★☆ core)
File: `exercises/ex2_search_variants.py`

Write: `find_all(items, target)` returning every index where target appears; `first_greater(items, x)` returning the first item bigger than x in a sorted list (use binary search!); and a linear search over a list of dictionaries by a chosen key.

### Dictionary lookup  (★★★ stretch)
File: `exercises/ex3_word_finder.py`

Build a sorted list of 5,000+ English words (download a word list, or generate fake ones with random letters). Write a spell-checker that uses binary search to check each word of a sentence and marks misspelt ones with *asterisks*.

## Optional extras (if he wants more)
- Explain binary search to someone at home using a phone book or dictionary
- Write a recursive version of binary search (we'll check it in P26)
