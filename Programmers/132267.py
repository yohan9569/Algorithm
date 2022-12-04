# 연습문제 lv1. 콜라 문제


def solution(a, b, n):
    ans = 0
    
    while n >= a:
        q, r = divmod(n, a)
        ans += q*b
        n = q*b + r
        
    return ans
