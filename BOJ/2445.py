# 구현 / 브론즈 3 / 별 찍기 - 8

n = int(input())
for i in range(1, n*2):
    if i < n:
        print('*'*i + ' '*(n*2 - i*2) + '*'*i)
    else:
        j = n*2 - i
        print('*'*j + ' '*(n*2 - j*2) + '*'*j)
