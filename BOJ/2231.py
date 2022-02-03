# 2231번 분해합

n = int(input())

for i in range(n):
    if i+sum(int(j) for j in list(str(i))) == n:
        print(i)
        break
        
    elif i == n-1:
        print(0)
