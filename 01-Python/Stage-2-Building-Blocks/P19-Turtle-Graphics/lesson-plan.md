# P19 · Turtle Graphics

**Stage:** Building Blocks  
**Session type:** Lesson (≈60 min)  
**Slides:** `P19-Turtle-Graphics.pptx`

_Drawing with code – loops and functions you can see_

## Learning goals
- Move a turtle with forward, left, right, penup, pendown
- Draw regular polygons using loops and the 360° rule
- Write drawing functions with parameters
- Make generative art and respond to key presses

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. Name two functions in the random module  
   **Answer:** e.g. randint, choice, shuffle, random, sample
2. What's a module?  
   **Answer:** A .py file of code you can import
3. How do you measure how long something takes?  
   **Answer:** Record time.time() before and after and subtract

## Slide outline & tutor notes

**3. Meet the turtle**  
turtle comes with Python – no install. If using Thonny it works out of the box. On Mac it opens a separate window, sometimes behind VS Code.

**4. Polygons and the 360° rule**  
Maths link: exterior angles of a polygon sum to 360°. He'll see this in Year 9 maths.

**5. Spirals and colour**

**6. Making it interactive**  
Event-driven programming is how every GUI and game works. We pass the function itself as a value – functions are objects too.

**7. Draw a scene**

**8. Turtle quiz**
- What angle does the turtle turn for each corner of a hexagon? → **60°**
- What's the difference between `t.color` and `turtle.bgcolor`? → **t.color sets the pen colour; bgcolor sets the background**
- Why `screen.onkey(up, "Up")` not `screen.onkey(up(), "Up")`? → **up() would call the function now and pass its result (None); we want to pass the function itself**
- How do you move without drawing? → **t.penup() then move, then t.pendown()**

## 🏠 Take-home project: Generative Art Gallery
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Make a gallery of 3 artworks that are different every time you run the program, using turtle, functions and random.

**Milestones**
1. Write a `move_to(x, y)` helper and at least 3 shape functions with parameters (size, colour…)
2. Artwork 1: a night sky – random stars of random sizes and a moon
3. Artwork 2: a spirograph – a loop of circles with a turn between each, colours cycling with `%`
4. Artwork 3: your own design (a city skyline, a forest, abstract art…)
5. A menu (`turtle.textinput`) to choose which artwork to draw; `screen.clear()` between them

**Stretch:** Press "s" to save the drawing: `turtle.getcanvas().postscript(file="art.eps")`.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Shape library  (★☆☆ warm-up)
File: `exercises/ex1_shapes.py`

Write `polygon`, `star(points, size)` and `flower(petals)` functions (a flower = a circle drawn repeatedly with a turn between). Draw a garden.

### Etch-a-Sketch  (★★☆ core)
File: `exercises/ex2_etch_sketch.py`

Arrow keys move the turtle, space lifts/lowers the pen, c clears, and number keys 1–5 change colour.

### Recursive fractal tree  (★★★ stretch)
File: `exercises/ex3_fractal_tree.py`

A tree is a trunk with two smaller trees on top. Write `tree(length)` that draws a branch, then calls itself twice (turned left and right) with a shorter length, stopping when length < 5. This is a sneak peek of recursion (P26)!

## Optional extras (if he wants more)
- Make a piece of generative art you're proud of and screenshot it
- Try changing the angles and shrink factor in the fractal tree – what's the weirdest tree you can make?
