# 백트래킹 / 실버 3 / N과 M (1)


from itertools import permutations as pm

n,m = map(int, input().split())
arr = [i for i in range(1,n+1)]
nPm = pm(arr,m)

for p in nPm:
    print(*p, sep=' ')
