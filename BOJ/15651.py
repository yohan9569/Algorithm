# boj 백준 백트래킹 15651번 N과 M (3)


from itertools import product as pr

n,m = map(int, input().split())
arr = [i for i in range(1,n+1)]
nPm = pr(arr,repeat=m)

for p in nPm:
    print(*p, sep=' ')
