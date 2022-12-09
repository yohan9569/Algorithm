# 연습문제 lv1. 푸드 파이트 대회

def solution(food):
    a = "".join(f"{i}" * (food[i]//2) for i in range(1, len(food)))
    return a + "0" + a[::-1]
