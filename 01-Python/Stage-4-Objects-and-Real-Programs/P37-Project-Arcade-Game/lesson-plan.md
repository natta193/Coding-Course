# P37 · Project – Arcade Game

**Stage:** Objects and Real Programs  
**Session type:** Project session (≈60 min)  
**Slides:** `P37-Project-Arcade-Game.pptx`

_Design and build your own arcade game in Pygame (2–3 sessions)_

## Learning goals
- Design a game: concept, sprites, states, controls
- Build it in milestones using classes and sprite groups
- Add game feel: particles, sound, screen shake, difficulty curve
- Playtest with real people and act on feedback

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 10 min — brief + plan this project together on paper
- 30 min — build milestone 1–2 together (he drives the keyboard)
- 5 min — agree which milestones he'll do at home (the take-home)

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. Events vs get_pressed() – which for shooting one bullet per press?  
   **Answer:** Events (KEYDOWN)
2. How do you remove bullets and enemies that collide?  
   **Answer:** pygame.sprite.groupcollide(bullets, enemies, True, True)
3. What are the states of a typical game?  
   **Answer:** Menu, playing, game over (maybe paused)

## Slide outline & tutor notes

**3. Pick your game**  
Let him choose. If he picks something huge, help him cut it down to an MVP (minimum viable product) – a professional concept worth naming.

**4. Design document (10 minutes, on paper)**

**5. Milestones**

**6. Game feel tricks**

## 🏠 Take-home project: Keep Building Your Game
**Time:** 2 hours per gap (2–3 gaps) over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Your arcade game is a multi-week project – push it forward one milestone per gap.

**Milestones**
1. Gap 1: M1–M3 (movement, core mechanic, enemies + collisions + score)
2. Gap 2: M4 (states, restart, high score file)
3. Gap 3: M5 game feel (sounds, particles, shake, difficulty curve)
4. Each time: get one person to play it and write down their reaction

**Stretch:** Put it on itch.io (with a parent's OK) using pygbag to make a web version.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Space shooter – reference game  (★★★ stretch)
File: `exercises/project_space_shooter.py`

A complete reference game: ship, bullets, enemy waves, particles, lives, score, states and a saved high score – all with sprites and no image files needed. Use it for ideas or as the base for your own game.

## Optional extras (if he wants more)
- Keep building between sessions – aim for one milestone per session
- Get at least 2 people to play it; write down what they said
