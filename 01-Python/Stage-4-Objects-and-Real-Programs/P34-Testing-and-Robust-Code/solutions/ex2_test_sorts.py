import random

def merge_sort(items):
    if len(items) <= 1:
        return items[:]
    mid = len(items) // 2
    l, r = merge_sort(items[:mid]), merge_sort(items[mid:])
    out, i, j = [], 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            out.append(l[i]); i += 1
        else:
            out.append(r[j]); j += 1
    return out + l[i:] + r[j:]

def test_empty():
    assert merge_sort([]) == []

def test_single():
    assert merge_sort([5]) == [5]

def test_duplicates():
    assert merge_sort([3, 1, 3, 1]) == [1, 1, 3, 3]

def test_sorted_and_reversed():
    assert merge_sort(list(range(10))) == list(range(10))
    assert merge_sort(list(range(10, 0, -1))) == list(range(1, 11))

def test_negatives():
    assert merge_sort([0, -5, 3, -1]) == [-5, -1, 0, 3]

def test_random():
    for _ in range(100):
        data = [random.randint(-50, 50) for _ in range(random.randint(0, 30))]
        assert merge_sort(data) == sorted(data)

if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
    print("All tests passed")
