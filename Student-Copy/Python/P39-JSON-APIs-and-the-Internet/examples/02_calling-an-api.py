import requests   # in requirements.txt

url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 52.2, "longitude": 0.12,   # Cambridge
          "current": "temperature_2m,wind_speed_10m"}

response = requests.get(url, params=params, timeout=10)
print(response.status_code)          # 200
data = response.json()               # JSON -> dict
now = data["current"]
print(f"{now['temperature_2m']}°C, wind {now['wind_speed_10m']} km/h")
