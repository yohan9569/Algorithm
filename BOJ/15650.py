# 백트래킹 / 실버 3 / N과 M (2)


from itertools import combinations as cm

n,m = map(int, input().split())
arr = [i for i in range(1,n+1)]
nCm = cm(arr,m)

for c in nCm:
    print(*c, sep=' ')
