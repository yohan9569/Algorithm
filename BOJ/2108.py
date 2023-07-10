# 정렬 / 실버 3 / 통계학


import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = sorted([int(sys.stdin.readline()) for _ in range(n)])
# 중앙값 때만 sort하면, 최빈값 때 제대로 정렬되어있지 않아서 문제되는 것 같다.

print(round(sum(nums)/n))
print(nums[n//2])

mod = Counter(nums).most_common()
if len(mod)>1 and mod[0][1] == mod[1][1]: 
    print(mod[1][0])
else: 
    print(mod[0][0])

print(nums[-1]-nums[0])
