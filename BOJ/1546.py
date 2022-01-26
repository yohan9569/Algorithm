# 1546
N=int(input())
a=[int(i) for i in input().split()]
print(sum(i/max(a)*100 for i in a)/N)
