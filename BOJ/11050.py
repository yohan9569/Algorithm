# 수학 / 브론즈 1 / 이항 계수 1


n,k=map(int, input().split())
ans=1

for i in range(n,(n-k),-1):
    ans *= i
for j in range(k,1,-1):
    ans //= j

print(ans)



# another way - comb 메서드 배웠다.
import math
print(math.comb(*map(int,input().split())))
