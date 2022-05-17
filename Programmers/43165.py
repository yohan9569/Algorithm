# programmers 프로그래머스 43165번 타겟 넘버


# -1, 1 로 곱하는 방식
def solution(nums, t):
    from itertools import product as pr
    case=pr([1,-1],repeat=len(nums))
    ans=0
    for c in case:
        calc=[a*b for a,b in zip(c,nums)]
        if sum(calc)==t:
            ans+=1
    return ans


# 실패 사례들
# 시간 초과
def solution(nums, t):
    from itertools import product as pr
    case=pr(['+','-'],repeat=len(nums))
    ans=0
    for c in case:
        calc=[*zip(c,nums)]
        calc2=''
        for i,j in calc:
            calc2+=i+str(j)
        res=eval(calc2)
        if res==t:
            ans+=1
    return ans

# 시간 초과
def solution(nums, t):
    from itertools import product as pr
    nums=[*map(str,nums)]
    case=pr(['+','-'],repeat=len(nums))
    ans=0
    for c in case:
        calc=''.join([''.join(cal) for cal in zip(c,nums)])
        if eval(calc)==t:
            ans+=1
    return ans

# import operator -> operator.add 로 해보려했으나 간단히 다뤄지지 않음.
