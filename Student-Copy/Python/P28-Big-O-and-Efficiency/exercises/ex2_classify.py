def common_items(a, b):
    result = []
    for x in a:
        if x in b:
            result.append(x)
    return result

def count_each(words):
    counts = []
    for w in words:
        counts.append((w, words.count(w)))
    return counts

def is_sorted(items):
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True
