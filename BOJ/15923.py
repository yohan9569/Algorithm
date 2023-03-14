# 수학,구현 / 브론즈 3 / 욱제는 건축왕이야!!

n=int(input())
l=[[*map(int,input().split())] for _ in range(n)]
ans=0
for i in range(n):
    j=i+1
    if i==n-1:
        j=0
    a,b=l[i]
    c,d=l[j]
    ans+=abs(a-c)+abs(b-d)
print(ans)
