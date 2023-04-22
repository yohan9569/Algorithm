# 구현 / 브론즈 3 / 조교는 새디스트야!!

n = int(input())
l = map(int, input().split())
print(sum(i!=j for i,j in zip(l, range(1,n+1))))



# another way - str으로 비교
i=0;print(sum(str(i:=i+1)!=j for j in[*open(0)][1].split()))
