# 2577번
a,b,c = [int(input()) for _ in range(3)]
s = list(str(a*b*c))
d=dict()
for i in range(10): d[str(i)]=0
for n in s:
    d[n]+=1
print(*d.values(), sep='\n')
