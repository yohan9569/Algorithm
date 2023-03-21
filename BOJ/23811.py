# 구현 / 브론즈 3 / 골뱅이 찍기 - ㅌ

n=int(input())
a='@'*n
for i in[1,0,1,0,1]:
    for j in range(n):
        if i:print(a*5)
        else:print(a)
