# 백트래킹 / 골드 4 / N-Queen
# 전제: 같은 행에 둘 수 없다. arr의 index가 행, value가 열이라고 생각하고 채워가기.
# 풀이 순서
    # 1. 백트래킹 함수 - 재귀 사용
    # 2. promise 가망성 함수
    # 3. 함수 실행 파트

    
def backtrack(n:int, arr:list, idx:int):
    global ans
    
    for j in range(n):
        arr[idx] = j
        
        if promise(arr,idx):
            if idx==(n-1):
                ans += 1
                return
                
            else: backtrack(n, arr, idx+1)


def promise(arr:list, idx:int)->bool:
    k = 0
    
    while idx>k:
        if arr[idx]==arr[k] or abs(arr[idx]-arr[k])==(idx-k):
            return False
        k += 1
        
    return True

n = int(input())
arr = [-1]*n # value가 될 0~(n-1)과 겹치지 않도록
ans = 0
backtrack(n,arr,0)
print(ans)
