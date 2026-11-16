# common_items: O(n × m) because `x in b` on a list is O(m)
def common_items_fast(a, b):
    bset = set(b)                       # O(m)
    return [x for x in a if x in bset]  # O(n)  -> O(n + m)

# count_each: O(n²) because words.count is O(n) inside a loop
def count_each_fast(words):
    counts = {}
    for w in words:                     # O(n)
        counts[w] = counts.get(w, 0) + 1
    return counts

# is_sorted: already O(n) – optimal, you have to look at every item

print(common_items_fast([1, 2, 3, 4], [3, 4, 5]))
print(count_each_fast("a b a c a".split()))
