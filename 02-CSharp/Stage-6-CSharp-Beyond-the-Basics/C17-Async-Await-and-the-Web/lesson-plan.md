# C17 · Async, Await and the Web

**Stage:** CSharp Beyond the Basics  
**Session type:** Lesson (≈60 min)  
**Slides:** `C17-Async-Await-and-the-Web.pptx`

_Doing slow things without freezing – tasks, async/await and HttpClient_

## Learning goals
- Explain why async matters (waiting without blocking)
- Write async methods that return Task and Task<T>
- Run tasks concurrently with Task.WhenAll
- Call a web API with HttpClient and parse the JSON

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does [Theory] do in xUnit?  
   **Answer:** Runs the same test with several sets of data from [InlineData]
2. What's TDD's cycle?  
   **Answer:** Red, green, refactor
3. Why keep game rules separate from the UI?  
   **Answer:** So they can be tested automatically

## Slide outline & tutor notes

**3. Why async?**  
Unity has its own version (coroutines, and now Awaitable) – same idea. Web servers use async to handle thousands of users at once.

**4. async and await**

**5. Task.WhenAll: many at once**

**6. HttpClient + JSON**  
Property names must match JSON names (case-insensitive by default for GetFromJsonAsync). Temperature_2m matches "temperature_2m". Alternatively use [JsonPropertyName].

**7. Async rules of thumb**

**8. Parallel pinger**

**9. Async quiz**
- What does `await` do? → **Pauses the method until the task finishes, without blocking the thread**
- Return type of an async method that returns an int? → **Task<int>**
- What does Task.WhenAll do? → **Waits for all the given tasks to finish (and gives all their results)**
- Is async the same as using multiple CPU cores? → **No – async is about not wasting time waiting; parallelism is about doing work on several cores**
- Which exception for a failed HTTP request? → **HttpRequestException**

## 🏠 Take-home project: Async Horse Race
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

A console horse race where every horse is its own async task – watch concurrency happen.

**Milestones**
1. `async Task<string> RunHorse(string name, int trackLength, IProgress<(string, int)> progress)` – loop: wait a random `Task.Delay(50–250ms)`, move 1 step, report progress
2. Start 5 horses at once; draw the track on every progress update (`SetCursorPosition` or just reprint)
3. Use `Task.WhenAny` to announce the winner the moment the first horse finishes
4. Then `await Task.WhenAll` for the rest and print the finishing order with times (Stopwatch)
5. Let the player bet on a horse before the race

**Stretch:** Add a CancellationToken so pressing a key stops the race early ("the race has been abandoned!").

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Breakfast simulator  (★☆☆ warm-up)
File: `exercises/ex1_kitchen/Program.cs`

Simulate making breakfast: eggs (3 s), toast (2 s), juice (1 s), coffee (4 s) using Task.Delay. First do it one after another and time it; then all at once with WhenAll and time it. Print each step as it finishes.

### Weather for 5 cities at once  (★★☆ core)
File: `exercises/ex2_weather/Program.cs`

Port P39's weather app: geocode 5 cities and fetch their weather concurrently with HttpClient and GetFromJsonAsync. Print a table sorted by temperature. Handle network failure with a friendly message.

### Async file scanner with progress  (★★★ stretch)
File: `exercises/ex3_async_file_scanner/Program.cs`

Write an async program that scans a folder (recursively) for files, reads each text file with `File.ReadAllTextAsync`, counts words, and reports progress with `IProgress<int>`. Allow cancelling with a CancellationTokenSource after 5 seconds. Print the 5 biggest files by word count.

## Optional extras (if he wants more)
- Add an async "loading..." spinner to one of your console programs while it does something slow
- Look up Unity's coroutines (`IEnumerator` + `yield return`) – notice they're like Python generators!
