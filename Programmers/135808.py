# 연습문제 lv1. 과일 장수

def solution(k, m, score):
    score.sort(reverse=True)
    ans = 0
    for i in range(m-1, len(score), m):
        ans += score[i] * m
    return ans
