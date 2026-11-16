# C20 · Project – Unity Game and Graduation

**Stage:** CSharp Beyond the Basics  
**Session type:** Project session (≈60 min)  
**Slides:** `C20-Project-Unity-Game-and-Graduation.pptx`

_Design, build, polish and ship a complete 2D game – then show it off (4–6 sessions)_

## Learning goals
- Plan a game with a design document and milestones
- Build it with clean, component-based C# scripts
- Polish: audio, particles, menus, juice
- Build it as an app and present it – course complete!

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 10 min — brief + plan this project together on paper
- 30 min — build milestone 1–2 together (he drives the keyboard)
- 5 min — agree which milestones he'll do at home (the take-home)

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. Trigger vs collision?  
   **Answer:** Triggers detect overlap without a physical bounce; collisions are solid
2. What does Instantiate do?  
   **Answer:** Creates a copy of a prefab/GameObject in the scene
3. How do you reload the current scene?  
   **Answer:** SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex)

## Slide outline & tutor notes

**3. Game ideas (pick one, keep it small)**

**4. Script architecture**  
Encourage the C09 interface idea: bullets call GetComponent<IDamageable>() so barrels, enemies and the boss all just work.

**5. Events: decoupled scripts**

**6. Milestones**

**7. Graduation presentation**  
Make a big deal of this. Consider exporting a WebGL build and putting it on itch.io (free) so family and friends can play it – with parental OK.

## 🏠 Take-home project: Ship Your Game
**Time:** 2 hours per gap (4–6 gaps) over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Your graduation game. One milestone per gap; every session starts with a playtest of the latest build.

**Milestones**
1. Gap 1: grey-box prototype (M1)
2. Gap 2: core mechanic + win/lose (M2)
3. Gap 3: UI, menus, restart (M3)
4. Gap 4: content – levels or waves (M4)
5. Gap 5: polish – art, sound, particles (M5)
6. Gap 6: build it, playtest with 3 people, fix, rehearse your graduation demo

**Stretch:** Publish a WebGL build on itch.io (with a parent's OK) and send the link to family.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Unity game starter scripts  (★★★ stretch)
File: `exercises/project_unity_starter.cs`

A set of reusable, well-structured scripts to start any 2D Unity game from: physics player movement with coyote time and jump buffering, a Health component with events, a GameManager singleton with states, and a UI hearts display. Each class goes in its own file named after the class.

## Optional extras (if he wants more)
- One milestone per session; commit to Git after each one (Unity needs a Unity .gitignore – GitHub offers one)
- Final session: graduation presentation 🎓 – and decide what's next (A-level CS? A web stack? More Unity?)
