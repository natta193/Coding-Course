def merge(a, b, key=lambda x: x):
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    return out + a[i:] + b[j:]

def merge_sort(items, key=lambda x: x):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    return merge(merge_sort(items[:mid], key), merge_sort(items[mid:], key), key)

classes = [[45, 67, 89], [12, 50, 99], [33, 34, 35], [70], [1, 100]]
ranking = []
for c in classes:
    ranking = merge(ranking, c)
print(ranking)

people = [{"name": "Ana", "age": 15}, {"name": "Ben", "age": 12}, {"name": "Cai", "age": 14}]
print([p["name"] for p in merge_sort(people, key=lambda p: p["age"])])
