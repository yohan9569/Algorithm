# 정렬 / 브론즈 1 / 수 정렬하기 3


import sys

n=int(input())
a=[0]*10001 # 인덱스를 숫자 대용으로 쓰기 위해. 0도 있으니 +1

for _ in range(n):
    x=int(sys.stdin.readline())
    a[x]+=1
    
for i in range(len(a)):
    if a[i]:
        for _ in range(a[i]): # 중복이 있을 수 있다.
           print(i)
