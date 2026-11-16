text = """Paste a paragraph of any text here. The longer the better,
because frequency analysis works best with lots of letters."""

counts = {}
for ch in text.lower():
    if ch.isalpha():
        counts[ch] = counts.get(ch, 0) + 1

top = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:5]
for letter, n in top:
    print(f"{letter}: {'█' * n} {n}")
