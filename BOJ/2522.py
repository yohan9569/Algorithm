# 구현 / 브론즈 3 / 별 찍기 - 12

n = int(input())
l = [' '*(n-i) + '*'*i for i in range(1,n+1)]
print(*l, sep='\n')
print(*l[-2::-1], sep='\n')


# another ways - abs, ljust 활용
for i in range(1-n,n):
    print((' '*abs(i)).ljust(n,'*'))
