# 완전탐색 lv2. 피로도
# 순열을 이용한 완전 탐색

from itertools import permutations

def solution(k, dungeons):
    perm = permutations(dungeons)
    ans = []
    
    for case in perm:
        tmp_k = k
        cnt = 0
        for req, use in case:
            if tmp_k >= req:
                tmp_k -= use
                cnt += 1
            if tmp_k < 0:
                break
                
        if cnt == len(dungeons):
            return cnt
        ans.append(cnt)
    
    return max(ans)
