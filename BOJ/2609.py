# 수학 / 브론즈 1 / 최대공약수와 최소공배수


import math as m

a,b = map(int, input().split())
print(m.gcd(a,b), m.lcm(a,b))
