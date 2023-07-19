# 수학 / 브론즈 3 / 오븐 시계

a,b = map(int, input().split())
c = int(input())

d,e = divmod(b+c,60)
f = a+d

if f>23: 
    f%=24

print(f, e, sep=' ')
