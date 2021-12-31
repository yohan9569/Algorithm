# 5622번 다이얼
apb = list('abcdefghijklmnopqrstuvwxyz'.upper())
d = dict()
n = 3
for i,a in enumerate(apb):
    d[a] = n
    if a in list('CFILOSV'): n+=1
print(sum(d[p] for p in list(input())))
