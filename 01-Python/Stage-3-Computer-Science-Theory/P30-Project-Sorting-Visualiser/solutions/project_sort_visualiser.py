import random
import time
import turtle

WIDTH, HEIGHT = 800, 500

def bubble(a):
    n = len(a)
    for p in range(n - 1):
        for i in range(n - 1 - p):
            yield (i, i + 1), False
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                yield (i, i + 1), True

def insertion(a):
    for i in range(1, len(a)):
        j = i
        while j > 0:
            yield (j - 1, j), False
            if a[j - 1] <= a[j]:
                break
            a[j - 1], a[j] = a[j], a[j - 1]
            yield (j - 1, j), True
            j -= 1

def merge_sort(a, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    if hi - lo <= 1:
        return
    mid = (lo + hi) // 2
    yield from merge_sort(a, lo, mid)
    yield from merge_sort(a, mid, hi)
    merged, i, j = [], lo, mid
    while i < mid and j < hi:
        yield (i, j), False
        if a[i] <= a[j]:
            merged.append(a[i]); i += 1
        else:
            merged.append(a[j]); j += 1
    merged += a[i:mid] + a[j:hi]
    for k, v in enumerate(merged):
        a[lo + k] = v
        yield (lo + k,), True

def quick(a, lo=0, hi=None):
    if hi is None:
        hi = len(a) - 1
    if lo >= hi:
        return
    pivot, i = a[hi], lo
    for j in range(lo, hi):
        yield (j, hi), False
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            yield (i, j), True
            i += 1
    a[i], a[hi] = a[hi], a[i]
    yield (i, hi), True
    yield from quick(a, lo, i - 1)
    yield from quick(a, i + 1, hi)

SORTS = {"1": ("Bubble", bubble), "2": ("Insertion", insertion), "3": ("Merge", merge_sort), "4": ("Quick", quick)}

def draw(pen, data, highlight, title, comps, writes):
    pen.clear()
    w = (WIDTH - 40) / len(data)
    top = max(data)
    for i, h in enumerate(data):
        pen.color("crimson" if i in highlight else "steelblue")
        bar_h = h / top * (HEIGHT - 120)
        pen.penup(); pen.goto(-WIDTH / 2 + 20 + i * w, -HEIGHT / 2 + 20); pen.pendown()
        pen.begin_fill()
        for side in [max(w - 2, 1), bar_h, max(w - 2, 1), bar_h]:
            pen.forward(side); pen.left(90)
        pen.end_fill()
    pen.penup(); pen.goto(-WIDTH / 2 + 20, HEIGHT / 2 - 50); pen.color("black")
    pen.write(f"{title} sort   comparisons: {comps}   writes: {writes}", font=("Arial", 16, "bold"))

def main():
    for k, (name, _) in SORTS.items():
        print(f"{k}) {name}")
    choice = input("Algorithm: ").strip()
    while choice not in SORTS:
        choice = input("Pick 1-4: ").strip()
    n = int(input("How many bars (10-150)? ") or 50)
    delay = float(input("Delay per step in seconds (e.g. 0.01): ") or 0.01)

    name, algorithm = SORTS[choice]
    data = random.sample(range(1, n + 1), n)
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.tracer(0)
    pen = turtle.Turtle(visible=False)

    comps = writes = 0
    for highlight, was_write in algorithm(data):
        if was_write:
            writes += 1
        else:
            comps += 1
        draw(pen, data, highlight, name, comps, writes)
        screen.update()
        time.sleep(delay)
    draw(pen, data, (), name + " – done!", comps, writes)
    screen.update()
    turtle.done()

if __name__ == "__main__":
    main()
