# 수학 / 브론즈 2 / 손익분기점

a,b,c = map(int,input().split())

if c==b: 
    print(-1)
    
else:
    n = int(a/(c-b))
    if n<0: 
        print(-1)
    else: 
        print(n+1)
