n=int(input())
a=n//5
while a>=0:
    b=(n-(5*a))//3
    if a*5+b*3==n:
        break
    a-=1
if a*5+b*3!=n:ans=-1
else: ans=a+b
print(ans)