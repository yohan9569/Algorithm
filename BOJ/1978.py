# boj 수학2 1978번 소수 찾기

ans=0
_=input()


for i in input().split():
    i = int(i)
    
    if sum(i%j==0 for j in range(1,i)) == 1:
        ans+=1

        
print(ans)
