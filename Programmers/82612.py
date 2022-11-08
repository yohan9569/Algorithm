# 위클리 챌린지 lv1. 부족한 금액 계산하기

def solution(price, money, count):
    ans = sum(c*price for c in range(count+1)) - money
    return ans if ans > 0 else 0
