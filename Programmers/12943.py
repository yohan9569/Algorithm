# 연습문제 lv1. 콜라츠 추측

def solution(n):
    for i in range(500):
        if n==1:
            return i
        elif n%2==0:
            n //= 2
        else:
            n = n*3+1
    
    return -1
