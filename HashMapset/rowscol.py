grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
grid_t = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
print(grid_t)

count = 0
for row in grid:
    for t_row in grid_t:
        if row == t_row:
            count += 1

print(count)
