# 연습문제 lv1. 정수 내림차순으로 배치하기

def solution(n):
    # return int("".join(map(str, sorted(map(int, str(n)), reverse=True))))
    return int("".join(sorted(str(n), reverse=True)))
