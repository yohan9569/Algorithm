# 조합론 / 실버 3 / 사탕 나눠주기 - 푸는 중

# from itertools import combinations as cb
import math

n = int(input())
l = sorted(map(int, input().split()), reverse=True)
ans = set()

for i, v in enumerate(l):
    ans += cb(l[i+1:], v-1)  # 요소 중복 없는 경우만 카운트 해야 함.
    
    math.comb(len(l)-i-1, v-1)

print(ans)
