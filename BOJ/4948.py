# 수학 / 실버 2 / 베르트랑 공준( n, 2n 사이 소수 )
# 에라토스테네스의 체


while 1:
    n = int(input())
    
    if n==0: 
        break
    
    n2 = int(n)*2+1
    arr = [1]*n2
    
    for i in range(2,int(n2**0.5)+1):
        if arr[i]:
            for j in range(2*i,n2,i):
                arr[j] = 0
                
                
    print(sum(arr[n+1:]))
