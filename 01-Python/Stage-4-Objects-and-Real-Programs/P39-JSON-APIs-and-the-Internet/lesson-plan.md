# P39 · JSON, APIs and the Internet

**Stage:** Objects and Real Programs  
**Session type:** Lesson (≈60 min)  
**Slides:** `P39-JSON-APIs-and-the-Internet.pptx`

_Getting live data from the web into your programs_

## Learning goals
- Read and write JSON with the json module
- Explain clients, servers, HTTP requests and status codes
- Call a real web API with the requests library
- Process nested JSON responses and handle network errors

## Suggested timing
- 15 min — **review last take-home**: he demos it, you code-review it (see checklist below), then the recap quiz
- 35 min — teach through the slides; stop at every *Your turn*; do one in-session exercise (★ or ★★)
- 10 min — kick off the take-home project: read the brief together, get milestone 1 started so he isn't stuck at home

**Take-home review checklist:** Does it run? Can he explain every line? One thing done well (say it!) · one improvement (names, functions, edge cases) · did he try a stretch? Log it in the Progress Tracker.

## Recap quiz (start of session)
1. What does BFS use: a stack or a queue?  
   **Answer:** A queue
2. Which BST traversal gives sorted output?  
   **Answer:** In-order
3. How would you store a graph in Python?  
   **Answer:** An adjacency list – a dictionary mapping each node to a list of neighbours

## Slide outline & tutor notes

**3. JSON: the language of data on the web**

**4. json module**

**5. How the web works (the short version)**  
GCSE networks topic: protocols (HTTP/HTTPS, TCP/IP), client-server model. HTTPS = HTTP + encryption (TLS).

**6. Calling an API**

**7. Handling the real world**

**8. Explore an API**  
PokéAPI is free, no key. Answer path: data["types"][i]["type"]["name"], data["stats"][i]["base_stat"] and ["stat"]["name"].

**9. Web quiz**
- What does status code 404 mean? → **Not found**
- Which HTTP method reads data? → **GET**
- `json.loads` vs `json.load`? → **loads parses a string; load reads from a file**
- What Python type does a JSON array become? → **list**
- Why use a timeout? → **So the program doesn't hang forever if the server doesn't respond**

## 🏠 Take-home project: Personal Dashboard
**Time:** 1–2 hours over the gap between sessions · **Brief for him:** at the top of the take-home starter file

Your own morning dashboard in the terminal, built from free web APIs – plus caching so it works offline.

**Milestones**
1. Weather for your town from Open-Meteo (geocode the name first, like the lesson)
2. A random joke from `https://official-joke-api.appspot.com/random_joke`
3. A "number fact" or anything else free you find (search "public APIs list")
4. Save each response to `cache.json` with a timestamp; if the internet is down, show the cached version and say how old it is
5. Every API call has a timeout and error handling – the dashboard must never crash

**Stretch:** Add colours with the `colorama` package (`pip install colorama` with your venv active – then add it to requirements.txt).

Reference solution: `take-home/solution/` – for you, not him. His version will (and should) look different.

## In-session practice
Do one ★ or ★★ exercise in the session; the rest are optional extras. Starter files are in `exercises/`, worked solutions in `solutions/`.

### Weather app  (★★☆ core)
File: `exercises/ex1_weather_cli.py`

Ask for a city, look up its coordinates with Open-Meteo's geocoding API (`https://geocoding-api.open-meteo.com/v1/search?name=London`), then show current weather and a 3-day max/min forecast.

### Pokédex  (★★☆ core)
File: `exercises/ex2_pokedex.py`

Make a mini Pokédex: look up any Pokémon by name or number, print its info and a bar chart of its base stats, and cache results in pokedex_cache.json so repeat lookups don't hit the internet.

### Live trivia game  (★★★ stretch)
File: `exercises/ex3_trivia.py`

Use the Open Trivia DB (`https://opentdb.com/api.php?amount=10&type=multiple`) to build a quiz with fresh questions every game. The text comes HTML-encoded – fix it with `html.unescape`. Shuffle the answers, score the player, and reuse your leaderboard from Quiz Master.

## Optional extras (if he wants more)
- Find a free API about something you like (football, space, games – search "public-apis" on GitHub) and print something interesting from it
- Think about what you want to build for your capstone project
