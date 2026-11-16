import json
import time

import requests

CACHE = "cache.json"
TOWN = "Cambridge"


def load_cache():
    try:
        with open(CACHE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def fetch(key, url, params, cache):
    try:
        r = requests.get(url, params=params, timeout=8)
        r.raise_for_status()
        data = r.json()
        cache[key] = {"time": time.time(), "data": data}
        return data, None
    except requests.exceptions.RequestException:
        if key in cache:
            age = int((time.time() - cache[key]["time"]) / 60)
            return cache[key]["data"], f"(offline – cached {age} min ago)"
        return None, "(unavailable)"


cache = load_cache()
print("=" * 40, "\n  GOOD MORNING!  " + time.strftime("%A %d %B"), "\n" + "=" * 40)

geo, note = fetch("geo", "https://geocoding-api.open-meteo.com/v1/search", {"name": TOWN, "count": 1}, cache)
if geo and geo.get("results"):
    place = geo["results"][0]
    wx, note = fetch("weather", "https://api.open-meteo.com/v1/forecast",
                     {"latitude": place["latitude"], "longitude": place["longitude"],
                      "current": "temperature_2m,wind_speed_10m"}, cache)
    if wx:
        c = wx["current"]
        print(f"🌤  {TOWN}: {c['temperature_2m']}°C, wind {c['wind_speed_10m']} km/h {note or ''}")
else:
    print("🌤  Weather", note)

joke, note = fetch("joke", "https://official-joke-api.appspot.com/random_joke", None, cache)
if joke:
    print(f"😂 {joke['setup']}\n   {joke['punchline']} {note or ''}")
else:
    print("😂 Joke", note)

with open(CACHE, "w") as f:
    json.dump(cache, f)
