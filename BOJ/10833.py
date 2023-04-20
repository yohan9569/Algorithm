# 수학 / 브론즈 3 / 사과

a = 0
for r in [*open(0)][1:]:
  n,m = map(int,r.split())
  a += m%n
print(a)
