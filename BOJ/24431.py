# 해시를 사용한 집합과 맵 / 실버 4 / 유사 라임 게임


from collections import Counter as C

for _ in range(int(input())):
    n,L,F = map(int, input().split())
    w = [x[-F:] for x in input().split()]
    print(sum(i//2 for i in C(w).values()))
