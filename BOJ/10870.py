# 백준 10870 재귀 - 피보나치 수 5

def fibonacci(n):
    if n==0: 
      return 0
    elif n==1: 
      return 1
    elif n>1: 
      return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(int(input())))
