# boj 백준 수학 2869번 달팽이는 올라가고 싶다
# Ax - B(x-1) >= V    ->    x >= (V-B)/(A-B)

import math

a,b,v = map(int, input().split())
print(math.ceil((v-b)/(a-b)))
