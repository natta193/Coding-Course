import json
import requests

CACHE_FILE = "pokedex_cache.json"

def load_cache():
    try:
        with open(CACHE_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def lookup(name, cache):
    name = name.lower().strip()
    if name in cache:
        print("(from cache)")
        return cache[name]
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}", timeout=10)
    if r.status_code == 404:
        return None
    r.raise_for_status()
    raw = r.json()
    info = {
        "name": raw["name"], "id": raw["id"],
        "types": [t["type"]["name"] for t in raw["types"]],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in raw["stats"]},
    }
    cache[name] = info
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)
    return info

cache = load_cache()
while True:
    q = input("Pokémon (blank to quit): ")
    if not q:
        break
    p = lookup(q, cache)
    if not p:
        print("Not found!")
        continue
    print(f"#{p['id']} {p['name'].title()} – {', '.join(p['types'])}")
    for stat, val in p["stats"].items():
        print(f"  {stat:16} {'█' * (val // 5)} {val}")
