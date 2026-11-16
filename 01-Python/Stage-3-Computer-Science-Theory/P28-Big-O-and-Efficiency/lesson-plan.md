# P28 · Big-O and Efficiency

**Stage:** Computer Science Theory  
**Session type:** Lesson (≈60 min)  
**Slides:** `P28-Big-O-and-Efficiency.pptx`

_Measuring how algorithms scale – the language every software engineer speaks_

## Learning goals
- Describe time complexity with Big-O notation
- Recognise O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ)
- Work out the Big-O of simple code by looking at loops
- Measure real timings and plot them

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. How does merge sort combine two sorted lists?  
   **Answer:** Repeatedly takes the smaller of the two front items
2. What's a pivot in quicksort?  
   **Answer:** The item used to split the list into smaller and bigger parts
3. Name one advantage of bubble sort over merge sort  
   **Answer:** Uses almost no extra memory / simpler to code / fast on already-sorted data

## Slide outline & tutor notes

**3. Why not just time it?**

**4. The complexity zoo**  
Table for n = 1,000,000: log n ≈ 20, n log n ≈ 20 million, n² = 10¹², 2ⁿ = more than atoms in the universe.

**5. Reading Big-O from code**

**6. Better data structure, better Big-O**  
This is THE practical lesson of Big-O. Run both on 20,000 items and watch the difference.

**7. Rules of thumb**

**8. Timing code properly**

**9. Measure it**

**10. What's the Big-O?**
- Looking up `d["key"]` in a dictionary → **O(1)**
- Printing every item in a list → **O(n)**
- Printing every pair of items in a list → **O(n²)**
- Binary search → **O(log n)**
- Two separate (not nested) loops over a list → **O(n) – O(2n) drops the constant**
- Merge sort → **O(n log n)**

## 🏠 Take-home project: Speed Lab Report
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Be a scientist: measure how three algorithms scale, graph the results and write a conclusion.

**Milestones**
1. Pick three functions with different Big-O: e.g. sum of a list (O(n)), bubble sort (O(n²)), binary search (O(log n))
2. Time each one at n = 1,000, 2,000, 4,000 and 8,000 (repeat each 3 times and take the best)
3. Print a table of n against time for each function
4. Plot all three on one graph with matplotlib (log scale on the y-axis helps!)
5. Write a conclusion in a comment: what happened each time n doubled, and does it match the Big-O?

**Stretch:** Add `x in list` vs `x in set` for the same sizes and explain the result.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Plot the growth  (★★☆ core)
File: `exercises/ex1_plot_growth.py`

Make sure matplotlib is in your venv (`pip install matplotlib` with `(.venv)` showing). Plot log n, n, n log n and n² for n from 1 to 100 on one graph. Then time linear search vs binary search for growing n and plot the real timings.

### Classify and improve  (★★☆ core)
File: `exercises/ex2_classify.py`

For each function in the starter: write its Big-O in a comment, then write a faster version where possible.

### Two-sum challenge  (★★★ stretch)
File: `exercises/ex3_two_sum.py`

Given a list of numbers and a target, find two numbers that add up to the target. Write an O(n²) brute-force version and an O(n) version using a dictionary/set. Time both on 3,000 numbers (then try 1,000,000 on the fast one). (A real Google interview question!)

## Optional extras (if he wants more)
- Look at your Hangman or Quiz Master code – find one O(n) lookup that could be O(1) with a set or dict
- Find out what "P vs NP" is in one paragraph (it's a million-dollar question – literally)
