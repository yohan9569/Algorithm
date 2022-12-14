# 연습문제 lv2. 귤 고르기


from collections import Counter

def solution(k, tangerine):
    c = Counter(tangerine)
    tangerine.sort(key = lambda x: (c[x], x), reverse=True)
    ans = tangerine[:k]
    return len(set(ans))
