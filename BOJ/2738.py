# 2차원 배열 / 브론즈 5 / 행렬 덧셈


n, m = map(int, input().split())
a = [[*map(int, input().split())] for _ in range(n)]
b = [[*map(int, input().split())] for _ in range(n)]
ans = [[a[i][j] + b[i][j] for j in range(m)] for i in range(n)]

for i in ans:
    print(*i)
