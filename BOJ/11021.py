# 구현 / 브론즈 5 / A+B - 7

a=1

for _ in range(int(input())):
    print("Case #",a,": ",sum(map(int,input().split())),sep='')
    a+=1
