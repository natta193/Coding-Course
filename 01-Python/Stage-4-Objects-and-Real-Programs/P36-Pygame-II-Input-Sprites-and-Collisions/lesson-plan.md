# P36 · Pygame II – Input, Sprites and Collisions

**Stage:** Objects and Real Programs  
**Session type:** Lesson (≈60 min)  
**Slides:** `P36-Pygame-II-Input-Sprites-and-Collisions.pptx`

_Player control, images, collision detection and game states_

## Learning goals
- Move a player with the keyboard (events vs held keys)
- Use pygame.sprite.Sprite classes and sprite groups
- Detect collisions with Rect.colliderect and spritecollide
- Organise a game with states: menu, playing, game over

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What are the 3 steps of the game loop?  
   **Answer:** Events, update, draw
2. Which way does y increase on screen?  
   **Answer:** Downwards
3. How does a bounce work in code?  
   **Answer:** Flip the sign of the velocity

## Slide outline & tutor notes

**3. Two kinds of keyboard input**

**4. A Sprite class**

**5. Sprite groups**

**6. Collisions**

**7. Game states**  
Draw the state diagram: circles for states, arrows labelled with what causes the transition (press SPACE, lives = 0).

**8. Dodge!**  
This is a 30-minute build if he uses Sprite classes. It's the skeleton for the P37 project.

**9. Pygame II quiz**
- Smooth left/right movement: events or get_pressed()? → **get_pressed() – it's checked every frame while held**
- What two attributes does every Sprite need? → **image and rect**
- What does `spritecollide(player, enemies, True)` do with hit enemies? → **Removes them from the group (dokill = True)**
- What's a finite state machine? → **A system that is in one state at a time and moves between states on events**

## 🏠 Take-home project: Pong
**Time:** 2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

The original video game: two-player Pong in pygame, built with sprites and game states.

**Milestones**
1. Two paddles (W/S and Up/Down keys) and a ball that bounces off the top and bottom
2. The ball bounces off paddles; where it hits the paddle changes its angle
3. A point when the ball goes past a paddle; the ball resets to the centre heading towards the player who lost the point
4. Menu → playing → game over (first to 7) states, with SPACE to start/restart
5. Show the score in big digits at the top

**Stretch:** Add a 1-player mode where the right paddle is an AI that follows the ball (but not perfectly!).

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Coin collector  (★☆☆ warm-up)
File: `exercises/ex1_coin_collector.py`

Player moves in 4 directions with arrow keys. 10 coins appear at random places. Collect them all to win; show the score and a timer. When all are collected, show your time.

### Dodge! with sprites and states  (★★☆ core)
File: `exercises/ex2_dodge.py`

Build the Dodge game from the slide properly: Player and Block sprite classes, sprite groups, menu / playing / game over states, increasing difficulty and a saved high score.

### Breakout  (★★★ stretch)
File: `exercises/ex3_breakout.py`

Paddle, ball and a wall of bricks (a sprite group). The ball bounces off walls, paddle and bricks; bricks disappear when hit. Where the ball hits the paddle changes its angle. 3 lives; win when all bricks are gone.

## Optional extras (if he wants more)
- Find free game art on kenney.nl or opengameart.org and swap the rectangles for images with `pygame.image.load`
- Plan your P37 game: pick an idea, list the sprites, draw the state diagram
