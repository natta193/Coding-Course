# C19 · Unity II – Physics, Prefabs and UI

**Stage:** CSharp Beyond the Basics  
**Session type:** Lesson (≈60 min)  
**Slides:** `C19-Unity-II-Physics-Prefabs-and-UI.pptx`

_Rigidbodies, collisions, spawning with prefabs, and a score on screen_

## Learning goals
- Use Rigidbody2D and Collider2D for physics movement and jumping
- Respond to collisions and triggers with OnCollisionEnter2D / OnTriggerEnter2D
- Create prefabs and spawn them with Instantiate; remove with Destroy
- Show score and game-over UI with TextMeshPro and reload scenes

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What runs every frame in a MonoBehaviour?  
   **Answer:** Update()
2. What's Time.deltaTime?  
   **Answer:** Seconds since the last frame – used to make movement per second
3. What's a Component?  
   **Answer:** A piece of behaviour or data attached to a GameObject (Transform, SpriteRenderer, scripts…)

## Slide outline & tutor notes

**3. Physics components**

**4. Physics movement and jumping**

**5. Collision messages**  
Misspelling (OnCollisionEnter without 2D in a 2D game, or wrong capitalisation) is the #1 "why isn't it working" in Unity. No error – it just never gets called.

**6. Prefabs and spawning**

**7. Score UI with a singleton**  
The static Instance is the "singleton" pattern. Simple and fine for small games.

**8. Coin catcher**

**9. Unity physics quiz**
- What two components does an object need to collide? → **A Collider2D (both objects) and a Rigidbody2D (at least one)**
- Trigger or collision for collecting a coin? → **Trigger – you pass through it**
- What's a prefab? → **A saved GameObject template you can spawn copies of**
- What does `Destroy(obj, 10f)` do? → **Destroys obj after 10 seconds**
- Why isn't my OnCollisionEnter2D being called? → **Misspelt name, missing Rigidbody2D, or a collider is a trigger – check all three**

## 🏠 Take-home project: Mini Platformer Level
**Time:** 2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Build one complete platformer level using physics, triggers, prefabs and UI.

**Milestones**
1. Use the PlatformerPlayer script from the lesson; build a level from Ground-tagged platforms (with gaps!)
2. Coins (trigger + Coin script) scattered around; the score shows in a TextMeshPro label
3. Spikes (trigger, tag "Hazard") and a fall zone below the level that send you back to the last checkpoint
4. A `Checkpoint` trigger that stores the player's respawn position
5. A goal flag that shows "Level complete! X coins in Y seconds" and freezes time

**Stretch:** Add a moving platform (Kinematic Rigidbody2D moved with MovePosition between two points) that carries the player.

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Coin and player scripts  (★☆☆ warm-up)
File: `exercises/ex1_coin.cs`

Write the Coin catcher scripts from the "Your turn" slide: `CatcherPlayer` (keyboard movement clamped to the screen, OnTriggerEnter2D for coins and bombs) and `Coin` (a public value, spins while falling).

### Patrolling enemy  (★★☆ core)
File: `exercises/ex2_enemy_patrol.cs`

An enemy walks back and forth between two points (public Transforms), flipping its sprite to face the way it's walking. If the player lands on top of it (contact normal pointing down), the enemy dies; otherwise the player is hurt.

### Top-down shooter  (★★★ stretch)
File: `exercises/ex3_shooter.cs`

Player rotates to face the mouse (`Mouse.current.position`, `Camera.main.ScreenToWorldPoint`, `Mathf.Atan2`) and fires bullet prefabs on click. Bullets move forward and destroy enemies on trigger. Enemies chase the player with `Vector2.MoveTowards`.

## Optional extras (if he wants more)
- Finish the coin catcher with a start screen and a high score saved with `PlayerPrefs.SetInt`
- Plan your final project for C20: one-page design doc (pitch, controls, objects, win/lose)
