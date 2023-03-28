# 수학 / 브론즈 4 / 특식 배부

n=int(input())
l=map(int,input().split())
print(sum(min(a,n) for a in l))
