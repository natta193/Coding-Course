import requests

def get_json(url, params):
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Network problem:", e)
        return None

city = input("City: ")
geo = get_json("https://geocoding-api.open-meteo.com/v1/search", {"name": city, "count": 1})
if not geo or not geo.get("results"):
    print("City not found")
else:
    place = geo["results"][0]
    wx = get_json("https://api.open-meteo.com/v1/forecast", {
        "latitude": place["latitude"], "longitude": place["longitude"],
        "current": "temperature_2m,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min", "forecast_days": 3, "timezone": "auto"})
    if wx:
        cur = wx["current"]
        print(f"\n{place['name']}, {place.get('country', '')}: {cur['temperature_2m']}°C, wind {cur['wind_speed_10m']} km/h")
        d = wx["daily"]
        for day, hi, lo in zip(d["time"], d["temperature_2m_max"], d["temperature_2m_min"]):
            print(f"  {day}: {lo}–{hi}°C")
