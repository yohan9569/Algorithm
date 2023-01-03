# 연습문제 lv2. 점 찍기


def solution(k, d):
    ans = 0
    for x in range(0, d+1, k):
        y_lim = int((d**2 - x**2)**0.5)
        ans += y_lim // k + 1
    return ans
