def sierpinski(n):
    if n == 0:
        return ["*"]
    smaller = sierpinski(n - 1)
    pad = " " * (2 ** (n - 1))
    top = [pad + line + pad for line in smaller]
    bottom = [line + " " + line for line in smaller]
    return top + bottom


def permutations(word):
    if len(word) <= 1:
        return [word]
    result = []
    for i, ch in enumerate(word):
        for rest in permutations(word[:i] + word[i + 1:]):
            result.append(ch + rest)
    return result


def flood_fill(grid, r, c, new, old=None):
    if old is None:
        old = grid[r][c]
        if old == new:
            return
    if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] != old:
        return
    grid[r][c] = new
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        flood_fill(grid, r + dr, c + dc, new, old)


memo = {}
def count_paths(rows, cols):
    if rows == 1 or cols == 1:
        return 1
    if (rows, cols) not in memo:
        memo[(rows, cols)] = count_paths(rows - 1, cols) + count_paths(rows, cols - 1)
    return memo[(rows, cols)]


def power_set(items):
    if not items:
        return [[]]
    rest = power_set(items[1:])
    return rest + [[items[0]] + s for s in rest]


print("\n".join(sierpinski(3)))
print(permutations("abc"))
grid = [list(row) for row in ["....#", ".##.#", ".#..#", "####."]]
flood_fill(grid, 0, 0, "~")
print("\n".join("".join(row) for row in grid))
print(count_paths(3, 3), count_paths(16, 16))
print(len(power_set([1, 2, 3, 4])))
