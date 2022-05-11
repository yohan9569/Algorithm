# boj 백준 백트래킹 15652번 N과 M (4)


from itertools import combinations_with_replacement as cr

n,m = map(int, input().split())
arr = [i for i in range(1,n+1)]
nCm = cr(arr,m)

for c in nCm:
    print(*c, sep=' ')
