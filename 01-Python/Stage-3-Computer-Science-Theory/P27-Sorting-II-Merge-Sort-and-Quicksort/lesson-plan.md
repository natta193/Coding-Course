# P27 · Sorting II – Merge Sort and Quicksort

**Stage:** Computer Science Theory  
**Session type:** Lesson (≈60 min)  
**Slides:** `P27-Sorting-II-Merge-Sort-and-Quicksort.pptx`

_Divide and conquer – how real-world sorting gets fast_

## Learning goals
- Explain the divide-and-conquer strategy
- Explain and code merge sort (recursive)
- Explain and code quicksort
- Compare all four sorts on speed and memory

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What is a base case?  
   **Answer:** The simple case a recursive function answers directly, which stops the recursion
2. What's in a stack frame?  
   **Answer:** A call's local variables and where to return to
3. Why is naive recursive fibonacci slow?  
   **Answer:** It recalculates the same values over and over (exponentially many calls)

## Slide outline & tutor notes

**3. Divide and conquer**

**4. Merge sort: the idea**  
Draw the classic tree diagram: splitting down, merging up. GCSE asks students to show the stages of merge sort.

**5. Merge sort**

**6. Quicksort: the idea**

**7. Quicksort (simple version)**

**8. The four sorts**  
GCSE: know bubble, insertion, merge. A-level adds quicksort. Exams ask for one advantage and one disadvantage of each.

**9. Draw it**

**10. Sorting quiz 2**
- What's the base case of merge sort? → **A list of 0 or 1 items – already sorted**
- After partitioning, where is the pivot? → **In its final sorted position**
- Which sort always takes about n log n? → **Merge sort**
- One disadvantage of merge sort? → **Needs extra memory for the merged lists**
- 1,000,000 items: roughly how many steps for n log n? → **About 20 million (vs a trillion for n²)**

## 🏠 Take-home project: Big Sort
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Sort a really big file with your own merge sort and compare it with Python's built-in sort.

**Milestones**
1. Write a program that creates `words.txt` with 200,000 random "words" (random letters, 3–8 long), one per line
2. Read it back into a list and sort it with YOUR merge sort; check the result equals `sorted()`
3. Time your merge sort, your quicksort and `sorted()` on it and print a results table
4. Find the 10 most common words (sorting makes duplicates sit next to each other – use that, no dictionary!)
5. Write the sorted words to `sorted_words.txt`

**Stretch:** Find out what algorithm Python's `sorted()` uses (Timsort) and why it's faster than yours, in 3 sentences in a comment.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Sort race  (★★☆ core)
File: `exercises/ex1_sort_race.py`

Time bubble, insertion, merge, quicksort and Python's sorted() on random lists of 1,000 and 3,000 items, then try 100,000 with just the fast ones. Print a results table.

### Merge practice  (★★☆ core)
File: `exercises/ex2_merge_lists.py`

Write `merge(a, b)` for two sorted lists without using sort. Then use it to merge 5 sorted lists of exam results into one ranking. Finally, write `merge_sort` that sorts dictionaries by a chosen key.

### In-place quicksort  (★★★ stretch)
File: `exercises/ex3_inplace_quicksort.py`

Write quicksort that sorts the list in place using the Lomuto partition scheme (pivot = last item; walk through, swapping smaller items to the front). Then try it on an already-sorted list of 900 items – what happens and why? Fix it with a random pivot.

## Optional extras (if he wants more)
- Explain merge sort to someone at home with a pack of cards
- Make a revision sheet: for each of the 4 sorts – how it works (2 lines), best use, one pro, one con
