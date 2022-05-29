# boj 백준 그리디 1541번 잃어버린 괄호


q = input().split('-')

for i,v in enumerate(q):
    if '+' in v: 
        v1 = sum([*map(int, v.split('+'))])
    else: 
        v1 = int(v)
        
    if i==0: 
        ans = v1
    else: 
        ans -= v1
        

print(ans)
