# boj 백준 백트래킹 15650번 N과 M (2)


from itertools import combinations as cm

n,m = map(int, input().split())
arr = [i for i in range(1,n+1)]
nCm = cm(arr,m)

for c in nCm:
    print(*c, sep=' ')
