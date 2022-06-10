# programmers 12977번 Summer/Winter Coding(~2018) lv.1 소수 만들기

# 세 수 조합 리스트를 만든다.
# 가장 큰 수 이하 소수를 찾는다 (에스토스테네스의 체).
# 조합 리스트 원소들이 소수인지 확인한다.

from math import sqrt
from itertools import combinations

def solution(nums):
    comb_list = [sum(c) for c in combinations(nums, 3)]
    max_num = max(comb_list)+1
    arr = [1]*max_num
    
    for i in range(2, int(sqrt(max_num))+1):
        if arr[i]:
            for j in range(2*i, max_num, i):
                arr[j] = 0
    
    ans = 0
    for c in comb_list:
        if arr[c]:
            ans += 1
        
    return ans
