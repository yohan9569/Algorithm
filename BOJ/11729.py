# 재귀 / 실버 1 / 하노이 탑 이동 순서

def hanoi(n, from_, to_):
    if n==1:
        print(from_, to_, sep=' ')
        return
      
    hanoi(n-1, from_, 6-from_-to_)
    print(from_, to_, sep=' ')
    hanoi(n-1, 6-from_-to_, to_)
    return
  
def aaa(n):
    if n==1:
        return 1
      
    return 1 + 2*aaa(n-1)
  
n = int(input())
print(aaa(n))
hanoi(n, 1, 3)
