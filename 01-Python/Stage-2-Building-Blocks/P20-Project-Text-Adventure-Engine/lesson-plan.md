# P20 · Project – Text Adventure Engine

**Stage:** Building Blocks  
**Session type:** Project session (≈60 min)  
**Slides:** `P20-Project-Text-Adventure-Engine.pptx`

_A data-driven adventure game – rooms, items and puzzles stored in dictionaries_

## Learning goals
- Model a game world with nested dictionaries
- Separate data (the world) from logic (the engine)
- Parse simple commands like "go north" and "take key"
- Save and load game state to a file

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 10 min — brief + plan this project together on paper
- 30 min — build milestone 1–2 together (he drives the keyboard)
- 5 min — agree which milestones he'll do at home (the take-home)

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does `t.left(360 / 6)` draw towards?  
   **Answer:** A hexagon – each turn is 60°
2. What is event-driven programming?  
   **Answer:** Code that runs in response to events like key presses or clicks
3. What's the difference between `func` and `func()`?  
   **Answer:** func is the function itself; func() calls it

## Slide outline & tutor notes

**3. The brief**  
Let him invent the setting – haunted school, space station, Minecraft-ish cave. Ownership = motivation.

**4. The world is just data**

**5. Parsing commands**

**6. Milestones**  
json is formally taught in P39 – here just show json.dump / json.load as a magic save button.

## 🏠 Take-home project: Write Your World
**Time:** 2 hours (over 2 gaps if needed) over the gap between sessions · **Brief for him:** at the top of the take-home starter file

The engine works – now write the game! Make an adventure world you'd want to play.

**Milestones**
1. Plan a map on paper: at least 6 rooms with exits and a theme
2. Write the ROOMS data: descriptions, items, at least one locked room that `needs` an item
3. Add a twist: a hidden room, a riddle, or a trap that ends the game
4. Do the Stage 2 checkpoint without notes

**Stretch:** Add NPCs: a `"person"` key in a room with lines they say when you type "talk".

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Text adventure – full game  (★★☆ core)
File: `exercises/project_adventure.py`

Build the engine through M1–M4, then write your own world for M5. The solution is a small but complete engine with the 3-room demo world.

### Stage 2 checkpoint  (★★☆ core)
File: `exercises/stage2_checkpoint.py`

Eight questions covering functions, errors, dictionaries, sets, files and modules. No notes!

## Optional extras (if he wants more)
- Write your world – at least 6 rooms and one puzzle – and get someone to play it
- Draw a map of your world on paper with the exits labelled
