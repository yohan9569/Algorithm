# 연습문제 백트래킹 lv2. N-Queen


def backtrack(n:int, arr:list, idx:int, ans:int)->int:
    for j in range(n):
        arr[idx] = j
        if promise(arr,idx):
            if idx == (n-1):
                ans += 1
                return ans
            else: 
                ans = backtrack(n, arr, idx+1, ans)
    return ans

def promise(arr:list, idx:int)->bool:
    k = 0
    while idx > k:
        if arr[idx] == arr[k] or abs(arr[idx] - arr[k]) == (idx-k):
            return False
        k += 1
    return True

def solution(n):
    arr = [-1] * n
    return backtrack(n,arr,0, 0)
