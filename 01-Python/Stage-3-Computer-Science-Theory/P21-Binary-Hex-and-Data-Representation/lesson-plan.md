# P21 · Binary, Hex and Data Representation

**Stage:** Computer Science Theory  
**Session type:** Lesson (≈60 min)  
**Slides:** `P21-Binary-Hex-and-Data-Representation.pptx`

_How computers store numbers, text, images and sound using only 0s and 1s_

## Learning goals
- Convert between denary, binary and hexadecimal
- Add binary numbers and spot overflow
- Explain how text (ASCII/Unicode), images and sound are stored
- Calculate file sizes in bits, bytes, KB and MB

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. How do you save a dictionary to a file in one line?  
   **Answer:** json.dump(data, f)
2. What is data-driven design?  
   **Answer:** Keeping the content (data) separate from the code that uses it, so you change data not code
3. How do you split "go north" into verb and noun?  
   **Answer:** "go north".split() → ['go', 'north']

## Slide outline & tutor notes

**3. Why binary?**

**4. Place values: binary is base 2**  
Practise 5 conversions each way on paper before touching Python. Speed matters in exams. Max 8-bit value = 255.

**5. Hexadecimal: base 16**  
Conversion route: hex ↔ binary via nibbles is easiest. Hex → denary: first digit × 16 + second digit.

**6. Binary addition and overflow**

**7. Text, images and sound**  
Worked example: 1920×1080 at 24-bit = 49,766,400 bits ≈ 6.2 MB uncompressed. That's why we compress (JPEG, PNG, MP3) – lossy vs lossless is a GCSE topic worth mentioning.

**8. Units and file sizes**

**9. Convert like a computer**  
Algorithm: repeatedly n % 2 gives the next bit (from the right), n // 2 moves on. Reverse at the end, or build by prepending.

**10. Quick-fire conversions**
- 00101101 in denary → **45**
- 200 in binary → **11001000**
- 3C in denary → **60**
- 255 in hex → **FF**
- Bits needed to store 1000 different values → **10 (2¹⁰ = 1024)**
- Size of a 100×100 image, 8-bit colour, in bytes → **10,000 bytes**

## 🏠 Take-home project: Binary Blitz
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

A quiz game that drills binary and hex conversions until you can do them in your head – using your OWN conversion functions.

**Milestones**
1. Write `to_binary(n)` and `to_denary(bits)` without bin()/int(x, 2) – reuse your lesson code
2. Ask 10 random questions of mixed types: denary → binary, binary → denary, denary → hex
3. Levels: easy uses 0–15 (4 bits), hard uses 0–255 (8 bits) – the player chooses
4. Track score and the current streak; give a bonus point for 3 in a row
5. At the end, show the questions they got wrong with the right answers

**Stretch:** Add a "binary addition" question type that also asks whether the result overflows 8 bits.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Base converter  (★☆☆ warm-up)
File: `exercises/ex1_converter.py`

Write a menu program that converts between denary, binary and hex in any direction. Use your own functions for denary↔binary and Python's built-ins for hex.

### Binary adder  (★★☆ core)
File: `exercises/ex2_binary_adder.py`

Add two 8-bit binary strings column by column, right to left, with a carry – the same way a CPU's adder circuit works. Report overflow if there's a carry out of the last column. Don't convert to denary to do the sum!

### File size calculator + bitmap  (★★★ stretch)
File: `exercises/ex3_file_size.py`

(a) Write functions for image size and sound size that return a nicely formatted string in the best unit (B/KB/MB/GB). (b) Store a tiny 8×8 1-bit image as a list of binary strings and draw it with █ and spaces.

## Optional extras (if he wants more)
- Practise: convert your birthday (day, month) to binary and hex
- Design your own 8×8 sprite as binary strings and draw it with the program
