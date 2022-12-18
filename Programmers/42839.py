# 완전탐색 lv2. 소수 찾기


from itertools import permutations as pm
def solution(numbers):
    ans = []
    numbers = [*map(int, numbers)]
    
    # 가능한 숫자 조합
    case = set()
    for r in range(1, len(numbers)+1):
        case = case | {int("".join(map(str, c))) for c in pm(numbers, r)}
    Max = max(case) +1
    
    # 가장 큰 수 이하에 에라토스테네스의 체
    arr = [1] * Max
    for i in range(2, int(Max**0.5)+1):
        if arr[i]:
            for j in range(2*i, Max, i):
                arr[j]=0
    
    # 소수인 숫자 찾기
    for i in case:
        if i>1 and arr[i]:
            ans.append(i)
    
    return len(ans)



# better case
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
