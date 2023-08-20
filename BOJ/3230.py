# 구현 / 실버 5 / 금메달, 은메달, 동메달은 누가?


n,m = map(int,input().split())

rank1 = []
for i in range(1, n+1):
    cur = int(input())
    for compare in range(len(rank1)):
        if rank1[compare] >= cur:
            rank1[compare]+=1
    rank1.append(cur)

rank2 = []
for i in range(m, 0, -1):
    cur = int(input())
    for compare in range(len(rank2)):
        if rank2[compare][1] >= cur:
            rank2[compare][1]+=1
    rank2.append([i, cur])
    
rank2.sort(key=lambda x : x[1])

for r2 in rank2[:3]:
    print(rank1.index(r2[0])+1)



# another way - insert 활용
N,M,*l=map(int,open(0).read().split())
a=[0]
for i in range(N):a.insert(l[i],i)
b=[0]
for i in l[N:]:b.insert(i,a[M]+1);M-=1
print(*b[1:4])
