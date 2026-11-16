# C12 · Value Types, References, Enums and Null

**Stage:** CSharp Beyond the Basics  
**Session type:** Lesson (≈60 min)  
**Slides:** `C12-Value-Types-References-Enums-and-Null.pptx`

_What really happens in memory – and how C# protects you from null_

## Learning goals
- Explain value types vs reference types (stack vs heap)
- Use structs and records appropriately
- Use enums for fixed sets of options
- Handle null safely with ?, ?., ?? and ??=

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What's an interface?  
   **Answer:** A contract listing members a class must implement
2. How do you throw your own exception?  
   **Answer:** throw new SomeException("message");
3. What does `finally` do?  
   **Answer:** Runs whether or not an exception happened

## Slide outline & tutor notes

**3. Value types vs reference types**  
Remember P09's "lists hold references" trap? This is the same thing, now with names. Draw stack boxes with arrows into a heap cloud.

**4. Structs: small value types**

**5. Records: data classes in one line**

**6. Enums: named options**

**7. Null safety**  
Tony Hoare, who invented null references, called it his "billion-dollar mistake". C#'s nullable reference types are the fix.

**8. Traffic lights**

**9. Memory quiz**
- Is `string` a value or reference type? → **Reference (but immutable, so it feels like a value)**
- After `var b = a;` with a struct, does changing b change a? → **No – structs are copied**
- What does `a?.Name ?? "?"` give if a is null? → **"?"**
- What's free with a `record`? → **Constructor, properties, ToString, value equality, with-expressions**
- What's the garbage collector for? → **Freeing heap memory from objects nothing references any more**

## 🏠 Take-home project: The Card Game War
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Play the classic card game War, modelled with enums, records and value types.

**Milestones**
1. `enum Suit { Clubs, Diamonds, Hearts, Spades }` and `enum Rank { Two = 2, …, Ace = 14 }`
2. `record Card(Rank Rank, Suit Suit)` with a nice ToString (e.g. "Q♥")
3. Build and shuffle a 52-card deck with `Enum.GetValues`; deal into two `Queue<Card>` hands
4. Each round both players flip their top card; the higher rank takes both (put them at the back of their queue)
5. A tie means "war": each puts 3 cards face down and flips another – the winner takes the whole pile. Stop after 1,000 rounds or when someone has no cards

**Stretch:** Run 1,000 games silently and report the average number of rounds a game takes.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Reference lab  (★☆☆ warm-up)
File: `exercises/ex1_reference_lab/Program.cs`

Predict, then run: copy an int, a struct, a class object, an array and a record, change the copy, and print the original each time. Write a comment explaining each result.

### Traffic light simulator  (★★☆ core)
File: `exercises/ex2_traffic_lights/Program.cs`

Build the traffic-light task fully: enum, Next(), a Junction record, and a timed loop (`Thread.Sleep`) that runs two junctions out of phase so they're never both green.

### Vector2 struct  (★★★ stretch)
File: `exercises/ex3_vector/Program.cs`

Write a `readonly struct Vector2` with X and Y, Length, Normalized(), and operator overloads for +, -, * (by a number) and ==. Use it to simulate a ball moving with velocity and gravity for 10 steps (just like Unity!).

## Optional extras (if he wants more)
- Replace "magic strings" in your dungeon crawler with enums (directions, enemy types)
- Turn a data class in one of your projects into a record
