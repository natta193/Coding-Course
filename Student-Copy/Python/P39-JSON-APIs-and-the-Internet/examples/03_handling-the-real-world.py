def get_json(url, params=None):
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()      # error on 4xx/5xx
        return r.json()
    except requests.exceptions.Timeout:
        print("Server took too long")
    except requests.exceptions.ConnectionError:
        print("No internet connection?")
    except requests.exceptions.HTTPError as e:
        print("Server said no:", e)
    return None
