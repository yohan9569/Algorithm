# 수학 / 브론즈 1 / 최소공배수


from math import lcm

for _ in range(int(input())):
    a,b = map(int, input().split())
    print(lcm(a,b))
