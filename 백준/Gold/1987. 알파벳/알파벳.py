# 입력
r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

# 준비
dx = [0,0,-1,1]
dy = [1,-1,0,0]
max_depth = 1
visited = set(arr[0][0])

# dfs
def dfs(x, y):
    global max_depth
    max_depth = max(max_depth, len(visited))
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<r and 0<=ny<c and arr[nx][ny] not in visited:
            visited.add(arr[nx][ny])
            dfs(nx, ny)
            visited.remove(arr[nx][ny])

# 실행
dfs(0,0)
print(max_depth)
