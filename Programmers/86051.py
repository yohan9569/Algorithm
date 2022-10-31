# 월간 코드 챌린지 시즌3 lv1. 없는 숫자 더하기

def solution(numbers):
    ans = set(range(10))
    ans -= set(numbers)
    return sum(ans)
