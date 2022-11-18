# 월간 코드 챌린지 시즌1 lv1. 두 개 뽑아서 더하기

from itertools import combinations as cb

def solution(numbers):
    return sorted({sum(c) for c in cb(numbers, 2)})
