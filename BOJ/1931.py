# boj greedy 1931 회의실 배정
# 각 시점에서 고를 수 있는 것 중 가장 끝나는 시간이 가까운 것을 선택한다.


import sys
from operator import itemgetter

# 받기
meet = [tuple(map(int,sys.stdin.readline().split())) for _ in range(int(input()))]

# 끝나는 시간 기준으로 정렬
meet.sort(key=itemgetter(1,0))

# 답 구하기
ans = 1
now = meet[0]

for m in meet[1:]:
    if m[0] > =now[1]:
        now = m
        ans += 1
        
print(ans)
