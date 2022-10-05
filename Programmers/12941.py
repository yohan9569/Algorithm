# 연습문제 lv2. 최솟값 만들기

def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    return sum(a*b for a,b in zip(A,B))
