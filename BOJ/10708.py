# 구현 / 브론즈 2 / 크리스마스 파티

i=input
N=int(i());i()
t=map(int,i().split())
a=[0]*N
for j in t:
    for k,g in enumerate(map(int,i().split())):
        if g==j:a[k]+=1
        else:a[j-1]+=1
print(*a)
