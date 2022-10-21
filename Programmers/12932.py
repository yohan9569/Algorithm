# 연습문제 lv1. 자연수 뒤집어 배열로 만들기

def solution(n):
    return [*map(int, reversed(str(n)))]
