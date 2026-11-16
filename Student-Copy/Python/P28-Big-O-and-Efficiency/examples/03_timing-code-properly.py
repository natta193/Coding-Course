import timeit

setup = "data = list(range(10_000)); s = set(data)"
t_list = timeit.timeit("9_999 in data", setup, number=1_000)
t_set = timeit.timeit("9_999 in s", setup, number=1_000)
print(f"list: {t_list:.4f}s   set: {t_set:.6f}s")
