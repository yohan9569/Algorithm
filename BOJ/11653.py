# 수학 / 브론즈 1 / 소인수분해

a=[]

def sol(a,n):
    for i in range(1,n+1):
        if i==1:
            continue
            
        elif n%i==0:
            n=n//i
            a.append(i)
            break
    if n>1: 
        sol(a,n)
        
    return a
  
print(*sol(a, int(input())), sep='\n')
