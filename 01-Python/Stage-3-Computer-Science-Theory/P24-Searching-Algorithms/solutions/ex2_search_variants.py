def find_all(items, target):
    return [i for i, x in enumerate(items) if x == target]

def first_greater(sorted_items, x):
    low, high = 0, len(sorted_items)
    while low < high:
        mid = (low + high) // 2
        if sorted_items[mid] <= x:
            low = mid + 1
        else:
            high = mid
    return sorted_items[low] if low < len(sorted_items) else None

def find_by(records, key, value):
    for r in records:
        if r[key] == value:
            return r
    return None

print(find_all([1, 3, 1, 2, 1], 1))            # [0, 2, 4]
print(first_greater([2, 4, 4, 7, 10], 4))      # 7
people = [{"name": "Ana", "age": 13}, {"name": "Ben", "age": 15}]
print(find_by(people, "age", 15))
