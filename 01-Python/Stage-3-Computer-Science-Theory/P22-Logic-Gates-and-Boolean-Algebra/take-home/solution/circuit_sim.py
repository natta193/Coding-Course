from itertools import product


def truth_table(expr):
    names = [v for v in "ABC" if v in expr]
    rows = []
    for values in product([False, True], repeat=len(names)):
        env = dict(zip(names, values))
        result = bool(eval(expr, {"__builtins__": {}}, env))
        rows.append((values, result))
    return names, rows


def show(expr):
    try:
        names, rows = truth_table(expr)
    except Exception as e:
        print("Couldn't understand that:", e)
        return None
    print(" ".join(names), "| Q")
    for values, result in rows:
        print(" ".join(str(int(v)) for v in values), "|", int(result))
    trues = sum(r for _, r in rows)
    print(f"{trues}/{len(rows)} rows True" + ("  – a tautology!" if trues == len(rows) else ""))
    return [r for _, r in rows]


a = show(input("Expression 1: "))
b = show(input("Expression 2: "))
if a is not None and b is not None:
    print("Equivalent!" if a == b else "Not equivalent.")

# De Morgan checks: "not (A and B)" ≡ "not A or not B"  ✓
#                   "not (A or B)"  ≡ "not A and not B" ✓
