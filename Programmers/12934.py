# 연습문제 lv1. 정수 제곱근 판별

def solution(n):
    root = n**(1/2)
    if root % 1 == 0:
        return (root+1)**2
    else:
        return -1
