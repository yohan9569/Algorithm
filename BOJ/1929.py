# 수학 / 실버 3 / 소수 구하기
# 에라토스테네스의 체

from math import sqrt

m,n=map(int,input().split())
n+=1
arr=[1]*n # 숫자를 직접 넣지 않고 인덱스로 구별 # 그래서 n+=1

for i in range(2,int(sqrt(n))+1):
    if arr[i]:
        for j in range(2*i,n,i):
            arr[j]=0
            
for i in range(m,n):
    if i>1 and arr[i]:
        print(i)
