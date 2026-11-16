# P08 · Strings in Depth

**Stage:** Foundations  
**Session type:** Lesson (≈60 min)  
**Slides:** `P08-Strings-in-Depth.pptx`

_Indexing, slicing and the string methods you'll use forever_

## Learning goals
- Index and slice strings, including negative indexes
- Use common methods: upper, lower, strip, replace, split, find, count
- Know that strings are immutable
- Use ASCII/Unicode with ord() and chr()

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does `range(1, 10, 3)` give?  
   **Answer:** 1, 4, 7
2. When should you use while instead of for?  
   **Answer:** When you don't know in advance how many times to loop
3. How do you loop over every letter in a word?  
   **Answer:** for letter in word:

## Slide outline & tutor notes

**3. Indexing: every character has a position**  
Zero-indexing is weird at first. Analogy: floors in a UK building – ground floor is 0.

**4. Slicing: grabbing a chunk**

**5. String methods**

**6. Strings are immutable**  
The `s.upper()` without assignment bug is extremely common. Show it live.

**7. Characters are numbers underneath**  
This connects to data representation in Stage 3 (P21). ASCII is 7-bit = 128 characters; Unicode covers 150,000+ including emoji.

**8. Palindrome checker**  
Bonus hint: build a cleaned string with only `ch.isalpha()` characters.

**9. What's the output?**
- `"banana"[1:4]` → **"ana"**
- `"banana".count("a")` → **3**
- `"Hello"[-3:]` → **"llo"**
- `"a,b,c".split(",")` → **['a', 'b', 'c']**
- `len("  hi  ".strip())` → **2**
- `"cat".upper()[0]` → **"C"**

## 🏠 Take-home project: Secret Agent Toolkit
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

A menu of text-scrambling tools for secret messages – all built with string methods, indexing and loops.

**Milestones**
1. Menu loop with: reverse, Caesar encrypt, Caesar decrypt, remove vowels, "pig latin", quit
2. Reverse: one line with slicing
3. Caesar: shift letters by a key, keep capitals as capitals, wrap Z back to A, leave punctuation alone
4. Pig latin: move each word's first letter to the end and add "ay" ("hello world" → "ellohay orldway")
5. Check every tool with a few test messages

**Stretch:** Add a "crack it" tool that prints the message decrypted with all 26 shifts – then spot the real one.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Initials and username  (★☆☆ warm-up)
File: `exercises/ex1_initials.py`

Ask for first name and surname. Print their initials (e.g. "A.S.") and a username made from the first 3 letters of the surname + first letter of first name + their name lengths, all lower case.

### Caesar cipher  (★★☆ core)
File: `exercises/ex2_caesar.py`

Ask for a message and a shift. Encrypt every capital and lower-case letter by shifting it along the alphabet, wrapping Z round to A. Leave other characters alone. Then decrypt with the negative shift.

### Sentence analyser  (★★★ stretch)
File: `exercises/ex3_word_stats.py`

Ask for a sentence. Print: number of words, the longest word, the number of vowels, the sentence in Title Case, and the sentence with every word reversed ("hello world" → "olleh dlrow").

## Optional extras (if he wants more)
- Write a program that checks password strength: at least 8 chars, contains a digit, an upper-case and a lower-case letter. Say what's missing
- Send me a secret message encrypted with your Caesar cipher – I'll crack it!
