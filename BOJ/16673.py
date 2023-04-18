# 수학 / 브론즈 3 / 고려대학교에는 공식 와인이 있다

c,k,p=map(int,input().split())
print(sum(k*n+p*(n**2)for n in range(c+1)))
