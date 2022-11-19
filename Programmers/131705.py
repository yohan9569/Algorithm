# 연습문제 lv1. 삼총사


from itertools import combinations as cb

def solution(number):
    return [sum(c) for c in cb(number, 3)].count(0)
