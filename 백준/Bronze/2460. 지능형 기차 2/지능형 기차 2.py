c=m=0
for r in [*open(0)]:
    a,b=map(int,r.split())
    c+=b-a
    m=max(c,m)
print(m)