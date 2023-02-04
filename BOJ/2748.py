# 다이나믹프로그래밍, 수학 / 브론즈 1 / 피보나치 수 2


a,b,n = 0,1,int(input())

while n:
    a,b=b,a+b
    n-=1
    
print(a)
