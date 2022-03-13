# 2884번 알람 시계

h,m=map(int,input().split())
x,y=divmod(60*h+m-45, 60)

if x<0:
  x+=24

print(x,y)
