# 완전탐색 lv1. 최소직사각형

def solution(sizes):
    w = [max(i) for i in sizes]
    h = [min(i) for i in sizes]
    
    return max(w) * max(h)
