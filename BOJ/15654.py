# 백트래킹 / 실버 3 / N과 M (5)


from itertools import permutations as pm

m = int(input()[-1])
l = sorted(map(int, input().split()))

for c in pm(l,m):
    print(*c)
