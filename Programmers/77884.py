# 월간 코드 챌린지 시즌2 lv1. 약수의 개수와 덧셈

def cnt_div(n):
    div = set()
    for j in range(1, int(n**(1/2))+1):
        if n % j == 0:
            div.update([j, n//j])
    return len(div)


def solution(l, r):
    ans = 0
    
    for i in range(l, r+1):
        if cnt_div(i) % 2 == 0:
            ans += i
        else:
            ans -= i

    return ans
