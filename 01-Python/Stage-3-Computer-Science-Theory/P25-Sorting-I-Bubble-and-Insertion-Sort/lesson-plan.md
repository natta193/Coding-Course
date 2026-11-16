# P25 · Sorting I – Bubble and Insertion Sort

**Stage:** Computer Science Theory  
**Session type:** Lesson (≈60 min)  
**Slides:** `P25-Sorting-I-Bubble-and-Insertion-Sort.pptx`

_Putting things in order, one swap at a time_

## Learning goals
- Explain and code bubble sort, including the "no swaps" early exit
- Explain and code insertion sort
- Show the state of a list after each pass (exam skill)
- Compare the two by counting comparisons and swaps

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. How does binary search decide which half to keep?  
   **Answer:** Compares the middle item with the target – smaller means go left, bigger means go right
2. Why can't binary search be used on unsorted data?  
   **Answer:** Throwing away half only works if everything in that half is definitely too big/small
3. Max comparisons for binary search on 64 items?  
   **Answer:** 6 (2⁶ = 64) – 7 in some implementations

## Slide outline & tutor notes

**3. Why learn sorting?**

**4. Bubble sort: the idea**  
Act it out with 6 playing cards. He compares and swaps; you narrate passes. Then write the state after each pass – that's the exam question format.

**5. Bubble sort**

**6. Insertion sort: the idea**

**7. Insertion sort**

**8. Bubble vs insertion**

**9. Pass by pass**

**10. Sorting quiz**
- After one pass of bubble sort on `[4, 3, 2, 1]`? → **[3, 2, 1, 4]**
- How does bubble sort know it can stop early? → **A whole pass with no swaps**
- In insertion sort, what's true about the left part of the list? → **It's always sorted**
- Which is better for a nearly sorted list? → **Insertion sort**
- How many passes max for bubble sort on 6 items? → **5**

## 🏠 Take-home project: Leaderboard Sorter
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

A game leaderboard sorted by your own sorting algorithms – no `sorted()` or `.sort()` allowed!

**Milestones**
1. Make a list of at least 12 players as tuples: (name, score, time_seconds)
2. Write `insertion_sort(items, key)` that sorts by any key function you pass in
3. Sort by score (highest first); ties broken by time (fastest first) – use a key that returns a tuple like `(-score, time)`
4. Print a neat top-10 table with positions, and mark ties
5. Add new scores typed by the user and keep the board sorted after each one (insert in the right place!)

**Stretch:** Write bubble sort too, count comparisons for both on 1,000 random players, and explain which is better here.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Sort variations  (★☆☆ warm-up)
File: `exercises/ex1_descending.py`

Modify bubble sort to sort in descending order, then to sort a list of names by length, then to sort a list of (name, score) tuples by score.

### Count the work  (★★☆ core)
File: `exercises/ex2_count_operations.py`

Add counters for comparisons and swaps/shifts to both algorithms. Test on lists of 100 and 1,000 items: random, already sorted, and reversed. Print a table. What happens to the count when the list is 10× bigger?

### Cocktail shaker sort  (★★★ stretch)
File: `exercises/ex3_cocktail_sort.py`

Bubble sort only moves small items left one step per pass ("turtles"). Cocktail shaker sort alternates: a left-to-right pass then a right-to-left pass. Implement it and compare its swaps/passes with bubble sort on `[2, 3, 4, 5, 1]`.

## Optional extras (if he wants more)
- Watch a "sorting algorithms visualised" video (search "15 sorting algorithms in 6 minutes")
- Learn the exam answer: describe bubble sort in 4 bullet points without code
