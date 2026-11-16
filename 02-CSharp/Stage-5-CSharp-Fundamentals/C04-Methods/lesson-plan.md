# C04 · Methods

**Stage:** CSharp Fundamentals  
**Session type:** Lesson (≈60 min)  
**Slides:** `C04-Methods.pptx`

_Functions with types – return types, parameters, overloading, ref and out_

## Learning goals
- Write static methods with parameter types and return types
- Use void for methods that return nothing
- Overload methods and use optional/named parameters
- Understand ref and out parameters and expression-bodied methods

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. C# version of `for x in items:`?  
   **Answer:** foreach (var x in items)
2. What does `i++` do?  
   **Answer:** Adds 1 to i
3. Write a ternary that gives "even" or "odd" for n  
   **Answer:** n % 2 == 0 ? "even" : "odd"

## Slide outline & tutor notes

**3. Anatomy of a method**  
In a top-level-statements Program.cs, local functions can go anywhere in the file. `static` means it doesn't use any outside variables – good habit. In classes (C08) methods live inside the class.

**4. Python vs C# functions**

**5. Optional and named parameters**

**6. Overloading: same name, different parameters**

**7. out and ref**  
This is "passing by value vs by reference" – an A-level concept. Python effectively passes references to objects, but ints are immutable so it looks like by-value.

**8. Method toolkit**

**9. Methods quiz**
- What return type means "returns nothing"? → **void**
- What's overloading? → **Several methods with the same name but different parameter lists**
- What does `ref` do? → **Passes the caller's variable itself, so the method can change it**
- Why does `static int F(int x) { if (x > 0) return 1; }` not compile? → **Not all code paths return a value**
- What does `=>` mean after a method signature? → **An expression-bodied method – it returns that expression**

## 🏠 Take-home project: Dice Lab
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

A dice statistics library built from small, well-typed methods – then use it to answer questions about probability.

**Milestones**
1. `static int Roll(int sides = 6)` and `static int[] RollMany(int count, int sides = 6)`
2. `static (double mean, int min, int max) Stats(int[] rolls)` returning a tuple
3. `static void Histogram(int[] rolls, int sides)` printing a bar chart of how often each value came up
4. Answer with code: roll two dice 100,000 times – how often is the total 7? 12? Print percentages
5. Overload `Roll` so `Roll(3, 6)` means "roll 3 six-sided dice and add them" (3d6)

**Stretch:** Simulate the dice game "Pig" where a computer player always banks at 20 – what's its average number of turns to reach 100?

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Unit converter library  (★☆☆ warm-up)
File: `exercises/ex1_converters/Program.cs`

Port P11's converters as C# methods with proper types (`static double CToF(double c)` etc.) and a menu that uses a switch expression to pick the right method.

### Recursion in C#  (★★☆ core)
File: `exercises/ex2_recursion/Program.cs`

Write recursive `Factorial(int n)` returning `long`, `Fib(int n)` with a Dictionary for memoisation, and `Hanoi(int n, char from, char to, char spare)`. Compare: what's the biggest factorial that fits in a long?

### ATM with ref  (★★★ stretch)
File: `exercises/ex3_bank_methods/Program.cs`

Port the P12 ATM. Keep `balance` in top-level code and pass it by `ref` to `Deposit(ref decimal balance)` and `Withdraw(ref decimal balance)`. `CheckPin` returns bool with 3 attempts. Then rewrite Withdraw to return a tuple `(bool ok, decimal newBalance)` instead – which do you prefer?

## Optional extras (if he wants more)
- Port your P21 `ToBinary`/`ToDenary` functions to C# methods
- Find 3 overloads of `Math.Round` in VS Code's IntelliSense (type `Math.Round(` and use the arrows)
