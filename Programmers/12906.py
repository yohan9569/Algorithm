# programmers 연습문제 12906번 같은 숫자는 싫어

# 내 풀이
def solution(arr):
    ans=[arr[0]]
    for a in arr:
        if ans[-1]==a: continue
        ans.append(a)
    return ans



# 실패 사례 - 시간 초과
def solution(arr):
    a=[]
    for i,n in enumerate(arr[:-1]):
        if n != arr[i+1]: a.append(n)
    if a[-1]!=arr[-1]: a.append(arr[-1])
    return a
# 실패 사례 - 시간 초과
def solution(arr):
    ans=[]
    for a,b in zip(arr,arr[1:]):
        if a!=b: ans.append(a)
    if ans[-1]!=arr[-1]: ans.append(arr[-1])
    return ans



# 우수 풀이들
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

def no_continuous(s):
    result = []
    for c in s:
        if (len(result) == 0) or (result[-1] != c):
            result.append(c)
    return result
