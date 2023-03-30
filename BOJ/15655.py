# 백트래킹 / 실버 3 / N과 M (6)

from itertools import combinations as c
n,m=map(int,input().split())
l=sorted(map(int,input().split()))
for p in sorted(c(l,m)):
    print(*p)
