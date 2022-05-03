# boj 백준 수학 2839번 설탕 배달
# 5 를 하나씩 줄여가면서 3을 늘려간다.

n = int(input())
a = n//5

while a>=0:
    b = (n-(5*a))//3
    
    if a*5 + b*3 == n:
        break
        
    a -= 1
    
if a*5+b*3 != n:
    ans = -1
else: 
    ans = a+b
    
print(ans)
