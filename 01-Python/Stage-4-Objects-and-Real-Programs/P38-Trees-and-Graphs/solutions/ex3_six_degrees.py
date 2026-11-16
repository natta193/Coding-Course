from collections import deque
import itertools

FRIENDS = {
    "Ana": ["Ben", "Cai", "Eli"], "Ben": ["Ana", "Dev"], "Cai": ["Ana", "Fay"],
    "Dev": ["Ben", "Gus", "Hal"], "Eli": ["Ana", "Ivy"], "Fay": ["Cai", "Jon"],
    "Gus": ["Dev", "Kim"], "Hal": ["Dev", "Lou"], "Ivy": ["Eli", "Max"],
    "Jon": ["Fay", "Nia"], "Kim": ["Gus"], "Lou": ["Hal", "Oli"],
    "Max": ["Ivy"], "Nia": ["Jon", "Oli"], "Oli": ["Lou", "Nia"],
}

def degrees(a, b):
    queue = deque([(a, 0)])
    seen = {a}
    while queue:
        person, d = queue.popleft()
        if person == b:
            return d
        for f in FRIENDS[person]:
            if f not in seen:
                seen.add(f)
                queue.append((f, d + 1))
    return None

def friends_of_friends(a):
    direct = set(FRIENDS[a])
    suggestions = set()
    for f in direct:
        suggestions |= set(FRIENDS[f])
    return suggestions - direct - {a}

def is_connected():
    start = next(iter(FRIENDS))
    stack, seen = [start], {start}
    while stack:
        p = stack.pop()
        for f in FRIENDS[p]:
            if f not in seen:
                seen.add(f)
                stack.append(f)
    return len(seen) == len(FRIENDS)

print("Ana → Oli:", degrees("Ana", "Oli"))
print("Suggestions for Ana:", friends_of_friends("Ana"))
print("Connected:", is_connected())
far = max(itertools.combinations(FRIENDS, 2), key=lambda pair: degrees(*pair))
print("Furthest apart:", far, degrees(*far))
