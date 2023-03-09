# 구현 / 브론즈 3 / 골뱅이 찍기 - ㅁ

n=int(input())
m='@'*n
for i in[1,0,0,0,1]:
    for j in range(n):
        if i:print(m*5)
        else:print(m+'   '*n+m)
