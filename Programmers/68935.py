# 월간 코드 챌린지 시즌1 lv1. 3진법 뒤집기


def solution(n):
    ans = ''
    
    # 앞뒤 반전, 3진법
    while n:
        n, t = divmod(n, 3)
        ans+=str(t)
    
    # 10진법
    return int(ans,3)
