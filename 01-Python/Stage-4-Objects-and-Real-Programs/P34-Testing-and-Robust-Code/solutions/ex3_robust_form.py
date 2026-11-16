import hashlib
import json
import re

USERS_FILE = "users.json"

def load_users():
    try:
        with open(USERS_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def ask(prompt, check):
    while True:
        value = input(prompt).strip()
        error = check(value)
        if error is None:
            return value
        print("  ✗", error)

def check_username(u, users):
    if not 3 <= len(u) <= 15:
        return "Must be 3-15 characters"
    if not re.fullmatch(r"\w+", u):
        return "Letters, digits and _ only"
    if u.lower() in users:
        return "Username taken"
    return None

def check_email(e):
    return None if re.fullmatch(r"[^@\s]+@[^@\s]+\.[a-z]{2,}", e, re.I) else "Not a valid email"

def check_age(a):
    if not a.isdigit():
        return "Must be a whole number"
    return None if 13 <= int(a) <= 120 else "Must be 13-120"

def check_password(p):
    if not 8 <= len(p) <= 20:
        return "8-20 characters"
    if not (any(c.isdigit() for c in p) and any(c.isupper() for c in p) and any(c.islower() for c in p)):
        return "Needs a digit, an upper and a lower case letter"
    return None

users = load_users()
name = ask("Username: ", lambda u: check_username(u, users))
email = ask("Email: ", check_email)
age = int(ask("Age: ", check_age))
pw = ask("Password: ", check_password)
users[name.lower()] = {"email": email, "age": age, "password": hashlib.sha256(pw.encode()).hexdigest()}
with open(USERS_FILE, "w") as f:
    json.dump(users, f, indent=2)
print("Account created!")
