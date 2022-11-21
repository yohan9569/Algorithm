# 연습문제 lv2. 멀리 뛰기
# 피보나치 수열


def solution(n):
    a, b = 0, 1
    
    for _ in range(n):
        a, b = b, a+b
        
    return b % 1234567
