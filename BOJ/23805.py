# 구현 / 브론즈 3 / 골뱅이 찍기 - 돌아간 ㄹ

n=int(input())
a='@'*n
b=' '*n
for i in[1,0,0,0,2]:
    for j in range(n):
        if i>1:print(a+b+a*3)
        elif i:print(a*3+b+a)
        else:print(a+b+a+b+a)
