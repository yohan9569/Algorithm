# 수학 / 브론즈 1 / 부녀회장이 될테야


for _ in range(int(input())):
    k = int(input())
    n = int(input())
    a = [i for i in range(1,n+1)]
    
    while k>1:
        a = [sum(a[:i+1]) for i in range(n)]
        k -= 1
        
    print(sum(a))
