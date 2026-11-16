# P11 · Functions

**Stage:** Building Blocks  
**Session type:** Lesson (≈60 min)  
**Slides:** `P11-Functions.pptx`

_Write code once, use it everywhere – parameters and return values_

## Learning goals
- Define functions with def and call them
- Pass information in with parameters / arguments
- Send results back with return
- Know the difference between a procedure and a function

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. How do you get the last item of a list?  
   **Answer:** my_list[-1]
2. What does `pop()` do?  
   **Answer:** Removes the last item and returns it
3. How do you access row 2, column 0 of a grid?  
   **Answer:** grid[2][0]

## Slide outline & tutor notes

**3. Why functions?**

**4. Defining and calling**

**5. Parameters: passing data in**

**6. return: getting data back**  
Key misconception: print vs return. A function that prints the area can't be used in a calculation. Make him write both and try `area(2,3) + 1` with the print version.

**7. Procedures vs functions (GCSE terms)**  
In Python both use def. In exams, "subroutine" covers both. C# makes the distinction visible with `void`.

**8. Function factory**

**9. Predict it**
- `def f(x): return x * 2` then `print(f(f(3)))` → **12**
- `def g(): print("hi")` then `y = g()` – what is y? → **None (and "hi" is printed)**
- `def h(a, b): return a - b` then `h(b=1, a=5)` → **4**
- What's printed: `def k(): return 1` / `print("x")` inside k after return? → **Nothing – code after return never runs**

## 🏠 Take-home project: Casino Night: Blackjack
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Build a simple Blackjack (21) game against the computer dealer, with every part of the game as its own function.

**Milestones**
1. Write `draw_card()` that returns a random card value (2–10, picture cards = 10, ace = 11)
2. Write `hand_total(hand)` that adds up a list of cards – and counts an ace as 1 if the total would go over 21
3. Write `player_turn()` – keep asking hit or stand; return the hand (bust if over 21)
4. Write `dealer_turn()` – the dealer must hit until reaching 17 or more
5. Write `winner(player, dealer)` that returns a message, and a `main()` that plays rounds until the player quits

**Stretch:** Give the player 100 chips and let them bet each round; game over at 0 chips.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Unit converter library  (★☆☆ warm-up)
File: `exercises/ex1_converters.py`

Write functions `c_to_f(c)`, `f_to_c(f)`, `km_to_miles(km)`, `kg_to_stone(kg)`. Then a menu that lets the user pick a conversion and uses your functions.

### is_prime and friends  (★★☆ core)
File: `exercises/ex2_is_prime.py`

Write `is_prime(n)` returning True/False. Use it to write `primes_up_to(n)` that returns a list, and `next_prime(n)` that returns the first prime bigger than n.

### Dice simulator  (★★★ stretch)
File: `exercises/ex3_dice_stats.py`

Write `roll(sides)` returning a random roll, and `roll_many(n, sides)` returning a list of n rolls. Roll two dice 10,000 times, count how often each total (2–12) appears, and print a text bar chart. Which total is most common and why?

## Optional extras (if he wants more)
- Go back to your Hangman game and split it into functions: `choose_word()`, `show_board()`, `get_guess()`, `has_won()`
- Write a function `password_strength(pw)` that returns "weak", "medium" or "strong"
