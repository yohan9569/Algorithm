def is_valid(x, y, val):
    global grid

    if val in grid[x]:
        return False

    if val in [grid[i][y] for i in range(9)]:
        return False

    box_x, box_y = (x // 3) * 3, (y // 3) * 3
    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if grid[i][j] == val:
                return False
    return True

def dfs(d):
    global grid, zeros
    if d == len(zeros):
        return True

    x, y = zeros[d]
    for i in range(1, 10):
        if is_valid(x, y, i):
            grid[x][y] = i
            if dfs(d + 1):
                return True
            grid[x][y] = 0

    return False

def is_initial_grid_valid():
    global grid
    
    for i in range(9):
        row = [x for x in grid[i] if x != 0]
        col = [grid[j][i] for j in range(9) if grid[j][i] != 0]
        if len(row) != len(set(row)) or len(col) != len(set(col)):
            return False
    for box_x in range(0, 9, 3):
        for box_y in range(0, 9, 3):
            box = [
                grid[i][j]
                for i in range(box_x, box_x + 3)
                for j in range(box_y, box_y + 3)
                if grid[i][j] != 0
            ]
            if len(box) != len(set(box)):
                return False
    return True

n = int(input())
for _ in range(n):
    grid = [[*map(int, input())] for _ in range(9)]
    zeros = [(r, c) for r in range(9) for c in range(9) if grid[r][c] == 0]

    if not is_initial_grid_valid():
        print("Could not complete this grid.")
        print()
        continue

    if dfs(0):
        for row in grid:
            print(*row, sep="")
    else:
        print("Could not complete this grid.")
    print()
