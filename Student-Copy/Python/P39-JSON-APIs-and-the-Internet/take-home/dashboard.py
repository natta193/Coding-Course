# TAKE-HOME PROJECT: Personal Dashboard
# After lesson P39 (JSON, APIs and the Internet) - about 1–2 hours, in chunks over the next few days.
#
# Your own morning dashboard in the terminal, built from free web APIs – plus caching so
# it works offline.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Weather for your town from Open-Meteo (geocode the name first, like the lesson)
#   [ ] 2. A random joke from https://official-joke-api.appspot.com/random_joke
#   [ ] 3. A "number fact" or anything else free you find (search "public APIs list")
#   [ ] 4. Save each response to cache.json with a timestamp; if the internet is down, show
#          the cached version and say how old it is
#   [ ] 5. Every API call has a timeout and error handling – the dashboard must never crash
#
# Stretch: Add colours with the colorama package (pip install colorama with your venv
# active – then add it to requirements.txt).
#
# Bring it to the next session - working or stuck, both are fine.

import json
import time
import requests

CACHE = "cache.json"
