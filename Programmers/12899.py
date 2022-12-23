# 연습문제 lv2. 124 나라의 숫자


def solution(n):
    ans = ''
    trans_124 = ['4', '1', '2']
    
    while n:
        n, r = divmod(n, 3)
        ans = trans_124[r] + ans
        if r == 0:
            n -= 1
    
    return ans
