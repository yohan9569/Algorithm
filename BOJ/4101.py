# 구현 / 브론즈 5 / 크냐?

while (s:=input()) > '1':
    x,y = map(int, s.split())
    print('YNeos'[x<=y::2])


# another way
for x,y in [map(int, a.split()) for a in [*open(0)][:-1]]:
    print('YNeos'[x<=y::2])
