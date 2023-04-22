# 구현 / 브론즈 3 / 조교는 새디스트야!!

n = int(input())
l = map(int, input().split())
print(sum(i!=j for i,j in zip(l, range(1,n+1))))
