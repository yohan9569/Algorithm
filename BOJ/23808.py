# 구현 / 브론즈 3 / 골뱅이 찍기 - ㅂ

n = int(input())
for i in [0,0,1,0,1]:
    for j in range(n):
        if i:
            print('@'*5*n)
        else:
            print('@'*n+'   '*n+'@'*n)
