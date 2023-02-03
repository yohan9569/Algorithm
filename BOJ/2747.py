# 수학 / 브론즈 2 / 피보나치 수

a,b,n = 0,1,int(input())

while n>1:
    a,b = b,a+b
    n-=1

print(b)
