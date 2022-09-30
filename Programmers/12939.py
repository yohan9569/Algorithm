# 최댓값과 최솟값 lv2

def solution(s):
    n = [*map(int, s.split())]
    return f"{min(n)} {max(n)}"
