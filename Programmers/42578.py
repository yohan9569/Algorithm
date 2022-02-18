# 프로그래머스 # 해시 # 위장

def solution(clothes):
    from collections import Counter
    from functools import reduce
    
    cc = Counter(j for i,j in clothes)
    ccv = (c+1 for c in cc.values())
    ans = reduce(lambda x, y: x*y, ccv) -1 
    
    return ans
