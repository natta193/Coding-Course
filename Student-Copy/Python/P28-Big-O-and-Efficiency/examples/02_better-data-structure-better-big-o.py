def has_duplicate_fast(items):    # O(n)
    seen = set()
    for x in items:
        if x in seen:             # O(1) set lookup!
            return True
        seen.add(x)
    return False
