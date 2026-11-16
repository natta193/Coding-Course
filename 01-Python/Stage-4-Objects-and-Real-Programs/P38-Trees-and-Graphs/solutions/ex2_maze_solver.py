from collections import deque

MAZE = [
    "##########",
    "#S...#...#",
    "#.##.#.#.#",
    "#.#..#.#.#",
    "#.#.##.#.#",
    "#...#..#E#",
    "###...####",
    "##########",
]

def find(ch):
    for r, row in enumerate(MAZE):
        if ch in row:
            return r, row.index(ch)

def solve():
    start, end = find("S"), find("E")
    queue = deque([start])
    came_from = {start: None}
    while queue:
        cell = queue.popleft()
        if cell == end:
            break
        r, c = cell
        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if MAZE[nr][nc] != "#" and (nr, nc) not in came_from:
                came_from[(nr, nc)] = cell
                queue.append((nr, nc))
    if end not in came_from:
        return None
    path, cell = [], end
    while cell:
        path.append(cell)
        cell = came_from[cell]
    return path[::-1]

path = solve()
grid = [list(row) for row in MAZE]
for r, c in path[1:-1]:
    grid[r][c] = "*"
print("\n".join("".join(row) for row in grid))
print(f"Shortest path: {len(path) - 1} steps")
