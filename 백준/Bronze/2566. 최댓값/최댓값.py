grid = [[*map(int, row.split())] for row in open(0)]
Max = -1
for i in range(9):
    for j in range(9):
        if Max < grid[i][j]:
            Max, row, col = grid[i][j], i, j
print(Max, '\n', row+1, ' ', col+1)