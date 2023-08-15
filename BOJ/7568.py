# 브루트포스 / 실버 5 / 덩치


xy = []
ans = []

for _ in range(int(input())):
    xy.append(tuple(int(i) for i in input().split()))
    
for i in xy:
    cnt=0
    
    for j in xy:
        if i[0]<j[0] and i[1]<j[1]: 
          cnt+=1
    
    ans.append(cnt+1)
    
print(' '.join(str(i) for i in ans))
