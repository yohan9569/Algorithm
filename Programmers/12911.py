# 연습문제 lv2. 다음 큰 숫자

def solution(n):
    num1 = bin(n).count('1')
    ans = n+1
    while bin(ans).count('1') != num1:
        ans += 1
    return ans
