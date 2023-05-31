# 수학 / 브론즈 1 / 더하기 사이클

n = int(input())
num = n

cycle = 0

while 1:
    a,b = divmod(n,10)
    c = (a+b)%10
    n = (10*b)+c
    cycle += 1
    if n == num:
        break
      
print(cycle)
