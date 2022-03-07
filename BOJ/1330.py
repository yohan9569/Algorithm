# 1330 번  두 수 비교하기

a,b=map(int,input().split())
c=a-b

if c<0: print("<")
elif c>0: print(">")
else: print("==")
