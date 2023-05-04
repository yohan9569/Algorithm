# 수학 / 브론즈 3 / 지능형 기차 2

c=m=0
for r in [*open(0)]:
    a,b=map(int,r.split())
    c+=b-a
    m=max(c,m)
print(m)
