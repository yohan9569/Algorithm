# 조합론 / 실버 3 / 사탕 나눠주기


from collections import Counter as C

input()
c = C(map(int,input().split()))
ans = 0
tmp = 1

for i in range(1,51):
    tmp*=c[i]
    ans+=tmp

print(ans)
