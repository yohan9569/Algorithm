# 연습문제 lv1. 소수 찾기

def solution(n):
    n+=1
    arr=[1]*n
    for i in range(2,int(n**0.5)+1):
        if arr[i]:
            for j in range(2*i,n,i):
                arr[j]=0
    return sum(arr[2:])
