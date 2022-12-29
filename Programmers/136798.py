# 연습문제 lv1. 기사단원의 무기

def solution(number, limit, power):
    ans = 0
    for n in range(1, number+1):
        cnt = 0
        
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                cnt += 1
                if (i**2) != n:
                    cnt += 1
        
            if cnt > limit:
                cnt = power
                break
            
        ans += cnt
    return ans
