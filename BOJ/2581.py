# 수학 / 브론즈 2 / 소수


s=set()

for i in range(int(input()), int(input())+1):
    if i == 1: 
        continue
    
    a=0
    
    for j in range(2,i):
        if i%j == 0: 
            a=1
            break
    
    if a:
        continue
    
    s.add(i)
    
if len(s) == 0: 
    print(-1)
    
else: 
    print(sum(s))
    print(min(s))
