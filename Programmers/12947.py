# 연습문제 lv1. 하샤드 수

def solution(x):
    return x % sum(map(int, str(x))) == 0
