# C18 · Unity I – GameObjects and Scripts

**Stage:** CSharp Beyond the Basics  
**Session type:** Lesson (≈60 min)  
**Slides:** `C18-Unity-I-GameObjects-and-Scripts.pptx`

_Your C# in a real game engine – the editor, components and your first MonoBehaviour_

## Learning goals
- Install Unity 6 via Unity Hub and create a 2D project
- Explain GameObjects, Components, Transforms and the Inspector
- Write a MonoBehaviour with Start and Update
- Move objects smoothly with Time.deltaTime and keyboard input

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does `await` do?  
   **Answer:** Pauses the method until a task finishes without blocking the thread
2. What does Task.WhenAll do?  
   **Answer:** Waits for several tasks to finish together
3. Struct or class: Unity's Vector3?  
   **Answer:** Struct – a value type (C12)

## Slide outline & tutor notes

**3. Getting set up**  
In Unity: Edit → Preferences → External Tools → External Script Editor → VS Code. Install the "Unity" extension in VS Code for IntelliSense.

**4. The Unity editor tour**

**5. GameObjects and Components**

**6. Your first script**  
The class name must match the file name exactly (Spinner.cs → class Spinner) or Unity can't attach it. Drag the script onto a sprite in the Hierarchy.

**7. Time.deltaTime**

**8. Moving with the keyboard**  
Older tutorials use Input.GetAxis("Horizontal"). That needs Project Settings → Player → Active Input Handling set to "Both". Either works – just be consistent.

**9. Hello Unity**

**10. Unity quiz**
- What does every GameObject have? → **A Transform (position, rotation, scale)**
- When does Update run? → **Once every frame**
- Why multiply by Time.deltaTime? → **So movement is per second, not per frame – same speed at any frame rate**
- How do you make a script value editable in the Inspector? → **Make it a public field (or [SerializeField] private)**
- What class do Unity scripts inherit from? → **MonoBehaviour**

## 🏠 Take-home project: Asteroid Drift
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Your first Unity mini-game: fly a ship through a drifting asteroid field. No physics yet – just Transform movement and your own scripts.

**Milestones**
1. A ship sprite with a `ShipControls` script: A/D rotate, W thrusts forward (`transform.up`), with velocity that slowly drifts
2. Wrap the ship around the screen edges (leave the right → appear on the left)
3. An `AsteroidSpawner` that creates 8 asteroids from a prefab at random positions, each with a random speed, direction and spin
4. Asteroids wrap around the screen too – put the wrapping code in its own `ScreenWrap` component and reuse it
5. Camera follows nothing – the whole field fits on screen

**Stretch:** Count how many seconds you survive without touching an asteroid (check distances in Update for now – physics comes next lesson).

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Smooth camera follow  (★☆☆ warm-up)
File: `exercises/ex1_camera_follow.cs`

Write a CameraFollow script with a public `Transform target` and a `smoothing` value. In LateUpdate, move the camera towards the target using `Vector3.Lerp`, keeping the camera's z at -10.

### Screen-bouncing sprite  (★★☆ core)
File: `exercises/ex2_bouncer.cs`

Write a Bouncer script: the sprite moves with a public Vector2 velocity and bounces off the edges of the camera view. Get the edges from `Camera.main.orthographicSize` and `Camera.main.aspect`. Change colour on each bounce with `GetComponent<SpriteRenderer>().color = Random.ColorHSV()`.

### Solar system  (★★★ stretch)
File: `exercises/ex3_orbit.cs`

Make an Orbit script: a public Transform `centre`, a radius and a period in seconds. Each frame, place the object on a circle around the centre using `Mathf.Cos`/`Mathf.Sin` and `Time.time`. Build a sun, 3 planets and a moon orbiting a planet (the moon's centre is a moving planet!).

## Optional extras (if he wants more)
- Do Unity's free "Essentials" pathway on learn.unity.com (first missions)
- Find a free sprite pack on kenney.nl and import it into your project (drag the PNGs into the Project window)
