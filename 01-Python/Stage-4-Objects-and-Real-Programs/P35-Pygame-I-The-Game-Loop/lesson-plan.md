# P35 · Pygame I – The Game Loop

**Stage:** Objects and Real Programs  
**Session type:** Lesson (≈60 min)  
**Slides:** `P35-Pygame-I-The-Game-Loop.pptx`

_Windows, coordinates, drawing and the loop that runs every game ever made_

## Learning goals
- Install pygame and open a window
- Explain the game loop: events → update → draw
- Draw shapes and text using screen coordinates
- Control frame rate with a Clock and animate movement

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What are boundary test values for a range of 1–10?  
   **Answer:** 1 and 10 (plus 0 and 11 just outside)
2. What does assert do?  
   **Answer:** Crashes with an AssertionError if its condition is False
3. Why hash passwords?  
   **Answer:** So that if the file/database leaks, the real passwords aren't exposed

## Slide outline & tutor notes

**3. How games work**  
Install inside the course venv: activate it (you should see `(.venv)`), then `pip install pygame` – or it is already there if you ran `pip install -r requirements.txt`. On Mac with Apple Silicon, recent pygame wheels work fine; if not, try `pip install pygame-ce`.

**4. Minimal pygame program**

**5. Screen coordinates**

**6. Drawing toolbox**

**7. Animation: update positions each frame**  
Physics link: velocity, and if you add `vy += 0.5` each frame you get gravity (acceleration). Try it!

**8. Bouncy balls**

**9. Pygame quiz**
- What are the three steps of every frame? → **Handle events, update, draw**
- Where is (0, 0) on the screen? → **Top-left corner**
- What does `clock.tick(60)` do? → **Limits the loop to 60 frames per second**
- Why fill the screen every frame? → **To erase the previous frame – otherwise moving things leave trails**
- What colour is (0, 0, 255)? → **Blue**

## 🏠 Take-home project: Screensaver
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Make a mesmerising pygame screensaver. Pick at least two effects and switch between them with the number keys.

**Milestones**
1. Effect 1: a logo/rectangle bouncing around the edges, changing colour every time it hits a wall (the classic DVD screensaver – does it ever hit a corner exactly?)
2. Effect 2: fireworks – rockets fly up, burst into 40 particles with gravity that fade out
3. Effect 3 (your idea): rain, snow, a starfield, Matrix-style falling letters…
4. Use classes for the moving things (e.g. `Particle` with `update()` and `draw()`)
5. Escape quits; keys 1–3 switch effect

**Stretch:** Make it fullscreen (`pygame.FULLSCREEN`) and quit when the mouse moves, like a real screensaver.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Draw a scene  (★☆☆ warm-up)
File: `exercises/ex1_scene.py`

Draw a landscape with pygame shapes: sky, sun, ground, a house, trees. Then make clouds drift across the sky and wrap around.

### Ball class + gravity  (★★☆ core)
File: `exercises/ex2_ball_class.py`

Make a Ball class with position, velocity, radius and colour, and `update()` and `draw(screen)` methods. Spawn a new ball wherever the mouse is clicked (event type MOUSEBUTTONDOWN, `event.pos`). Add gravity and damping.

### 3D starfield  (★★★ stretch)
File: `exercises/ex3_starfield.py`

Make the classic "flying through space" starfield: each star has x, y, z. Each frame z decreases; screen position = centre + x/z, y/z scaled. Closer stars are bigger and brighter. Reset stars that pass the camera.

## Optional extras (if he wants more)
- Make something that moves in a pygame window and send me a screen recording
- Play an old arcade game (Snake, Breakout, Asteroids, Space Invaders) and write down the classes it would need
