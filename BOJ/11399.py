# 그리디 / 실버 4 / ATM

from functools import reduce

n = int(input())
pi = sorted([*map(int, input().split())])
res = [reduce(lambda x,y: x+y, pi[:i+1]) for i in range(n)]

print(sum(res))
