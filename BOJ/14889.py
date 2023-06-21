# 백트래킹, 브루트포스 / 실버 2 / 스타트와 링크

# 입력을 받아 어레이를 만든다.
# 팀 조합 경우의 수를 뽑는다. nC(n//2)
# 경우마다 두 팀의 차이를 구한다. (set minus 이용)
# 최소를 출력한다.


from itertools import combinations as cm, permutations as pm
import sys

# 입력을 받아 어레이를 만든다.
n=int(input())
arr=[]
for i in range(n):
    arr.append([*map(int, sys.stdin.readline().split())])
    
# 팀 조합 경우의 수를 뽑는다. nC(n//2)
startlink=set(i for i in range(n)) # 전체 팀원
start=cm(startlink, n//2)

# 경우마다 두 팀의 차이를 구한다. (sum of arr에서 빼기 -> 안됨.)
# 한 조합 내에서 ij 순열 뽑아서 계산
case=[]
for s in start:
    link=startlink-set(s)
    
		# 팀 1
    sij=pm(s, 2)
    temp=0
    for i,j in sij:
        temp+=arr[i][j]
    
		# 팀 2
    lij=pm(link, 2)
    temp2=0
    for j,k in lij:
        temp2+=arr[j][k]

    case.append(abs(temp-temp2))

# 최소를 출력한다.
print(min(case))
