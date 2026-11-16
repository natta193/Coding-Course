# C06 · Strings and Text

**Stage:** CSharp Fundamentals  
**Session type:** Lesson (≈60 min)  
**Slides:** `C06-Strings-and-Text.pptx`

_String methods, chars, StringBuilder – and why strings are immutable in C# too_

## Learning goals
- Use common string methods: Substring, IndexOf, Replace, Split, Trim, ToUpper, Contains
- Work with individual chars and char methods
- Build strings efficiently with StringBuilder
- Compare strings correctly (case, culture, ordinal)

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. How do you get the last item of an array?  
   **Answer:** arr[^1] or arr[arr.Length - 1]
2. Array vs List<T> – which can grow?  
   **Answer:** List<T>
3. How do you safely look up a dictionary key?  
   **Answer:** TryGetValue

## Slide outline & tutor notes

**3. String methods**

**4. chars**

**5. Strings are immutable**

**6. StringBuilder**  
Optional demo: time 100,000 `+=` vs StringBuilder appends. The difference is dramatic – it's O(n²) vs O(n), tying back to P28.

**7. Comparing strings**

**8. Caesar cipher in C#**

**9. Strings quiz**
- `"banana".Substring(1, 3)`? → **"ana" (start 1, length 3)**
- `"banana".IndexOf('n')`? → **2**
- Why use StringBuilder? → **Adding to a string in a loop creates a new string each time; StringBuilder edits one buffer – much faster**
- `(int)'a'`? → **97**
- Does `s.Trim();` on its own change s? → **No – strings are immutable; you need s = s.Trim();**

## 🏠 Take-home project: Word Games
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

A collection of word games and tools using strings, chars and StringBuilder.

**Milestones**
1. Anagram checker: two words are anagrams if their sorted letters match (ignore case and spaces)
2. Word scramble game: shuffle a random word's letters; the player has 3 tries to unscramble it
3. Acronym maker: "Portable Network Graphics" → "PNG"
4. Pig latin translator for a whole sentence (keep punctuation at the end of words)
5. A menu to pick each one; build any multi-part output with StringBuilder

**Stretch:** Add a "longest word you can make from these 7 letters" checker against a small word list.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Palindrome checker  (★☆☆ warm-up)
File: `exercises/ex1_palindromes/Program.cs`

Write `IsPalindrome(string s)` that ignores case, spaces and punctuation (keep only `char.IsLetterOrDigit`). Test on "Racecar", "Never odd or even", "A man, a plan, a canal: Panama" and "C#".

### Text analyser  (★★☆ core)
File: `exercises/ex2_word_stats/Program.cs`

Read a paragraph from the user. Print: word count, sentence count, average word length, the 5 most common words (ignore case and punctuation) and the text in Title Case.

### Password strength meter  (★★★ stretch)
File: `exercises/ex3_password_checker/Program.cs`

Score a password: +1 for each of length ≥ 8, length ≥ 12, a lower, an upper, a digit, a symbol; −1 if it contains a common word ("password", "1234", "qwerty"); −1 for 3+ repeated chars in a row. Show a strength bar and specific tips.

## Optional extras (if he wants more)
- Port the Morse translator and Caesar cipher into one "Spy Toolkit" menu program
- Look up "string interning" – what does C# do to save memory with identical strings?
