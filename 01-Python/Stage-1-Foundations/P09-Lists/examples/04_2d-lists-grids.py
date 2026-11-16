grid = [
    [".", ".", "X"],
    [".", "O", "."],
    ["X", ".", "."],
]

print(grid[0][2])    # X  (row 0, column 2)
grid[1][1] = "#"

for row in grid:
    print(" ".join(row))
