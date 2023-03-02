# 구현 / 브론즈 3 / 골뱅이 찍기 - 돌아간 ㅍ

n = int(input())
for i in range(5):
    for j in range(n):
        if i%2:
            print('@'*5*n)
        else:
            print('@'*n + '   '*n + '@'*n)
