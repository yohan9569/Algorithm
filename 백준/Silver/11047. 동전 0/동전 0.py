n,k=map(int,input().split())
Ai=[int(input()) for _ in range(n)]

ans=0
for a in reversed(Ai):
    q=k//a
    if q:
        k-=(a*q)
        ans+=q

print(ans)